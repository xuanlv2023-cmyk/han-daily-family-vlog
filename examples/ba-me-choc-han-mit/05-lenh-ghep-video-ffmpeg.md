# LỆNH FFMPEG GHÉP VIDEO TỰ ĐỘNG
## Dự án: Ba Cắn Mất Miếng Chuối To Và Cái Kết Bé Hân Dỗi Cả Ngày

Tạo file `concat_list.txt`:
```text
file 'clip_01_bite.mp4'
file 'clip_02_pout.mp4'
file 'clip_03_comfort.mp4'
```

### Lệnh 1: Nối 3 clip thành video dọc 9:16 (1080x1920) 60fps
```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,fps=60" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p video_assembled.mp4
```

### Lệnh 2: Lồng ghép âm thanh và xuất video hoàn thiện
```bash
ffmpeg -i video_assembled.mp4 -i audio_full.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest Han_Daily_Ep01_Final.mp4
```
