import cv2
from pathlib import Path

VIDEOS = Path("videos/raw")
FRAMES = Path("frames")
FRAMES.mkdir(exist_ok=True)

for video in VIDEOS.glob("*.mp4"):
    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    step = int(round(fps))  

    count, saved = 0, 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if count % step == 0:
            name = FRAMES / f"{video.stem}_{saved:04d}.jpg"
            cv2.imwrite(str(name), frame)
            saved += 1
        count += 1
    cap.release()
    print(f"{video.name}: Saved {saved} frames")

print("Done! Check the frames/ folder")