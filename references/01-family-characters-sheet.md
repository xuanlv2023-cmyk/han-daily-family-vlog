# HỒ SƠ 4 NHÂN VẬT GIA ĐÌNH HÂN DAILY & HỆ THỐNG TOKEN ĐỒNG BỘ
## Skill: `han-daily-family-vlog` • Token Registry: 4 Nhân Vật & Đa Bối Cảnh

Tài liệu này xác lập tiêu chuẩn nhận diện hình ảnh cho toàn bộ 4 thành viên gia đình trong kênh **Hân Daily**, đạt chuẩn **CHỤP ẢNH NGƯỜI THẬT 100% (REAL HUMAN DSLR PHOTO)**, loại bỏ hoàn toàn cảm giác tượng sáp đơ hoặc mặt nhựa hoạt hình AI.

---

## 1. HỆ THỐNG TOKEN THAM CHIẾU ĐỒNG BỘ (DYNAMIC TOKEN REGISTRY)

Vì kênh Hân Daily là thể loại hài kịch gia đình đa nhân vật, bắt buộc phải dùng hệ thống Token định danh rõ ràng để AI không bao giờ bị hòa trộn khuôn mặt giữa ba, mẹ, bé Hân và em Bo:

### A. Quy chuẩn Token 4 Nhân vật Gia đình:
- `@_Char_Be_Han` (hoặc `@_Brand_Baby_Lead`): Bé Hân (3-4 tuổi) — Ngôi sao trung tâm, má bánh bao phúng phính.
- `@_Char_Be_Bo` (hoặc `@_Brand_Toddler_Boy`): Em Bo (8-10 tháng) — Em bé trai bụ bẫm, cười khoe 2 răng sữa.
- `@_Char_Me_Uyen` (hoặc `@_Brand_Mother_Lead`): Mẹ Uyên Hân (24-25 tuổi) — Người mẹ trẻ trung, thanh tú, ấm áp.
- `@_Char_Ba_Long` (hoặc `@_Brand_Father_Lead`): Ba Hoàng Long (27 tuổi) — Ông bố đeo kính cận đen, hay trêu con.

### B. Quy chuẩn Token Bối cảnh Nhà Cửa:
- `@_Location_Living_Room`: Phòng khách hiện đại với sofa nỉ kem, thảm chơi xốp trẻ em, kệ đồ chơi.
- `@_Location_Kitchen_Dining`: Bàn ăn gia đình và khu bếp ấm cúng, ghế ăn dặm của bé.
- `@_Location_Kids_Playroom`: Phòng chơi riêng của 2 bé với lều bóng, gấu bông và tranh vẽ tường.

### C. Cơ chế 2 Chế độ (Tự Sáng Tạo vs Clone Đối Thủ):
1. **Chế độ Tự Sáng Tạo:** Gọi đúng Token của các nhân vật xuất hiện trong phân cảnh đó vào thẻ `[CHARACTER ANCHOR]` và gọi Token bối cảnh vào thẻ `[ENVIRONMENT & LIGHTING]`.
2. **Chế độ Clone Đối Thủ (Multimodal Video Audit):**
   - Bóc tách nhân vật bé gái đối thủ $\rightarrow$ ánh xạ sang `@_Char_Be_Han`.
   - Bóc tách bố mẹ đối thủ $\rightarrow$ ánh xạ sang `@_Char_Ba_Long` và `@_Char_Me_Uyen`.
   - Bóc tách bối cảnh phòng khách/nhà bếp tương ứng.

---

## 2. BỘ QUY TẮC TRIỆT TIÊU CHẤT AI (ANTI-AI PHOTOREALISM SYSTEM)

> **⚠️ BỘ QUY TẮC PHÒNG CHỐNG "MẶT SÁP & HOẠT HÌNH AI":**
> 1. **Cấm tuyệt đối từ khóa làm mịn bệt da:** `porcelain skin, flawless, plastic doll, airbrushed, 3D render, Pixar style, anime, CGI`.
> 2. **Bắt buộc dùng da thật trẻ em và người lớn:** `authentic unretouched raw 8k DSLR photograph, natural real child skin texture with delicate micro-pores, soft chubby rosy dumpling cheeks, authentic warm skin tones with natural blood circulation warmth`.
> 3. **Ánh sáng sinh hoạt gia đình đời thường:** `warm natural indoor daylight through living room window, soft diffused ceiling ambient lights, realistic floor contact shadows, zero artificial glow, zero CGI bloom`.
> 4. **Khóa ngũ quan - Giải phóng trang phục:** Ảnh Turnaround chỉ khóa khuôn mặt, độ tuổi và hình thể. Quần áo mặc nhà, váy đầm và đồ chơi thay đổi linh hoạt theo từng tình huống tiểu phẩm.

