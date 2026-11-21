# Báo cáo cá nhân — Ngày 11

Họ tên: Nguyễn Hải Đăng. Mã học viên: 2A202603190
CVAT: **2.81.0**, local Docker `http://localhost:8080`. Guideline: **Road v1.0**, kèm các giả định được ghi ở Phiếu QC1.
Lần nộp (`revision`): **2**. Native export chuẩn bị **2026-11-21 00:56:29 +07**. Có một chu kỳ sửa sau QC.
Báo cáo được Codex soạn từ dữ liệu đã lưu và hướng dẫn của học viên.

## 1. Kiểm project

| Mục | Đúng Road v1.0? | Ghi chú |
| --- | --- | --- |
| 6 label, đúng kiểu | Có | lane/road_curb polyline; crosswalk/drivable polygon; traffic_light/traffic_sign rectangle. |
| Thuộc tính và giá trị | Có về schema | Đối chiếu đầy đủ schema CVAT với taxonomy repo; lỗi giá trị gán theo ảnh còn ghi ở Phiếu QC1. |
| 4 tag ảnh | Có | Mọi ảnh core có camera, timeofday, weather, source; camera/source đúng. A10 weather còn cần rain theo rule mặt đường ướt. |
| Job completed | Có | #13 và #15 có state=completed, stage=annotation; giữ nguyên. |

## 2. Số lượng đã gán

| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front | 12 | 38 | 14 | 7 | 23 | 26 | 30 |
| fisheye | 8 | 9 | 12 | 9 | 11 | 2 | 3 |
| front-extra | Loại khỏi phạm vi | — | — | — | — | — | — |
| fisheye-extra | Loại khỏi phạm vi | — | — | — | — | — | — |

Tổng core: **20 ảnh, 184 shapes, 80 tags**. Không dùng số đếm của extra.

## 3. Bảng ca khó

| Ảnh | Nhãn | Phân vân giữa | Đã chọn | Lý do |
| --- | --- | --- | --- | --- |
| A02/A03/A08/A12 | lane.position | Nhận định người kiểm / học viên | Giữ nguyên, giả định đúng | Học viên yêu cầu chờ verdict coach; không tính lỗi position trong phiếu này. |
| Các ảnh có xe khác | drivable | Road if empty / car cutout | Chấp nhận cutout lần này | Theo yêu cầu học viên; chưa ghi nhận là coach xác nhận bằng chứng. |
| A04/A09/A11 | lane.kind=double | Một / hai polyline | Hai polyline | Coach yêu cầu hai polyline theo hai vệt sơn. |
| A05 và đường không kẻ làn | drivable.area_type | direct / alternative | direct cho mặt đường tiếp cận không có marking | Theo clarification coach; không gồm đối diện hay emergency stop. |
| A07 | lane R1 | Biên gần sedan / vạch ngoài cùng | Còn Rework | Polyline hiện tại chưa nằm trên vạch solid R1 gần xe. |

## 4. Phiếu QC 1 nhận được

Người kiểm: **Nguyễn Gia Huy**. Quyết định hiện tại: **Rework**. Xem [Phiếu QC1 tổng hợp](nguyengiahuy-qc1-for-nguyenhaidang.md): **1 lỗi nặng, 12 lỗi chính / 264 nhãn = 4.55%, 1 lỗi nhẹ**. Phiếu gồm kết quả hiện hành và hai vòng kiểm cũ trong phụ lục; không cộng dồn số lỗi giữa các vòng.

| Mã lỗi / nhóm | Số lỗi còn | Đồng ý / xử lý | Đã sửa? |
| --- | ---: | --- | --- |
| QC1-01 | 1 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-02 | 1 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-04 | 2 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-05 | 1 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-06 | 6 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-09 | 1 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| QC1-11 | 2 | Không nằm trong giả định miễn của lần này | Còn theo phiếu hiện tại |
| Position A02/A03/A08/A12 | 0 tính lỗi | Chấp nhận theo giả định, chờ coach | Giữ nguyên |
| Car cutout | 0 tính lỗi | Chấp nhận theo giả định | Giữ nguyên |
| Thiếu tag, B05/B07/B08 position, sign nhóm đã sửa, B02/B04 edge_zone | 0 còn trong các mục đã khắc phục | Đối chiếu với snapshot mới | Đã sửa bởi học viên |

