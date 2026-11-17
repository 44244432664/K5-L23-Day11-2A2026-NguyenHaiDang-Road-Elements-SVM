# Nộp bài (hạn 16:35, Ngày 11)

Nộp đúng 4 file lên kênh nộp bài coach chỉ định. Không gửi file GT, không gửi ảnh và không đăng file lên kênh chung của lớp.

- [ ] `<tên>-front.zip`: CVAT for images 1.1, **không kèm ảnh**; gồm task front (A01–A12) và front-extra nếu có làm.
- [ ] `<tên>-fisheye.zip`: CVAT for images 1.1, **không kèm ảnh**; gồm task fisheye (B01–B08) và fisheye-extra nếu có làm.
- [ ] `<tên>-qc1-for-<tên bạn được kiểm>.md`: Phiếu QC 1 đã điền theo [`templates/qc1_form.md`](templates/qc1_form.md).
- [ ] `<tên>-report.md`: báo cáo theo [`templates/report.md`](templates/report.md).

Trước khi nộp:

- [ ] Mọi job ở trạng thái **completed**.
- [ ] Đã mở lại hai file zip và chạy `PYTHONPATH=src python3 -m road_lab.road_check lint <tên>-front.zip <tên>-fisheye.zip`; không còn dòng nào mức nặng.
- [ ] Mọi ảnh có đủ bốn tag, tag camera đúng.
- [ ] Báo cáo có ảnh chụp màn hình và bảng kiểm file (mục 1).

Sửa sau buffer: nộp lại hai file zip cùng tên, ghi vào mục 4 của báo cáo đã sửa những gì.
