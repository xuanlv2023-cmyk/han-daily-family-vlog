#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Dự án: Ba Cắn Mất Miếng Chuối To (Skill: han-daily-family-vlog)
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn Tool Batch:
- 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
- 01_PROMPTS_ANH: Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn).
- 02_PROMPTS_VIDEO: Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn).
- 03_PROMPTS_VOICE: Lời thoại sạch 100%, không kèm tên cảnh, không nhãn người nói, không kèm chú thích SFX (3 cảnh = đúng 3 đoạn văn).
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
                     "Dự án: Ba Cắn Mất Miếng Chuối To • Hệ thống 4 Nhân Vật Gia Đình • Bối cảnh: @_Location_Cozy_Living_Room",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh Turnaround của các nhân vật tham gia làm Character Reference cho Tool AI.")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet Bé Hân (Chị cả 3 tuổi) @_Brand_Baby_Lead")
    p_c1 = doc.add_paragraph()
    p_c1.add_run("• Tên: ").bold = True
    p_c1.add_run("Bé Hân @_Brand_Baby_Lead (3 tuổi, má bánh bao phúng phính, mắt to tròn, tóc búi củ tỏi kẹp hoa cúc ngọc trai).\n")
    p_c1.add_run("• Trang phục tham chiếu: ").bold = True
    p_c1.add_run("Váy yếm vintage màu be kem, áo thun trắng, túi chéo hạt ngọc trai mini.")
    p_c1.paragraph_format.space_after = Pt(4)

    prompt_han = "A professional four-view character turnaround model sheet of @_Brand_Baby_Lead, an adorable 3-year-old Vietnamese toddler girl, displaying front view, three-quarter view, profile side view, and funny dramatic sulking pout expression close-up. Extremely cute round face with chubby rosy dumpling cheeks, large expressive sparkling dark brown eyes, button nose, tiny pouty lips, hair styled in a neat high topknot bun with a dainty white daisy pearl hairpin, natural soft baby skin texture, living human realism. Wearing a vintage beige pinafore dress over a soft white tee, tiny pearl beaded crossbody purse, cream socks, brown t-strap shoes. Stationary mounted camera, eye-level toddler shot, natural soft daylight, neutral studio background, raw 8k DSLR photography, zero AI plastic doll skin, zero 3D anime CGI look --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_han)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Character Sheet Ba Hoàng Long (27 tuổi) @_Brand_Father_Lead")
    p_c2 = doc.add_paragraph()
    p_c2.add_run("• Tên: ").bold = True
    p_c2.add_run("Ba Hoàng Long @_Brand_Father_Lead (27 tuổi, kính ngố tròn gọng đen, áo len xanh rêu olive, quần kaki be, tính hài hước).")
    p_c2.paragraph_format.space_after = Pt(4)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Master Character Sheet Mẹ Uyên Hân & Bé Bo (8 tháng)")
    p_c3 = doc.add_paragraph()
    p_c3.add_run("• Mẹ Uyên Hân: ").bold = True
    p_c3.add_run("25 tuổi, áo len đỏ trễ vai burgundy, tóc đen dài gợn sóng.\n")
    p_c3.add_run("• Em trai Bé Bo: ").bold = True
    p_c3.add_run("8 tháng tuổi, má núng nính, mặc bodysuit gấu teddy bear màu nâu nhạt.")
    p_c3.paragraph_format.space_after = Pt(4)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Master Location Sheet @_Location_Cozy_Living_Room")
    prompt_loc = "A cinematic establishing photo of @_Location_Cozy_Living_Room, a bright and warm modern Scandinavian apartment living room, light beige leather sofa, oak wood coffee table, fluffy woven area rug, indoor potted plants, sheer white curtains filtering soft natural morning sunlight, clean aesthetic family home, pristine sensor image, zero UI graphics, no watermark --ar 9:16 --style raw"
    add_clean_paragraph(doc, prompt_loc)

    doc.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

