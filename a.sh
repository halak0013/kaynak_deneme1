for f in *.mp3; do ffmpeg -loop 1 -i a.jpg -i ${f%.} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -shortest -movflags +faststart "${f%.mp3}.mp4"; done



for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.} -shortest -acodec copy -vcodec mjpeg  "vid/${f%.mp3}.mp4"; done






for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.} -shortest -acodec copy -vcodec mjpeg  "vid/${f%.mp3}.mp4"; done
for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.} -shortest -acodec copy -vcodec mjpeg  "vid/${f%.mp3}.mp4"; done
for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.} -shortest -acodec copy -vcodec mjpeg  "vid/${f%.mp3}.mp4"; done


for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.} -shortest -threads 3 -acodec copy -vcodec libx264 "vid/${f%.mp3}.mp4"; done

for f in *.mp3; do ffmpeg -loop 1 -i b.jpg -i ${f%.}  -threads 6 -acodec copy -vcodec mjpeg "vid/${f%.mp3}.mp4"; done