A10: đã tách cụm biển thành #3196/#3227/#3228; #3203 đã đổi mandatory nhưng ONE WAY #3202 còn information. B03: #3085 được bật edge_zone, trong khi #3084 ngoài rìa còn false; cần đổi #3084=true và #3085=false.

### Phiếu QC1 đã thực hiện cho bạn

Tôi kiểm lô của **Nguyễn Gia Huy**, ghi trong [nguyenhaidang-qc1-for-nguyengiahuy.md](nguyenhaidang-qc1-for-nguyengiahuy.md). Mẫu gồm A04, A08, B02, B03, B04 và B06: **6 ảnh, 114 nhãn = 90 shape + 24 tag**. Phiếu ghi nhận không còn lỗi xác nhận trong mẫu sau sửa, với 10 mục cũ được giữ để truy vết. Quyết định của phiếu là **Hold**, chờ coach xác nhận ngoại lệ vạch không nhìn thấy và quy ước L/R cho camera sau.

Hai mục lịch sử về vạch đôi A04 dùng cách biểu diễn một polyline, khác với chỉ dẫn hai polyline theo hai vệt sơn được áp dụng trong phiếu nhận được. Đã ghi rõ điểm cần đối chiếu trong phiếu kiểm cho bạn; không suy ra Release hoặc tự thay đổi số lỗi khi chưa kiểm lại dữ liệu của bạn.

Phiếu tôi viết cho bạn là file QC thuộc bộ 5 file nộp theo SUBMISSION.md. Phiếu Nguyễn Gia Huy viết cho tôi là tài liệu phản hồi bổ sung trong gói lưu hồ sơ.

## 5. Kiểm file export

| File | Mở lại được? | Shape ảnh 1 job/file | Shape ảnh 2 job/file | Tag camera trong XML? |
| --- | --- | --- | --- | --- |
| nguyenhaidang-front.zip | Có, native 1.1 | A01: 10/10 | A02: 8/8 | Có, đúng mọi ảnh |
| nguyenhaidang-fisheye.zip | Có, native 1.1 | B01: 4/4 | B02: 7/7 | Có, đúng mọi ảnh |

Đã kiểm **toàn bộ** shape/tag của 20 ảnh với API, không chỉ hai ảnh trong bảng. ZIP chỉ có `annotations.xml`; `contains_images=false`. SHA-256 nằm trong manifest. Kiểm mở lại bằng parser/lint được thực hiện; không re-import vào task thật vì sẽ làm thay đổi nhãn.

Raw lint: **9 nặng / 18 chính / 22 nhẹ**. Giữ nguyên cảnh báo và đối chiếu từng dòng ở [CSV](evidence/lint-reconciliation.csv). Không khẳng định đạt điều kiện “không còn cảnh báo nặng” hoặc coach đã duyệt ngoại lệ.

## 6. Ảnh chụp màn hình

1. [Project Labels trong CVAT](evidence/project-labels.png).
2. [A08 front trong CVAT](evidence/front-cvat.png).
3. [B05 fisheye trong CVAT](evidence/fisheye-cvat.png), [phóng to đoạn cung từ screenshot](evidence/fisheye-curve-detail.png).
4. [Trích đoạn XML native có polyline lane](evidence/xml-polyline.png).

## 7. Tự đánh giá

Nhóm cần kiểm kỹ trước lần sau là QC1-06 và QC1-11: mở Details của từng đối tượng để so thuộc tính với vệt sơn; xác định tâm box trước khi bật edge_zone. Với vạch đôi, giữ hai polyline theo chỉ dẫn coach. Khi có tranh luận, ghi giả định và chờ verdict thay vì âm thầm đổi tiêu chí.

Polyline lane tạo nhãn mục tiêu cho mô hình tìm vạch / phân loại vị trí. Ví dụ B05/B07/B08 đã sửa position sang other: giữ L1/R1 ở camera bên sẽ đưa mục tiêu vị trí sai vào dữ liệu học. Không có thí nghiệm huấn luyện hoặc điểm model nào được thực hiện trong lần QC này.

## 8. Hoạt động row anchor tùy chọn

Không thực hiện: mục buffer tùy chọn, không chấm điểm. Không tạo số x hoặc so sánh với bạn khác khi không có dữ liệu của họ.

**Trạng thái bàn giao:** đủ các file và bằng chứng kỹ thuật cho 20 ảnh core; chưa Release QC vì còn A07 và các mục ghi trên phiếu.