def export_file_01(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)",
                     "Dự án: Ba Cắn Mất Miếng Chuối To • Chuẩn 9:16 Real Human Family Photography",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    prompts = [
        "authentic unretouched raw 8k DSLR family photograph, @_Brand_Baby_Lead (cute 3-year-old Vietnamese toddler girl with chubby dumpling cheeks and daisy hairpin) happily holding a ripe yellow banana with both tiny chubby hands offering it to her father @_Brand_Father_Lead (27-year-old handsome Vietnamese dad wearing round black glasses), sitting in Scandinavian living room @_Location_Cozy_Living_Room near beige sofa, soft natural morning window light, realistic child and adult skin texture with visible micro-pores, natural floor contact shadows, shot on Sony A7 IV with 35mm f/1.8 lens, pristine clean sensor image, zero AI plastic doll skin, zero 3D CGI look --ar 9:16 --v 6.1 --style raw",
        "candid domestic family portrait, raw 8k DSLR photograph, @_Brand_Baby_Lead, cute 3-year-old Vietnamese toddler girl, dramatic hilarious sulking pout expression, cheeks puffed up comically like steamed buns, large round teary eyes glaring playfully sideways, holding shortened half-eaten banana in tiny hands, sitting on fluffy living room rug in @_Location_Cozy_Living_Room, father @_Brand_Father_Lead blurred in background laughing mischievous, natural indoor lighting, 50mm f/1.4 lens, ultra-sharp focus on toddler facial pores, genuine baby skin, zero airbrushed skin, zero 3D anime --ar 9:16 --v 6.1 --style raw",
        "heartwarming candid family snapshot, raw 8k DSLR camera capture, complete Vietnamese family of 4 in sunlit Scandinavian living room @_Location_Cozy_Living_Room: mother @_Brand_Mother_Lead in burgundy knit sweater holding chubby 8-month-old baby son @_Brand_Toddler_Boy in brown bear romper, crouching to comfort pouting 3-year-old daughter @_Brand_Baby_Lead who hugs mother's waist, while father @_Brand_Father_Lead with round glasses smiles apologetically beside sofa, warm golden daylight, natural skin textures for all members, shot on Sony A7 IV, zero 3D CGI rendering, zero plastic wax smoothing --ar 9:16 --v 6.1 --style raw"
    ]
    for p in prompts:
        add_clean_paragraph(doc, p)
    doc.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

