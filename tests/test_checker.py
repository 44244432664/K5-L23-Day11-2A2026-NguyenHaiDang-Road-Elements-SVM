"""The checker must pass its own mandatory self-test and keep the rubric identical to lab/AGENTS.md."""
import io
import re
from collections import Counter
from pathlib import Path

from road_lab import road_check as rc
from road_lab.cvat_xml import Shape
from road_lab.synthetic import synthetic_gt

ROOT = Path(__file__).resolve().parents[1]


def test_selftest_passes():
    out = io.StringIO()
    assert rc.selftest(synthetic_gt(), out), out.getvalue()


def test_gt_against_itself_is_perfect():
    gt = synthetic_gt()
    res = rc.check(gt, gt, "gt")
    assert res.findings == []
    assert res.auto_score == rc.AUTO_MAX == 78
    assert res.decision == "Release"


def test_each_perturbation_caught_exactly_once():
    gt = synthetic_gt()
    sub, expected = rc.perturb(gt)
    res = rc.check(gt, sub, "p")
    assert Counter((f.image, f.code) for f in res.findings) == Counter(expected)
    assert sorted(c for _, c in expected) == ["QC1-01", "QC1-04", "QC1-04", "QC1-05", "QC1-08"]
    assert res.decision == "Rework"  # camera tag and front light colour are critical


def test_missing_core_image_lowers_attempted_not_score_rate():
    gt = synthetic_gt()
    sub = [im for im in gt if not im.name.startswith("A12")]
    res = rc.check(gt, sub, "partial")
    assert "A12" in res.missing
    assert res.auto_score == rc.AUTO_MAX  # criteria are rated on attempted images only


def test_rubric_totals():
    assert sum(p for *_, p, _a in [(r[0], r[1], r[2], r[3]) for r in rc.RUBRIC]) == 100
    manual = {rid: p for rid, _, p, auto in rc.RUBRIC if not auto}
    assert manual == {"screens": 2, "qc1": 15, "report": 5}


def _table_points(md: str) -> list[int]:
    m = re.search(r"<!-- rubric:start -->(.*?)<!-- rubric:end -->", md, re.S)
    assert m, "rubric markers missing"
    return [int(x) for x in re.findall(r"^\|[^|]+\|[^|]+\|\s*(\d+)\s*\|\s*$", m.group(1), re.M)]


def test_rubric_identical_in_agents_and_rubric_md():
    agents = (ROOT / "lab" / "AGENTS.md").read_text(encoding="utf-8")
    rubric = (ROOT / "RUBRIC.md").read_text(encoding="utf-8")
    a = re.search(r"<!-- rubric:start -->(.*?)<!-- rubric:end -->", agents, re.S).group(1)
    b = re.search(r"<!-- rubric:start -->(.*?)<!-- rubric:end -->", rubric, re.S).group(1)
    assert a.strip() == b.strip()
    pts = _table_points(agents)
    assert pts == [10, 25, 10, 10, 15, 10, 15, 5]
    assert "+0,5" in a and "+4" in a


def test_lint_flags_far_to_near_and_missing_tag():
    gt = synthetic_gt()
    im = gt[0].copy()
    im.tags = [t for t in im.tags if t.label != "weather"]
    lane = next(s for s in im.shapes if s.label == "lane")
    lane.points = list(reversed(lane.points))
    codes = {f.code for f in rc.lint([im])}
    assert "QC1-01" in codes or "QC1-12" in codes
    assert "QC1-04" in codes


def test_lint_clean_on_gt():
    assert [f for f in rc.lint(synthetic_gt()) if f.severity != "minor"] == []


def test_cli_selftest_and_check(tmp_path, capsys):
    from road_lab.cvat_xml import write
    gt = synthetic_gt()
    p = tmp_path / "gt.xml"
    write(gt, p)
    assert rc.main(["selftest", "--gt", str(p)]) == 0
    assert "SELFTEST PASS" in capsys.readouterr().out
    md = tmp_path / "qc1.md"
    assert rc.main(["check", "--gt", str(p), "--sub", str(p), "--name", "x", "--qc1-md", str(md)]) == 0
    text = md.read_text(encoding="utf-8")
    for code in rc.CODE_TITLES:
        assert code in text


def test_unknown_label_is_file_error():
    gt = synthetic_gt()
    sub = [im.copy() for im in gt]
    sub[0].shapes.append(Shape("pothole", "polygon", [(0, 0), (10, 0), (10, 10)], {}))
    res = rc.check(gt, sub, "bad")
    assert any(f.code == "QC1-12" for f in res.findings)


def test_duplicate_slot_grades_labelled_copy_and_warns():
    gt = synthetic_gt()
    sub = [im.copy() for im in gt]
    empty = sub[0].copy()
    empty.shapes, empty.tags = [], []
    sub.insert(0, empty)  # an empty duplicate listed first must not hide the labelled copy
    res = rc.check(gt, sub, "dup")
    slot = rc.image_slot(gt[0].name)
    assert slot in res.attempted and slot not in res.missing
    assert res.auto_score == rc.AUTO_MAX
    assert [f.image for f in res.findings if f.code == "QC1-12"] == [slot]
    assert any(f.image == slot and "2 lần" in f.message for f in rc.lint(sub))
    assert len(rc.label_counts(sub)) == len(sub)
