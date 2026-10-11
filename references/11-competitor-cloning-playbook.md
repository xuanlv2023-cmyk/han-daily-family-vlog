# CẨM NANG BÓC TÁCH & CLONE VIDEO ĐỐI THỦ (COMPETITOR CLONING PLAYBOOK)
## Skill: `han-daily-family-vlog` (Chuyên sâu nhân bản kênh Linh Mít Daily & Shorts Gia Đình)

Playbook này hướng dẫn quy trình bóc tách (Reverse-Engineering) và tái tạo (Clone) 1:1 bất kỳ video ngắn nào từ kênh đối thủ (đặc biệt là thư mục tham chiếu `Linh mít Daily`), chuyển đổi trọn vẹn sang hệ thống nhân vật gia đình Bé Hân với chất lượng tương đương hoặc vượt trội, đạt chuẩn 100% Giọng Miền Nam / Sài Gòn và cấu trúc xuất tool hàng loạt.

---

### BƯỚC 1: KHÁM NGHIỆM VIDEO ĐỐI THỦ (DECONSTRUCTION PIPELINE)

Khi nhận đầu vào là một video đối thủ (ví dụ `1_1962537371797874.mp4`, `12_1690724045952077.mp4`...):

1. **Đo đạc thông số kỹ thuật gốc:**
   - **Thời lượng (Duration):** Hầu hết video đối thủ dao động từ 10.0s đến 18.0s (lý tưởng: 12.0s - 15.0s).
   - **Tỷ lệ & Cỡ khung:** 9:16 dọc (720x1280 hoặc 1080x1920), 24-30 FPS.
   - **Cấu trúc đúp quay (Take Structure):**
     - Đa số (70%): **1 Đúp Quay Đơn Duy Nhất (Single Continuous Master Shot)** giữ nguyên góc máy từ đầu đến cuối để cảm xúc phản ứng không bị đứt đoạn.
     - Thiểu số (30%): **2 Cảnh (Two-Shot Match Cut)**: Cảnh 1 (Toàn cảnh thiết lập tình huống 0-6s) $\to$ Cảnh 2 (Cận cảnh đặc tả phản ứng nổ tung của bé 6-15s).

2. **Lập Bảng Beat Sheet Từng Giây (Second-by-Second Breakdown):**
   - Phân rã video thành 4 nhịp kịch bản:
     - `0s - 3s (Setup - Thả thính):` Ai làm gì? Đạo cụ là gì? (Ví dụ: Ba cầm nĩa gà rán đưa tới).
     - `3s - 7s (Twist / Prank - Cú lừa):` Hành động bất ngờ đảo chiều (Ví dụ: Cây nĩa quay ngoắt đút cho mẹ).
     - `7s - 11s (Reaction Climax - Đứng hình & Dỗi hờn):` Biểu cảm vi mô của em bé (Ví dụ: Há miệng ngơ ngác $\to$ má phồng $\to$ liếc xéo tóe lửa).
     - `11s - 15s (Resolution & Laughter - Mách tội & Tiếng cười):` Bé quay sang mách mẹ hoặc dậm chân, ba mẹ cười nắc nẻ.

3. **Bóc tách Tương tác Thể chất (Physical Micro-Interactions):**
   - Xác định rõ vị trí ngồi/đứng, chuyển động của bàn tay, tiếp xúc cơ thể (gạt tay, ôm cổ, úp tường, cắn đồ ăn).

---

### BƯỚC 2: BẢN ĐỒ ÁNH XẠ NHÂN VẬT & BỐI CẢNH (MAPPING MATRIX)

Ánh xạ toàn bộ nhân vật và bối cảnh từ video đối thủ sang Hệ Thống Token Độc Quyền của Bé Hân:

| Nhân Vật Video Đối Thủ | Token Ánh Xạ Chuẩn Bé Hân | Đặc Trưng Diện Mạo & Vai Diễn |
| :--- | :--- | :--- |
| **Bé Gái Đối Thủ (Linh Mít)** | `@_Char_Be_Han` (`@_Brand_Baby_Lead`) | Bé Hân 3 tuổi, búi tóc củ tỏi kẹp hoa cúc ngọc trai, má bánh bao ửng hồng, đôi mắt to tròn, môi trề dỗi hờn, mặc váy yếm xinh xắn. |
| **Em Trai Nhỏ (nếu có)** | `@_Char_Be_Bo` (`@_Brand_Toddler_Boy`) | Em Bo 8 tháng, má núng nính, đầu tròn xoe, 2 răng sữa, bodysuit gấu teddy nâu. |
| **Mẹ Đối Thủ** | `@_Char_Me_Uyen` (`@_Brand_Mother_Lead`) | Mẹ Uyên Hân 25 tuổi, thanh tú, tóc đen uốn sóng, áo dệt kim trễ vai nữ tính, nụ cười rạng rỡ. |
| **Ba Đối Thủ** | `@_Char_Ba_Long` (`@_Brand_Father_Lead`) | Ba Hoàng Long 27 tuổi, đeo kính cận gọng tròn đen trí thức, áo polo/len mỏng màu trung tính, thích trêu chọc con gái. |
| **Xe hơi trong video** | `@_Location_Car_Interior` | Khoang xe SUV sang trọng ghế da đỏ/đen, góc máy quay ngang nhìn qua kính lái hoặc bệ giữa. |
| **Góc tường dỗi** | `@_Location_Living_Room_Wall` | Bức tường phòng khách chung cư tông màu ấm, sàn gỗ sáng, tranh treo nghệ thuật. |
| **Bàn ăn quán gà rán** | `@_Location_Restaurant_Dining` | Bàn ăn mặt đá marble trắng, đĩa gà rán giòn rụm, ánh sáng ấm cúng. |
| **Xe máy SH** | `@_Location_Street_Scooter` | Xe máy SH Mode màu be/trắng trên đường phố hiện đại, nón bảo hiểm POC thời trang. |

---

### BƯỚC 3: BẢN ĐỊA HÓA THOẠI 100% GIỌNG MIỀN NAM / SÀI GÒN

Chuyển đổi hoàn toàn lời thoại hoặc tiếng ú ớ từ video đối thủ sang văn phong Nam Bộ chuẩn, lém lỉnh, ngọng líu:

- **Nguyên tắc chuyển ngữ thoại của Bé Hân:**
  - Thay "không/không chơi" $\to$ *"hổng/hổng thèm chơi dí ba nữa nè!"*
  - Thay "sao vậy/kìa" $\to$ *"kì zậy nè!", "sao hổng ai dỗ tui hết dợ!?"*
  - Thay "hết rồi" $\to$ *"ăn hết trơn gòi!"*
  - Ngữ điệu hờn dỗi, lí sự dồn dập, kéo dài âm đuôi ngọng nghịu đáng yêu.
- **Tiếng cười ba mẹ ở hậu trường:**
  - Bắt buộc chèn thẻ `[SFX_CONTAGIOUS_LAUGHTER]` ghi rõ tiếng cười thật của ba mẹ (ba cười sặc sụa, mẹ cười nắc nẻ) làm nền cho thoại.

---

### BƯỚC 4: QUY TRÌNH TẠO PROMPT 1 ĐOẠN VĂN LIÊN TỤC (BATCH PROMPTS PIPELINE)

Để đảm bảo copy chạy tool hàng loạt không bị lỗi:
1. **Prompt Ảnh Keyframe:** Viết thành **1 đoạn văn liên tục**, mô tả rõ góc chụp, nhân vật, biểu cảm vi mô theo đúng khung hình đối thủ.
2. **Mega Prompt Video:** Viết thành **1 đoạn văn liên tục** chứa đầy đủ các thẻ Tagged Blocks `[SPECIFICATION] [CAMERA LOCK & FRAMING] [FAMILY CHARACTER ANCHORS] [DYNAMIC OUTFITS] [ENVIRONMENT & LIGHTING] [INITIAL STATE] [COMEDY SKIT & REACTION TIMELINE] [AUDIO DIALOGUE & BABY LIP-SYNC] [AUDIO BGM & COMEDY SFX] [FINAL STATE] [NEGATIVE CONSTRAINTS]`.
3. **Thoại Voice TTS:** Viết thành **1 đoạn văn liên tục** cho mỗi phân cảnh.

---

### BƯỚC 5: XUẤT 5 FILE DOCX CHUẨN HOÀN TOÀN KHÔNG TABLE
Sử dụng script `export_batch.py` để xuất trọn bộ 5 file docx chuẩn chỉ:
1. `00_HO_SO_THAM_CHIEU_GOC.docx`
2. `01_PROMPTS_ANH_HANG_LOAT.docx`
3. `02_PROMPTS_VIDEO_HANG_LOAT.docx`
4. `03_PROMPTS_VOICE_HANG_LOAT.docx`
5. `04_METADATA_SEO.docx`