def export_file_02(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO HÀNG LOẠT (BATCH MEGA PROMPTS)",
                     "Dự án: Ba Cắn Mất Miếng Chuối To • Chuẩn Tagged Blocks Bắt Buộc 1:1",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn sạch).")

    video_prompts = [
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic candid family snapshot, raw 8k DSLR realism, unretouched real human photography. [CAMERA LOCK & FRAMING]: Locked-off eye-level medium shot framing father and toddler daughter, stationary tripod-mounted camera. Continuous unbroken single-take video throughout all 10.0 seconds with zero camera movement, no zoom, no pan, strictly no scene transition. [FAMILY CHARACTER ANCHORS]: @_Brand_Baby_Lead (3-year-old daughter in beige pinafore dress and daisy hairpin, natural chubby rosy cheeks and baby skin pores) and @_Brand_Father_Lead (27-year-old father with round glasses in olive sweater, natural skin texture). [ENVIRONMENT & LIGHTING]: Sitting near the beige sofa in @_Location_Cozy_Living_Room, soft morning daylight illuminating their cheerful faces, natural floor contact shadows, shot on Sony A7 IV. [INITIAL STATE]: Inherits Keyframe K1: Bé Hân happily holds a fresh yellow banana with both tiny hands, offering it toward her smiling father. [COMEDY SKIT & REACTION TIMELINE]: - [0.0s - 3.0s]: Toddler extends banana forward with an adorable innocent smile, nodding her head cheerfully while delivering her line with synchronized baby lip-sync. - [3.0s - 7.0s]: Father leans in playfully and takes a comically large bite from the banana, chewing with an exaggerated mischievous grin, eyes twinkling behind glasses. - [7.0s - 10.0s]: Toddler watches the bite happen, her smile slowly freezing in naive shock as she looks down at the remaining half banana, settling into Keyframe K2. [AUDIO DIALOGUE & BABY LIP-SYNC]: Exact synchronized spoken Vietnamese dialogue: Father (10 từ/10s): \"Cho ba xin một miếng nhỏ xíu nha!\", Bé Hân (2 từ): \"Dạ ba!\", exaggerated cartoon bite crunch SFX (\"Rộp/Ngoạm\"), cheerful acoustic ukulele bed. [FINAL STATE]: Banana missing a large bite, toddler holding the shortened banana, eyes beginning to widen, matching Keyframe K2. [NEGATIVE CONSTRAINTS]: Strictly NO distorted banana shape, NO extra fingers, NO camera panning, NO AI plastic skin, NO 3D Pixar animation look, NO porcelain shine.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, candid emotional toddler portrait, raw DSLR photography, unretouched real human photography. [CAMERA LOCK & FRAMING]: Locked-off close-up portrait shot focusing directly on Bé Hân, stationary camera with subtle organic breathing motion. Continuous unbroken single-take video throughout all 10.0 seconds. [FAMILY CHARACTER ANCHORS]: @_Brand_Baby_Lead in sharp focus with chubby rosy dumpling cheeks and visible delicate pores; @_Brand_Father_Lead visible slightly blurred in background chuckling warmly. [ENVIRONMENT & LIGHTING]: Cozy living room background @_Location_Cozy_Living_Room, warm soft bokeh, crystal-sharp focus on toddler facial pores and misty eyes, natural indoor lighting. [INITIAL STATE]: Seamlessly matching Keyframe K2: toddler holding the half-eaten banana, staring down at it. [COMEDY SKIT & REACTION TIMELINE]: - [0.0s - 3.0s]: Stares at the banana stump in comical disbelief, blinking large round eyes twice in slow funny surprise as she realizes how much is gone. - [3.0s - 7.0s]: Chubby cheeks puff up like steamed buns, her lower lip sticks out dramatically into an iconic hilarious pout, eyes turning teary and glaring sideways at her father, stomping tiny foot lightly. - [7.0s - 10.0s]: Delivers her cute sulking line with synchronized pouting baby lip-sync, crossing tiny arms in indignation, settling into Keyframe K3. [AUDIO DIALOGUE & BABY LIP-SYNC]: Exact synchronized spoken Vietnamese baby dialogue: Bé Hân (Giọng ngọng mếu má 14 từ/10s): \"Ba... ba ăn mất miếng to của con rồi! Hổng chơi dí ba nữa!\", Father (6 từ): \"Ba lỡ miệng mà công chúa ơi!\", funny cartoon \"Boing\" spring sound and record scratch SFX, warm background laughter. [FINAL STATE]: Dramatic sulking pout face with puffed cheeks, glaring comically sideways, matching Keyframe K3. [NEGATIVE CONSTRAINTS]: Strictly NO face warping, NO artificial 3D anime gloss, NO distorted hands, NO text watermarks, NO adult teeth on toddler, NO waxy baby skin.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, heartwarming candid family snapshot, raw 8k DSLR realism, unretouched real human photography. [CAMERA LOCK & FRAMING]: Wide eye-level family shot capturing all 4 members in the living room, stable camera glide. Continuous unbroken single-take video throughout all 10.0 seconds. [FAMILY CHARACTER ANCHORS]: Mother: @_Brand_Mother_Lead carrying baby son @_Brand_Toddler_Boy in bear romper; Daughter: @_Brand_Baby_Lead running to hug mother's waist; Father: @_Brand_Father_Lead smiling playfully beside the sofa. All members display natural real human skin textures. [ENVIRONMENT & LIGHTING]: Sunlit Scandinavian living room @_Location_Cozy_Living_Room, warm golden hour ambient glow, natural floor contact shadows, shot on Sony A7 IV. [INITIAL STATE]: Inherits Keyframe K3: Bé Hân pouting, turning toward mother who enters from hallway. [COMEDY SKIT & REACTION TIMELINE]: - [0.0s - 3.0s]: Mother enters carrying chubby smiling baby brother Bo, crouching gently to comfort Bé Hân, smiling tenderly. - [3.0s - 7.0s]: Bé Hân rushes into mother's arms, burying her cheek into mother's sweater with animated gestures, while baby Bo claps chubby hands with joyful baby babble. - [7.0s - 10.0s]: Mother scolds father playfully, father rubs back of neck laughing apologetically, entire family bursts into radiant warm laughter, completing the video. [AUDIO DIALOGUE & BABY LIP-SYNC]: Exact synchronized spoken Vietnamese dialogue: Mother (14 từ/10s): \"Thôi mẹ thương, mẹ đền cho Hân quả khác nha! Ba xấu tính ghê á!\", Bé Hân (6 từ): \"Dạ... mẹ bắt đền ba đi!\", baby giggle sfx, uplifting acoustic piano crescendo, warm family laughter. [FINAL STATE]: Complete 4-member family laughing together in a loving embrace, holding posture to close the video loop. [NEGATIVE CONSTRAINTS]: Strictly NO missing limbs, NO warped baby heads, NO camera jitter, NO CGI look, NO plastic doll face, NO waxy shine."
    ]
    for vp in video_prompts:
        add_clean_paragraph(doc, vp)
    doc.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

