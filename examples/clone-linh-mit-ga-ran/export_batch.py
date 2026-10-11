#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại (Clone Video 1 Linh Mít Daily)
Skill: han-daily-family-vlog
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn Tool Batch:
- 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
- 01_PROMPTS_ANH: Mỗi cảnh là đúng 1 đoạn văn liên tục (1 cảnh = 1 đoạn văn sạch).
- 02_PROMPTS_VIDEO: Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (1 cảnh = 1 đoạn văn sạch).
- 03_PROMPTS_VOICE: Lời thoại sạch 100% Giọng Miền Nam, không kèm tên cảnh, không nhãn người nói, không kèm chú thích SFX (1 cảnh = 1 đoạn văn sạch).
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_styled_title(doc, title_text, subtitle_text, note_text=None):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_title = p_title.add_run(title_text)
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(234, 88, 12) # Orange
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(100, 116, 139)

    if note_text:
        p_sub.paragraph_format.space_after = Pt(4)
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_note = p_note.add_run(note_text)
        run_note.font.name = 'Segoe UI'
        run_note.font.size = Pt(9.5)
        run_note.font.color.rgb = RGBColor(194, 65, 12)
        p_note.paragraph_format.space_after = Pt(16)
    else:
        p_sub.paragraph_format.space_after = Pt(14)

