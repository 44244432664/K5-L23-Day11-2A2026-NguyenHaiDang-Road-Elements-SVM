# Guideline Road v1.0 · AI20K K5 · Ngày 11

Đây là guideline do khóa học soạn để gán nhãn phần tử đường. Nó không phải guideline chính thức của BDD100K hay WoodScape: hai bộ dữ liệu đó chỉ cung cấp ảnh (và nhãn nền cho coach). Khi guideline này khác cách gán gốc của dataset, bạn làm theo guideline này.

Đọc ở đâu: bài giảng sáng, slide 28–42 (làn, vùng lái, đèn, biển) và slide 55–58 (fisheye); phần này; slide 9–10 của deck thực hành. Ngày 20 mở rộng thành phiên bản 1.x (ô đỗ, ca mưa, đêm); mã và nghĩa các quy tắc dưới đây không đổi. Bản máy đọc cho script: [`lab/AGENTS.md`](../lab/AGENTS.md).

## 1. Gán gì, vẽ hình gì, dạng gì

| Label | Dạng trong CVAT | Vẽ cái gì trên ảnh | Thuộc tính |
| --- | --- | --- | --- |
| `lane` | polyline (đường gấp khúc, hở) | Một vạch kẻ làn: nối các điểm nằm trên tâm vệt sơn, từ gần xe ra xa | position L1, R1, L2, R2, other · style solid, dashed · color white, yellow, other · kind single, double |
| `road_curb` | polyline | Mép đường là vỉa hè hoặc lề, nơi không có vạch sơn | không có |
| `crosswalk` | polygon (vùng kín) | Cả vùng vạch ngựa vạn, một polygon bao các vạch | không có |
| `drivable` | polygon | Phần mặt đường xe đi được nếu đường trống | area_type direct (làn đang đi), alternative (làn cùng chiều bên cạnh) |
| `traffic_light` | rectangle (hộp chữ nhật) | Cả vỏ cụm đèn, hộp sát mép | color red, yellow, green, off, unknown · type vehicle, pedestrian, beacon · facing front, side, back · edge_zone (ô tick) |
| `traffic_sign` | rectangle | Cả tấm biển, hộp sát mép (biển phụ có hộp riêng) | group prohibitory, mandatory, warning, information, supplementary, other · facing front, side, back · edge_zone |
| Tag ảnh | tag (nhãn cho cả ảnh, không vẽ hình) | Gắn cho mỗi ảnh một lần | camera front, fisheye_front, fisheye_rear, fisheye_left, fisheye_right · timeofday day, dusk, night · weather clear, rain, fog, other · source real, simulated |

Cờ occluded có sẵn trong CVAT: bật cho đoạn polyline bạn nối qua chỗ bị che.

Trên CVAT của lớp, mỗi tag ảnh là một label kiểu Tag có một thuộc tính select tên `value` (ví dụ label `camera`, thuộc tính `value` = `fisheye_left`).

## 2. Thứ tự làm trên mỗi ảnh

1. Bốn tag ảnh (camera trước tiên).
2. Làn: R1 và L1, rồi L2 và R2 nếu thấy; road_curb nếu mép đường không sơn.
3. Thuộc tính của từng vạch; bật occluded nếu có đoạn nối qua chỗ che.
4. drivable (direct, rồi alternative nếu có); crosswalk nếu có.
5. Hộp đèn và biển, đủ thuộc tính.
6. Ctrl+S.

Mỗi ảnh chỉ yêu cầu nhóm label ghi ở bảng kế hoạch ảnh (slide Task 1, Task 2 của deck thực hành); không gán những loại không được yêu cầu cho ảnh đó.

## 3. Quy tắc

### Làn (lane)

- Polyline đặt trên tâm vệt sơn, không đặt ở mép vạch.
- Vẽ từ gần xe ra xa. Điểm đầu sát xe là điểm quan trọng nhất, đặt thật chính xác.
- Vạch đứt là một polyline, không phải mỗi vệt một đường.
- Đoạn bị che ngắn (xe, người): nối liền qua chỗ che và bật occluded. Đừng dừng trước vật che.
- Dừng ở điểm xa nhất còn thấy vạch, không kéo tới chân trời.
- Lệch khỏi tâm vạch tối đa 5 px. Thêm điểm ở chỗ vạch cong.
- position tính theo làn đang đi: L1 và R1 là hai vạch sát xe, L2 và R2 là vạch kế tiếp bên ngoài.