---

## 3. CHI TIẾT 4 NHÂN VẬT THAM CHIẾU

### 1. BÉ HÂN (3–4 TUỔI) - NGÔI SAO TRUNG TÂM (`@_Char_Be_Han` / `@_Brand_Baby_Lead`)
- **Ảnh tham chiếu:** `01_Be_Han_3Tuoi_Turnaround.jpg`
- **Ngoại hình:** 3 tuổi, má bánh bao phúng phính trắng hồng, đôi mắt to tròn đen láy linh hoạt, búi tóc củ tỏi đính kẹp hoa cúc ngọc trai.
- **Biểu cảm đặc trưng:** Bĩu môi hờn dỗi má bánh bao phồng to, hoặc cười tít mắt ngây thơ, biểu cảm cực kỳ sống động.
- **Prompt Token:**
```text
authentic unretouched raw 8k DSLR photograph, @_Char_Be_Han, a super cute 3-year-old Vietnamese toddler girl, chubby rosy dumpling cheeks, large sparkling round dark brown eyes with expressive natural lashes, charming funny pouty lips with natural lip texture, hair styled in a high topknot bun with a dainty pearl daisy flower hairpin, wearing a tiny pearl beaded crossbody purse, natural real child skin texture with visible delicate micro-pores, zero plastic doll look, zero CGI --style raw
```

### 2. BÉ BO (8–10 THÁNG) - EM TRAI BỤ BẪM (`@_Char_Be_Bo` / `@_Brand_Toddler_Boy`)
- **Ảnh tham chiếu:** `02_Be_Bo_8Thang_Turnaround.jpg`
- **Ngoại hình:** 8 tháng tuổi, em bé trai bụ bẫm tròn xoe, tay chân ngấn bánh mì, hai má núng nính, cười toe toét khoe 2 chiếc răng sữa tí hon, mắt sáng ngơ ngác hóng hớt.
- **Trang phục đặc trưng:** Bodysuit liền thân vải nỉ mềm hình thú cưng có mũ tai gấu ngộ nghĩnh.
- **Prompt Token:**
```text
authentic unretouched 8k DSLR photo, @_Char_Be_Bo, an adorable 8-month-old chubby Vietnamese baby boy, extremely chubby cheeks, cute chunky baby rolls on arms and legs, bright curious eyes with innocent reflections, smiling happily showing two tiny baby front teeth, wearing a soft plush hooded animal romper bodysuit, genuine baby skin with natural soft texture, zero 3D render --style raw
```

### 3. MẸ UYÊN HÂN (24–25 TUỔI) - NGƯỜI MẸ TRẺ TRUNG (`@_Char_Me_Uyen` / `@_Brand_Mother_Lead`)
- **Ảnh tham chiếu:** `03_Me_Uyen_Han_Turnaround.jpg`
- **Ngoại hình:** 25 tuổi, nét đẹp thuần Việt thanh tú, da sáng tự nhiên có kết cấu thật, vóc dáng thon thả, mái tóc đen dài uốn lượn bồng bềnh, nụ cười rạng rỡ ấm áp yêu thương con.
- **Phong cách:** Trẻ trung, trang nhã (áo len dệt kim mềm, váy chữ A mặc nhà).
- **Prompt Token:**
```text
authentic raw 8k DSLR camera capture, @_Char_Me_Uyen, a gorgeous 25-year-old Vietnamese mother, delicate oval face, natural soft matte skin finish with visible micro-pores, graceful long wavy dark hair, warm loving radiant smile, slender fit hourglass figure, elegant modern young mom aesthetic, natural indoor lighting, zero airbrushed skin, zero waxy shine --style raw
```

### 4. BA HOÀNG LONG (27 TUỔI) - ÔNG BỐ HÀI HƯỚC (`@_Char_Ba_Long` / `@_Brand_Father_Lead`)
- **Ảnh tham chiếu:** `04_Ba_Hoang_Long_Turnaround.jpg`
- **Ngoại hình:** 27 tuổi, gương mặt điển trai hiền lành, **đeo kính cận gọng tròn đen trí thức trẻ trung**, nụ cười ấm áp tinh nghịch, tóc đen cắt gọn gàng.
- **Vai trò:** Hay bày trò chọc ghẹo con gái rượu làm bé Hân dỗi hờn má bánh bao.
- **Prompt Token:**
```text
authentic unretouched 8k DSLR portrait, @_Char_Ba_Long, a handsome 27-year-old Vietnamese father, wearing stylish modern round black-rimmed glasses, gentle warm playful smile, short neat black hair, natural skin texture with visible micro-pores, dressed in a comfortable casual knit sweater, loving fun family dad, realistic indoor ambient light --style raw
```
