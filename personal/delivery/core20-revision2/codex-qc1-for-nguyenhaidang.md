# Phiếu QC 1 — Road v1.0

Lô được kiểm (học viên): **Nguyen Hai Dang**. Người kiểm: **Codex, mô phỏng vai trò bạn kiểm; không phải chữ ký của một học viên khác**.
Ngày: **2026-11-21 01:04:31 +07**. Guideline: **Road v1.0 + các giả định học viên yêu cầu**.
File được kiểm: `nguyenhaidang-front.zip`, `nguyenhaidang-fisheye.zip`; manifest `nguyenhaidang-manifest.json`, **revision 2**.
Số ảnh kiểm: **20 core, 0 extra**. Số nhãn đã kiểm: **264 = 184 shapes + 80 tags**.
Phạm vi CVAT: project #3; job/task #13 và #15. Task #14/#16 và mọi ảnh extra bị loại khỏi kiểm và export.

## Tổng hợp theo mã

| Mã | Loại lỗi | Số mục kiểm | Số lỗi | Mức |
| --- | --- | ---: | ---: | --- |
| QC1-01 tag camera và tag ảnh | sai thuộc tính / bỏ sót | 80 | 1 | nhẹ (tag khác camera) |
| QC1-02 đủ L1, R1 khi thấy vạch | bỏ sót | 32 | 1 | nặng |
| QC1-03 position | sai thuộc tính / thừa | 47 | 0 | nặng |
| QC1-04 tâm vạch, chiều, điểm dừng | sai phạm vi / chiều | 47 | 2 | chính |
| QC1-05 vạch đứt, che | sai phạm vi / thuộc tính | 47 | 1 | chính |
| QC1-06 style, color, kind | sai thuộc tính | 47 | 6 | chính |
| QC1-07 vùng lái, crosswalk, curb | sai phạm vi / bỏ sót / thừa | 76 | 0 | chính |
| QC1-08 đèn, màu | bỏ sót / phạm vi / thuộc tính | 28 | 0 | nặng / chính |
| QC1-09 facing, type, group, biển phụ | sai thuộc tính / cách tách biển | 61 | 1 | chính |
| QC1-10 hình in, đủ biển | bỏ sót / sai phạm vi | 33 | 0 | chính |
| QC1-11 fisheye / edge_zone | sai thuộc tính / phạm vi | 46 | 2 | chính |
| QC1-12 file | lỗi file | 2 | 0 | nhẹ / nặng |

QC1-02 gồm 32 vị trí biên được sàng lọc ở 16 ảnh front/rear; chỉ tính lỗi khi có vạch nhìn thấy. QC1-03: 47 lane, trong đó position của 16 lane ở A02/A03/A08/A12 được chấp nhận theo giả định. QC1-07 không tính car cutout. QC1-10 kiểm 33 box biển và quét cả 20 ảnh; kiểm đầy đủ nhóm label bị giới hạn bởi bảng kế hoạch chưa có. Số mục kiểm giữa các mã có thể trùng nhau.

## Danh sách lỗi (mỗi lỗi một dòng)

| # | Mã | Ảnh | Nhãn (label, id CVAT) | Mức | Mô tả và hướng sửa |
| ---: | --- | --- | --- | --- | --- |
| 1 | QC1-02 | A07 | lane #3136 / #3226; unannotated solid R1 | nặng | Both current lane polylines trace the outer right-hand dashed marking. The prominent solid white boundary immediately right of the silver sedan, around (772,563) to (695,270), is still not annotated as lane. Add the actual solid R1; assign the outer dashed marking R2. The green drivable edge does not replace a lane polyline. Counted as one combined critical boundary finding. |
| 2 | QC1-04 | A04 | lane #3113 | chính | Polyline runs from (604,323) to (718,536), far to near. Reverse its point order so the near endpoint comes first. |
| 3 | QC1-04 | B03 | lane #3016 | chính | Polyline starts near the distant car at (677,285) and ends nearer the camera at (785,361). Reverse the point order. |
| 4 | QC1-05 | A07 | lane #3136 + #3226 | chính | Two fragments still describe the same outer dashed marking. Join its visible fragments and gaps into one polyline, without merging physically separate lines of a double marking. |
| 5 | QC1-06 | A02 | lane #3098 | chính | The outer-left marking has separated white dashes but style=solid. Use dashed. |
| 6 | QC1-06 | A02 | lane #3099 | chính | The nearer-left marking has separated white dashes but style=solid. Use dashed. |
| 7 | QC1-06 | A03 | lane #3104 | chính | The left boundary paint is yellow but color=white. Use yellow. |
| 8 | QC1-06 | A03 | lane #3105 | chính | The right boundary consists of separated white dashes but style=solid. Use dashed. |
| 9 | QC1-06 | A07 | lane #3136 + #3226 | chính | The outer marking is dashed, but both current fragments have style=solid. Use dashed. This is one physical-marking attribute finding. |
| 10 | QC1-06 | A12 | lane #3213 | chính | The distant right boundary has separated white dashes but style=solid. Use dashed. |
| 11 | QC1-09 | A10 | traffic_sign #3202 | chính | The ONE WAY arrow plate is grouped information. Use group=mandatory. |
| 12 | QC1-11 | B03 | traffic_sign #3084 | chính | edge_zone=false, but box center (1144.2,379.4) is 514.7px from image center, outside the lab radius threshold 0.8 Ä‚â€” 640 = 512px. Set edge_zone=true under the repo convention. |
| 13 | QC1-01 | A10 | weather tag | nhẹ | The tag is now present but saved as overcast. Road v1.0 weather=rain includes visibly wet pavement from rain, which this image shows. Set rain. This non-camera metadata issue is recorded as minor in this peer review. |
| 14 | QC1-11 | B03 | traffic_sign #3085 | chính | edge_zone was enabled on the central blue sign instead of the peripheral sign #3084. Its box center is inside the 512px radius, so #3085 should have edge_zone=false; #3084 should have true. |