def add_clean_paragraph(doc, text_content, font_name='Consolas', font_size=10, is_bold=False):
    """Thêm đúng 1 đoạn văn liên tục không nhãn thừa cho tool batch"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text_content)
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = is_bold
    run.font.color.rgb = RGBColor(30, 41, 59)

def export_file_00(output_dir):
    doc = Document()
    add_styled_title(doc, "HỒ SƠ THAM CHIẾU GỐC (MASTER REFERENCE ASSETS)",
                     "Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại (Clone Video 1 Linh Mít Daily)",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh Turnaround của các nhân vật tham gia làm Character Reference cho Tool AI.")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet Bé Hân (Chị cả 3 tuổi) @_Brand_Baby_Lead")
    p_c1 = doc.add_paragraph()
    p_c1.add_run("• Tên: ").bold = True
    p_c1.add_run("Bé Hân @_Brand_Baby_Lead (3 tuổi, má bánh bao phúng phính, mắt to tròn, tóc búi củ tỏi kẹp hoa cúc ngọc trai).\n")
    p_c1.add_run("• Trang phục tập này: ").bold = True
    p_c1.add_run("Váy dệt kim be cổ bèo, áo cardigan xanh navy viền trắng nơ ngực, vớ trắng ngắn.")
    p_c1.paragraph_format.space_after = Pt(4)

    prompt_han = "Character turnaround model sheet of an exceptionally cute 3-year-old Vietnamese toddler girl (Bé Hân), arranged side-by-side on a wide 16:9 seamless warm studio canvas. On the left and center: three full-body views showing her toddler proportions, chubby rosy dumpling cheeks, dressed in a charming cream knitted dress under navy blue cardigan with white collar, wearing tiny pearl daisy hairpin. These views include front, three-quarter, and profile standing views with strictly two clean chubby legs. On the right side: ultra-detailed close-up facial beauty portrait showing her iconic pouty face, puffed dumpling cheeks, and hilarious side-eye glare. 100% real human toddler photography, authentic unretouched raw 8k DSLR on Sony A7R V with 85mm f/1.4 lens, natural baby skin texture with microscopic pores, zero CGI, zero 3D render --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_han)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Character Sheet Ba Hoàng Long (27 tuổi) @_Brand_Father_Lead")
    p_c2 = doc.add_paragraph()
    p_c2.add_run("• Tên: ").bold = True
    p_c2.add_run("Ba Hoàng Long @_Brand_Father_Lead (27 tuổi, kính ngố tròn gọng đen, áo thun tay dài xanh rêu olive, tính hài hước).")
    p_c2.paragraph_format.space_after = Pt(4)

    prompt_ba = "Character turnaround model sheet of a handsome, stylish 27-year-old Vietnamese father (Ba Hoàng Long), arranged side-by-side on a wide 16:9 seamless modern studio backdrop. Three full-body views showing his tall frame dressed in olive-green long-sleeve tee, dark jeans, and clean sneakers. On the right side: close-up facial portrait showing his handsome gentle features, stylish modern round black-rimmed glasses, friendly laughing eyes, and playful charismatic smile. 100% real human, raw 8k DSLR photography on Sony A7R V, zero CGI, zero 3D render --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_ba)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Master Character Sheet Mẹ Uyên Hân (25 tuổi) @_Brand_Mother_Lead")
    p_c3 = doc.add_paragraph()
    p_c3.add_run("• Tên: ").bold = True
    p_c3.add_run("Mẹ Uyên Hân @_Brand_Mother_Lead (25 tuổi, thanh tú, tóc đen dài gợn sóng, áo dệt kim cổ bẻ polo xanh navy viền trắng).")
    p_c3.paragraph_format.space_after = Pt(4)

    prompt_me = "Character turnaround model sheet of an exceptionally beautiful 25-year-old Vietnamese mother (Uyên Hân), arranged side-by-side on a wide 16:9 seamless minimalist grey studio cyclorama. Three full-body views showing her slender figure wearing navy knit polo top with white collar. On the right side: close-up portrait showing delicate oval face, fair luminous skin, captivating dark eyes, and radiant warm smile. 100% real human raw 8k DSLR photography, natural skin pores, zero CGI, zero 3D render --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_me)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Master Location Sheet @_Location_Restaurant_Dining")
    prompt_loc = "A cinematic establishing photo of @_Location_Restaurant_Dining, a warm modern family restaurant dining room, white marble dining table with plate of crispy golden fried chicken nuggets, warm diffused ambient ceiling spotlights, natural indoor shadows, 9:16 vertical ratio, clean aesthetic sensor image, zero watermark --ar 9:16 --style raw"
    add_clean_paragraph(doc, prompt_loc)

    doc.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

def export_file_01(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)",
                     "Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại • Chuẩn 9:16 Real Human Photography",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (1 cảnh = đúng 1 đoạn văn sạch).")

    prompts = [
        "Authentic raw 8k DSLR candid photograph of a super cute 3-year-old Vietnamese girl (Bé Hân) with chubby rosy dumpling cheeks and high bun with pearl daisy hairpin, sitting in the center of a dining table between her stylish mother in navy knit top and handsome father wearing round black glasses in olive shirt. On the white marble table is a plate of crispy golden popcorn chicken. The toddler has an iconic hilarious dramatic sulking face with puffed dumpling cheeks, exaggerated lower lip pouting downward, and eyes giving an epic sideways side-eye glare at her smiling father, natural child skin pores, warm restaurant indoor lighting, 9:16 vertical ratio, shot on Sony A7R V with 85mm f/1.4 lens, ultra photorealistic, zero CGI, zero plastic skin --ar 9:16 --v 6.1 --style raw"
    ]
    for p in prompts:
        add_clean_paragraph(doc, p)
    doc.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

def export_file_02(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO HÀNG LOẠT (BATCH MEGA PROMPTS)",
                     "Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại • Chuẩn Tagged Blocks Bắt Buộc 1:1",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (1 cảnh = đúng 1 đoạn văn sạch).")

    video_prompts = [
        "[SPECIFICATION]: Exactly 15.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic candid family snapshot, unretouched real human photography, zero AI plastic look, zero CGI rendering. [CAMERA LOCK & FRAMING]: Locked-off eye-level medium shot framing all three family members around the dining table, stationary tripod-mounted camera. Continuous unbroken single-take video throughout all 15.0 seconds with zero camera movement, no zoom, no pan, strictly no scene cut. [FAMILY CHARACTER ANCHORS]: Center: @_Brand_Baby_Lead (super cute 3-year-old Vietnamese girl, chubby rosy dumpling cheeks, expressive dark brown eyes, high topknot bun with pearl daisy hairpin, authentic soft baby skin with natural micro-pores). Left: @_Brand_Mother_Lead (25-year-old stylish mother with long wavy dark hair, elegant fair complexion). Right: @_Brand_Father_Lead (27-year-old handsome father with round black-rimmed glasses, playful smile). [DYNAMIC OUTFITS]: @_Brand_Baby_Lead wearing cream knitted dress and navy blue cardigan with white collar, mother wearing navy knit polo top with white collar, father wearing olive-green long-sleeve tee, clean anatomically perfect 5-finger hands. [ENVIRONMENT & LIGHTING]: Positioned in @_Location_Restaurant_Dining, white marble dining table with plate of crispy golden popcorn chicken in foreground, cozy restaurant background with warm ambient ceiling spotlights, natural soft contact shadows. [INITIAL STATE]: Toddler sitting in highchair between parents, mouth wide open awaiting food, blowing gently with tiny puckered lips, eyes sparkling with innocent anticipation. [COMEDY SKIT & REACTION TIMELINE]: - [0.0s - 3.5s]: Father holds stainless steel fork with a piece of crispy chicken extending toward toddler's mouth, toddler opens mouth wide blowing innocently with puffed cheeks. - [3.5s - 6.5s]: Sudden comedic twist, father smoothly pivots the fork left directly into mother's mouth, mother bites the chicken happily and chews with joyful satisfaction. - [6.5s - 11.5s]: Iconic comedic reaction sequence, toddler freezes completely with mouth still wide open in disbelief for 2 seconds, mouth slowly closes, dumpling cheeks puff up dramatically like steamed buns, exaggerated lower lip pouts downward in immense grievance, eyes shift sideways into an epic hilarious side-eye glare at father without moving her head. - [11.5s - 15.0s]: Toddler turns her head to mother with teary pouty baby scolding gestures, while father and mother burst into uncontrollable genuine contagious laughter, father reaching to gently pat toddler's head. [AUDIO DIALOGUE & BABY LIP-SYNC]: Exact synchronized spoken Southern Vietnamese dialogue: Father (0-3s): \"Nguội rồi nè, há miệng to ba đút cho công chúa nhen!\", Mother (4-6s): \"Ưm ngon quá ba ơi!\", Toddler (11-15s ngọng líu dỗi hờn): \"Mẹ kì zậy... con thổi nguội gòi mà mẹ ăn hết trơn!\", Father and Mother: (bursting into authentic uncontrollable laughter). [AUDIO BGM & COMEDY SFX]: Cartoon crow caw sfx during freeze, cartoon spring boing sfx when cheeks puff out, warm authentic parents laughter, soft cheerful acoustic ukulele bed at -22dB. [FINAL STATE]: Toddler maintaining adorable dramatic pout, parents laughing warmly together. [NEGATIVE CONSTRAINTS]: Strictly NO extra fingers, NO fused hands, NO distorted baby limbs, NO waxy plastic doll face, NO 3D Pixar anime look, NO text overlays, NO watermarks."
    ]
    for vp in video_prompts:
        add_clean_paragraph(doc, vp)
    doc.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

def export_file_03(output_dir):
    doc = Document()
    add_styled_title(doc, "KỊCH BẢN LỜI THOẠI HÀNG LOẠT (BATCH TTS SCRIPTS)",
                     "Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại • 100% Giọng Miền Nam",
                     "Định dạng Tool Batch: Lời thoại tiếng Việt sạch 100%, không nhãn người nói, không chú thích SFX. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (1 cảnh = đúng 1 đoạn văn sạch).")

    dialogue_lines = [
        "Nguội rồi nè, há miệng to ba đút cho công chúa nhen! Ưm ngon quá ba ơi! Mẹ kì zậy... con thổi nguội gòi mà mẹ ăn hết trơn!"
    ]
    for dl in dialogue_lines:
        add_clean_paragraph(doc, dl, font_name='Segoe UI', font_size=11.5)
    doc.save(os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx"))

def export_file_04(output_dir):
    doc = Document()
    add_styled_title(doc, "GÓI TỐI ƯU SEO & ĐĂNG TẢI VIRAL ĐA KÊNH",
                     "Dự án: Cú Lừa Gà Rán & Pha Liếc Xéo Huyền Thoại • Chuẩn Đăng Tải Shorts / TikTok / Reels")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Prompt Tạo Ảnh Bìa Thumbnail (9:16)")
    thumb_prompt = "A hyper-realistic candid family comedy thumbnail photo, 9:16 vertical framing. Close-up on @_Brand_Baby_Lead, super cute 3-year-old Vietnamese toddler girl with chubby rosy dumpling cheeks, sitting at a restaurant dining table, lower lip pushed out in an iconic hilarious dramatic sulk, big dark eyes giving an epic side-eye glare at her smiling father in the background, pearl daisy hairpin in high topknot bun. On the table is a plate of crispy fried chicken. Warm golden restaurant lighting, clean negative space at the top for bold catchy text, masterpiece, 8k resolution, raw photography, zero AI plastic look, zero 3D CGI rendering --ar 9:16 --v 6.1 --style raw"
    add_clean_paragraph(doc, thumb_prompt)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Chữ Dán Thumbnail (Overlay Text)")
    add_clean_paragraph(doc, "CON THỔI NGUỘI MẸ ĂN MẤT! 😭🍗\nCÚ LIẾC XÉO BẤT LỰC! 😡✨\nBA ĐỪNG LỪA CON NỮA MÀ! 😂", font_name='Segoe UI', font_size=11)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Tiêu Đề Đa Nền Tảng (A/B Testing Headlines)")
    add_clean_paragraph(doc, "A: Ba đút gà rán cho mẹ và pha liếc xéo dỗi hờn huyền thoại của Bé Hân 😂🍗 #Shorts\nB: Người ta thổi nguội nãy giờ mà mẹ cắn mất tiêu, nhìn cái mặt dỗi cưng xỉu! 🥺❤️ #TikTokBaby\nC: Khi ba giả vờ đút đồ ăn cho con gái rượu và cái kết bất lực... 🤣 #Reels", font_name='Segoe UI', font_size=11)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Caption & Hashtag 3 Tầng")
    add_clean_paragraph(doc, "Con gái cưng ngồi thổi phù phù nãy giờ cho nguội đặng ăn, ai ngờ ba bẻ lái đút cái rụp vô miệng mẹ! Nhìn cái tướng đứng hình rồi liếc xéo ba tóe lửa kìa trời ơi, má bánh bao phồng căng thấy ghét ghê hôn 😂 Cả nhà thả tim dỗ dành bé Hân đi mua đĩa gà rán khác nha! 💖🍗\n\n#Shorts #TikTokBaby #ReelsViral #FamilyHumor #HaiHuocGiaDinh #BeHanDaily #EmBeHaiHuoc #MaBanhBao #LinhMitDaily #EmBeDoiHon #TieuPhamGiaDinh #MeVaBe #ChuyenNhaHan #HanDaily #CuLuaGaRan", font_name='Segoe UI', font_size=10.5)

    doc.save(os.path.join(output_dir, "04_METADATA_SEO.docx"))

def export_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "export_batch")
    os.makedirs(output_dir, exist_ok=True)
    export_file_00(output_dir)
    export_file_01(output_dir)
    export_file_02(output_dir)
    export_file_03(output_dir)
    export_file_04(output_dir)
    print(f"[OK] Đã xuất thành công trọn bộ 5 file .docx chuẩn Tool Batch tại: {output_dir}")

if __name__ == '__main__':
    export_all()
