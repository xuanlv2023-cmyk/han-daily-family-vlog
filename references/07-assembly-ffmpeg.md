# LỆNH FFMPEG GHÉP VIDEO TIỂU PHẨM GIA ĐÌNH (ASSEMBLY FFPEG)
## Skill: `han-daily-family-vlog`

Tổng hợp các lệnh FFmpeg để nối các phân đoạn tiểu phẩm, đồng bộ audio thoại và xuất video dọc YouTube Shorts chuẩn 1080x1920 (60fps).

---

### 1. FILE DANH SÁCH PHÂN ĐOẠN (`concat_list.txt`)
```text
file 'clip_01_situation.mp4'
file 'clip_02_pouty_reaction.mp4'
file 'clip_03_laugh_ending.mp4'
```

---

### 2. LỆNH GHÉP NỐI & CHUẨN HÓA DỌC 9:16 (1080x1920, 60FPS)
```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,fps=60" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p video_assembled.mp4
```

---

### 3. LỆNH GHÉP AUDIO VOICE & BGM
Ghép video hình ảnh với file âm thanh tổng hợp `audio_final.mp3` (chứa thoại + tiếng cười + SFX + BGM):
```bash
ffmpeg -i video_assembled.mp4 -i audio_final.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest final_family_short.mp4
```