## Ca mơ hồ

| Ảnh | Câu hỏi cho lead | Lời đáp / xử lý lần này |
| --- | --- | --- |
| A02/A03/A08/A12 | Position làn đang tranh luận. | Chấp nhận đúng theo yêu cầu học viên cho lần QC này; chưa có kết luận coach. Không tính lỗi position. |
| Các polygon drivable | Car cutout có được chấp nhận? | Chấp nhận đúng theo yêu cầu học viên. Không tính lỗi cutout; không ghi là coach đã xác nhận. |
| A05/A06/A07/A09/A10 | Miễn cảnh báo L1/R1 tại biên không có vạch sơn nhìn thấy? | Người kiểm không yêu cầu vẽ vạch không tồn tại; xác nhận ngoại lệ chính thức của coach chưa được cung cấp. Riêng A07 còn lỗi R1 nhìn thấy nhưng chưa được gán. |
| A06/B02 | Màu đèn người đi bộ trắng hoặc rất mờ trong taxonomy? | Chưa có quy ước bổ sung; không đoán màu và không tính lỗi nặng. |
| 20 ảnh core | Danh sách nhóm label bắt buộc cho từng ảnh theo slide Task 1/2? | Không có bảng slide đầy đủ trong repo; không tính lỗi bỏ sót nhóm dựa trên suy đoán. |

## Quyết định

**Lỗi nặng: 1. Lỗi chính: 12 / 264 = 4.55%. Lỗi nhẹ: 1. Ca chờ lead: 5 nhóm, đã xử lý bằng giả định hoặc không tính lỗi như bảng trên.**

**Quyết định: Rework.** Còn lỗi nặng A07 nằm ngoài các giả định được chấp nhận. Tỉ lệ lỗi chính dưới 5% không xóa điều kiện lỗi nặng. Không ghi Release hoặc coach phê duyệt khi chưa có xác nhận.

Job #13 và #15 đã có `state=completed`, `stage=annotation` trước khi kiểm. Trạng thái completed là trạng thái tiến độ, không đồng nghĩa Release QC. Không thay đổi nhãn, stage hay state trong lần hoàn tất hồ sơ này.

Hai ZIP native đã mở lại, đối chiếu toàn bộ 20 ảnh / 264 nhãn với API đã lưu và kiểm taxonomy. Không kèm ảnh. Raw lint còn **9 nặng / 18 chính / 22 nhẹ**, gồm nhiều cảnh báo theo khả năng nhìn thấy vạch, double markings, thuộc tính position được giả định, box nhỏ và điểm lặp; chúng được giữ nguyên trong manifest và [bảng đối chiếu](evidence/lint-reconciliation.csv). Không đổi raw lint thành 0.

Ảnh không có lỗi QC đã xác nhận trong phạm vi/giả định: A01, A05, A06, A08, A09, A11, B01, B02, B04, B05, B06, B07, B08. “Không có lỗi xác nhận” không phải so khớp GT hoặc quyết định coach cho ca tranh luận.

Bằng chứng: [kiểm export](evidence/export-checks.json), [danh sách lỗi có cấu trúc](evidence/final-findings.json), [raw lint](evidence/lint-raw.txt). Các review cũ giữ tại `personal/reviews/core20` và `core20-r2`; phiếu này thay thế số lỗi cũ trong phạm vi giả định mới.