def export_file_03(output_dir):
    doc = Document()
    add_styled_title(doc, "KỊCH BẢN LỜI THOẠI HÀNG LOẠT (BATCH TTS SCRIPTS)",
                     "Dự án: Ba Cắn Mất Miếng Chuối To • Giọng Ngọng Bé Hân & Ba Mẹ",
                     "Định dạng Tool Batch: Lời thoại tiếng Việt sạch 100%, không nhãn người nói, không chú thích SFX. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    dialogue_lines = [
        "Cho ba xin một miếng nhỏ xíu nha! Dạ ba!",
        "Ba ăn mất miếng to của con gòi! Hổng chơi dí ba nữa! Ba lỡ miệng mừ công chúa ơi!",
        "Thôi mẹ thương, mẹ đền cho Hân quả khác nha! Ba xấu tính ghê á! Dạ, mẹ bắt đền ba đi!"
    ]
    for dl in dialogue_lines:
        add_clean_paragraph(doc, dl, font_name='Segoe UI', font_size=11.5)
    doc.save(os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx"))

def export_file_04(output_dir):
    doc = Document()
    add_styled_title(doc, "GÓI TỐI ƯU SEO & ĐĂNG TẢI VIRAL ĐA KÊNH",
                     "Dự án: Ba Cắn Mất Miếng Chuối To • Chuẩn Đăng Tải Shorts / TikTok / Reels")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Prompt Tạo Ảnh Bìa Thumbnail (9:16)")
    thumb_prompt = "A hyper-realistic cinematic family comedy thumbnail photo, 9:16 vertical framing. Close-up on @_Brand_Baby_Lead, super cute 3-year-old Vietnamese toddler girl with chubby rosy dumpling cheeks, holding a comically half-eaten yellow banana, lower lip pushed out in an iconic dramatic sulk, big teary eyes glaring playfully sideways at her father, pearl daisy hairpin in high topknot bun. In the background, her handsome father wearing round glasses laughs heartily with guilty expression. Inside a bright cozy Scandinavian living room, warm morning lighting, clean negative space at the top for bold catchy text, masterpiece, 8k resolution, raw photography, zero AI plastic look, zero 3D CGI rendering --ar 9:16 --v 6.1 --style raw"
    add_clean_paragraph(doc, thumb_prompt)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Chữ Dán Thumbnail (Overlay Text)")
    add_clean_paragraph(doc, "BA ĂN HẾT CỦA CON! 😭🍌\nMÁ BÁNH BAO BỐC HỎA! 😡✨\nĐỪNG TRÊU BÉ HÂN NỮA! 😂", font_name='Segoe UI', font_size=11)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Tiêu Đề Đa Nền Tảng (A/B Testing Headlines)")
    add_clean_paragraph(doc, "A: Ba cắn mất miếng chuối to đùng và cái kết Bé Hân bĩu môi dỗi cả ngày 😂🍌 #Shorts\nB: Ai bảo ba cắn to quá làm chi, nhìn cái má bánh bao dỗi kìa cưng xỉu! 🥺❤️ #TikTokBaby\nC: Khi ba xin một miếng nhỏ xíu của con gái rượu và cái kết... 🤣 #Reels", font_name='Segoe UI', font_size=11)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Caption & Hashtag 3 Tầng")
    add_clean_paragraph(doc, "Bảo cho ba xin một miếng nhỏ xíu thôi mà ba ngoạm một cái mất nửa quả chuối của người ta! Nhìn cái mặt bĩu môi hờn dỗi má bánh bao cưng không chịu nổi luôn á cả nhà ơi 😂 May mà có mẹ với em Bo ra giải cứu kịp thời! Cả nhà thả tim dỗ dành bé Hân nha! 💖✨\n\n#Shorts #TikTokBaby #ReelsViral #FamilyHumor #HaiHuocGiaDinh #BeHanDaily #EmBeHaiHuoc #MaBanhBao #EmBeDoiHon #TieuPhamGiaDinh #MeVaBe #ChuyenNhaHan #HanDaily #HanMitDaily #GiaDinhUyenHan", font_name='Segoe UI', font_size=10.5)

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
