import time
from ultralytics import YOLO

model = YOLO("best.pt")

results = model.track(
    source="videos/test/Hartland-qulidier-playoff-m6.mp4",
    stream=True,
    verbose=False,
    show=True,
    device="mps",         
)

start = time.time()
n = 0
for r in results:
    n += 1
    if n % 200 == 0:
        fps = n / (time.time() - start)
        print(f"Frames: {n}, Speed: {fps:.0f} FPS")

fps = n / (time.time() - start)
print(f"\Total: {n} frames, Average speed {fps:.0f} FPS")