### Vùng lái (drivable)

Gán theo "đi được nếu đường trống", không khoét lỗ quanh xe khác. Không gồm lề, vỉa hè, thân xe mình, vùng phía sau cọc.

### Đèn và biển

- Gán mọi cụm đèn và tấm biển cao từ 8 px trở lên.
- Hộp sát vỏ đèn hoặc mép biển, không gồm cần treo.
- color của đèn là màu đang sáng trong ảnh này; đèn tắt là off.
- Biển phụ (tấm nhỏ dưới biển chính) có hộp riêng, group = supplementary.
- Hình biển in trên thùng xe, ảnh phản chiếu không phải biển: không gán.

### Nhóm biển (group) cho biển trong ảnh BDD100K (biển Mỹ)

Ảnh BDD100K quay ở Mỹ nên hình dạng và màu biển khác biển Việt Nam (QCVN 41:2024/BGTVT). Bạn phân nhóm theo chức năng của biển, không theo hình dạng hay màu. Năm nhóm này tương ứng năm nhóm của quy chuẩn Việt Nam.

| group | Tương ứng ở Việt Nam | Biển Mỹ thường gặp trong ảnh |
| --- | --- | --- |
| prohibitory | biển cấm | Stop, Yield, Speed Limit, Do Not Enter, Wrong Way, No Left Turn, No U-Turn, No Parking, No Trucks |
| mandatory | biển hiệu lệnh | One Way, Keep Right, Keep Left, Left Turn Only, Straight Only (biển bắt buộc đi theo hướng) |
| warning | biển nguy hiểm và cảnh báo | hình thoi vàng (đường cong, giao lộ, đèn tín hiệu phía trước, người đi bộ qua đường, trường học); biển công trường màu cam |
| information | biển chỉ dẫn | biển xanh lá chỉ hướng và lối ra, biển số đường (route shield), biển xanh dương dịch vụ (bệnh viện, trạm xăng) |
| supplementary | biển phụ | tấm chữ nhật nhỏ đi kèm biển chính ("SCHOOL", "XING", mũi tên, "500 FT", thời gian, "EXCEPT ...") |
| other | không thuộc năm nhóm | chỉ dùng khi không xếp được; ghi vào bảng ca khó |

Biển không chắc nhóm: chọn nhóm gần nhất theo chức năng, ghi vào bảng ca khó kèm lý do; coach không trừ điểm khi lý do hợp lý.

## 4. Riêng ảnh fisheye (camera bắt đầu bằng fisheye_)

- Polyline đi theo cung cong trên ảnh; vạch thẳng ngoài đời thành cong trên ảnh. Không nối hai điểm đầu cuối, không nắn ảnh. Mọi chỗ lệch ≤ 5 px, đặt điểm dày ở vòng ngoài nơi cung cong nhất.
- Thân xe mình và vùng tối viền ảnh: không gán, và không tính vào vùng lái.
- position L1/R1/L2/R2 chỉ dùng ở fisheye_front và fisheye_rear. Ở fisheye_left và fisheye_right luôn dùng position = other.
- Đèn, biển có tâm hộp nằm ngoài 80 % bán kính vòng ảnh: bật edge_zone. Hộp vẫn thẳng, sát pixel, ôm cả phần nền ở các góc.
- Vạch ngựa vạn gán crosswalk (polygon). Vạch ô đỗ không gán lane.

## 5. Kiểm trước khi nộp (self-QC)

- [ ] Mọi ảnh đủ bốn tag, camera đúng.
- [ ] Mọi polyline đi từ gần ra xa, vạch đứt là một đường, chỗ che có occluded.
- [ ] Không còn L1 hoặc R1 bị thiếu khi thấy được; không nhầm L1 với L2.
- [ ] Hộp đèn, biển sát và đủ thuộc tính.
- [ ] Ảnh fisheye: theo cung, không gán thân xe.
- [ ] Export CVAT for images 1.1 và mở lại được (`python -m road_lab.road_check lint <file>.zip`).

---
AI20K · AI in Action · VinUni. Dữ liệu BDD100K © 2018 The Regents of the University of California, theo BDD100K License.
