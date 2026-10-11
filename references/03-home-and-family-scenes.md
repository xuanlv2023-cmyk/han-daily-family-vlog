# BỐI CẢNH GIA ĐÌNH & KHÔNG GIAN ĐỜI THƯỜNG (SCENES & SETTINGS)
## Skill: `han-daily-family-vlog` • Token Registry: `@_Location_...`

Tài liệu quy chuẩn các bối cảnh gia đình với hệ thống Token đồng bộ, ánh sáng thực tế và loại bỏ triệt để hiệu ứng 3D hoạt hình nhân tạo.

---

### 1. HỆ THỐNG TOKEN BỐI CẢNH ĐỒNG BỘ (LOCATION TOKENS)

Khi viết prompt Keyframe và Video, bắt buộc khai báo Token bối cảnh tương ứng trong thẻ `[ENVIRONMENT & LIGHTING]`:

| Token Bối Cảnh | Tên Không Gian | Đặc Trưng Không Gian & Ánh Sáng Thực Tế |
| :--- | :--- | :--- |
| `@_Location_Living_Room` | Phòng khách chung cư hiện đại | Sofa da be, thảm xốp/lông mềm, cửa ban công đón ánh sáng ban ngày tự nhiên dịu nhẹ, đồ chơi trẻ em gọn gàng. |
| `@_Location_Kitchen_Dining` | Bàn ăn & Đảo bếp gia đình | Đảo bếp đá cẩm thạch trắng, đĩa hoa quả/bánh kẹo tươi ngon, đèn thả ấm áp, ghế ngồi của bé. |
| `@_Location_Master_Bedroom` | Phòng ngủ bố mẹ & các con | Giường king-size ga gối linen ấm cúng, đèn ngủ ánh vàng dịu, không gian vui đùa trước giờ ngủ. |
| `@_Location_Family_Car` | Khoang xe ô tô gia đình SUV | Ghế da nâu/đỏ đô sang trọng, ánh sáng tự nhiên qua kính xe, bố mẹ ngồi trước, bé Hân ngồi ghế trẻ em phía sau. |

---

### 2. NGUYÊN TẮC ÁNH SÁNG ĐỜI THƯỜNG (ANTI-CGI LIGHTING)

> **⚠️ BỘ QUY TẮC ÁNH SÁNG GIA ĐÌNH CHÂN THỰC:**
> 1. **Loại bỏ ánh sáng hoạt hình Pixar:** Cấm dùng `cinematic volumetric rays, glossy 3D lighting, cartoon bloom, unreal engine`. Chúng làm căn nhà trông như cảnh dựng 3D.
> 2. **Ánh sáng sinh hoạt tự nhiên (Natural Domestic Ambient Light):**
>    - Ánh sáng ban ngày mềm mại khuếch tán qua rèm voan trắng từ cửa sổ ban công lớn.
>    - Ánh đèn trần downlight vàng dịu (3000K) ấm cúng vào buổi tối.
>    - Bóng tiếp đất chân thực dưới sàn nhà (floor contact shadows) của bàn chân bé và các đồ vật/đồ chơi.
> 3. **Chất cảm biến máy ảnh gia đình:**
>    - Khóa chất máy ảnh: `shot on Sony A7 IV with 35mm f/1.8 lens, natural dynamic range, true-to-life domestic colors, pristine sensor capture, unretouched real human photography, zero CGI rendering`.

---

### 3. PROMPTS MẪU TỪNG BỐI CẢNH (CAMERA SENSOR CAPTURE)

#### Bối cảnh 1: Phòng khách chung cư (`@_Location_Living_Room`)
```text
inside @_Location_Living_Room, a bright warm luxury Scandinavian living room, comfortable beige modular sofa, circular wooden coffee table, soft cream area rug, large window with sheer white curtains letting in soft natural daylight, natural floor contact shadows, cozy domestic family atmosphere, shot on Sony A7 IV with 35mm f/1.8 lens, pristine clean sensor image, zero CGI rendering, zero 3D look
```

#### Bối cảnh 2: Gian bếp & Bàn ăn (`@_Location_Kitchen_Dining`)
```text
inside @_Location_Kitchen_Dining, a modern open-concept family kitchen with white marble island counter, stylish pendant lights casting warm gentle glow, wooden shelves with pastel ceramics, fresh fruit platter on counter, bright airy domestic atmosphere, true-to-life indoor lighting, zero artificial bloom
```
