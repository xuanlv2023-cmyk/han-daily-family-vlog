# BÀI HỌC KINH NGHIỆM & SỬA LỖI AI TRẺ EM (LESSONS LEARNED)
## Skill: `han-daily-family-vlog`

Tạo hình ảnh và video AI về trẻ em đòi hỏi sự cẩn trọng đặc biệt về mặt giải phẫu và độ chân thực để tránh tạo ra cảm giác "uncanny valley" (kỳ quặc, đáng sợ).

---

### 1. LỖI MẶT TRẺ EM BỊ GIÀ HOẶC BIẾN DẠNG RĂNG (TEETH & AGING)
- **Hiện tượng:** AI vô tình tạo cho em bé 3 tuổi bộ răng người lớn đầy đủ hoặc đường nét khuôn mặt quá góc cạnh như người lớn bị thu nhỏ.
- **Giải pháp:**
  - Luôn mô tả rõ: `soft chubby baby cheeks, round soft baby jawline, tiny white baby teeth, innocent childish eyes`.
  - Không dùng các từ khóa miêu tả người lớn như `chiseled, sharp jawline, contoured`.

---

### 2. LỖI TAY CHÂN EM BÉ BỊ MẤT NGÓN HOẶC DÍNH KHỚP
- **Hiện tượng:** Bàn tay em bé cầm thìa, cầm quả chuối hoặc cầm điện thoại bị dính 6 ngón hoặc biến dạng ngón tay.
- **Giải pháp:**
  - Trong prompt hình ảnh ban đầu: `chubby little toddler hands, 5 distinct cute baby fingers holding object naturally`.
  - Kiểm tra kỹ bàn tay trên ảnh Keyframe trước khi đưa vào tạo video.

---

### 3. LỖI CẢM GIÁC 3D/HOẠT HÌNH
- **Hiện tượng:** Em bé trông giống nhân vật hoạt hình Pixar hoặc búp bê sứ.
- **Giải pháp:**
  - Sử dụng các từ khóa nhiếp ảnh máy cơ: `authentic raw unedited DSLR photograph, natural baby skin texture with microscopic pores, natural daylight, candid domestic snapshot, zero CGI, zero 3D illustration`.
