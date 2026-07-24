# FTC AI Spectator Camera 🤖📹

Real-time robot detection and tracking for **FIRST Tech Challenge** matches, built with a custom-trained YOLOv8 model.

> Built by an FTC competitor — tested on my own team's matches in Kazakhstan.

<img width="640" height="360" alt="demo" src="https://github.com/user-attachments/assets/0a89722a-6c6c-479e-98f0-6710cc7c500e" />

## What it does

- Detects all robots on the field (up to 4) from static camera footage
- Tracks each robot across frames with a persistent ID (ByteTrack)
- Works on tournaments it has never seen — including different venues, lighting, and screen recordings

## Results

| Metric | Value |
|--------|-------|
| mAP@50 | **96.1%** |
| Precision | 94.2% |
| Recall | 89.5% |
| Inference speed (Colab T4 GPU) | 3.2 ms/frame (~300 FPS) |
| End-to-end on MacBook (CPU) | ~20 FPS |

Model: YOLOv8n (3M params, 6 MB) — small enough for real-time use on edge devices.

## How it was built

1. **Data collection** — frames extracted from 8 full matches across 6 different FTC tournaments (DECODE season), downloaded from public streams
2. **Labeling** — semi-automated pipeline in Roboflow: 10 frames labeled by hand → model-assisted labeling for the rest → manual review (173 approved images)
3. **Training** — YOLOv8n fine-tuned on Google Colab (T4), 79 epochs with early stopping; hue augmentation disabled to preserve alliance colors
4. **Evaluation** — tested on a held-out tournament (Hawaii) and real matches of my own team — footage the model never saw during training
Dataset is public on [Roboflow Universe](https://universe.roboflow.com/husein-maxut/find-ftc-robot).

## Project structure

```
extract_frames.py   # cut video into frames for labeling
train.py            # train YOLOv8 on the Roboflow dataset (Colab)
test_local.py       # run tracking on a video locally + FPS benchmark
weights/best.pt     # trained model weights
```

## Quick start

```bash
pip install ultralytics
python test_local.py   # runs tracking on your video with live preview
```

Or in Python:

```python
from ultralytics import YOLO
model = YOLO("weights/best.pt")
model.track(source="your_match.mp4", save=True, conf=0.35)
```

## Roadmap

- [x] Robot detection + multi-object tracking
- [ ] Alliance color classification (red / blue)
- [ ] Team number recognition (OCR on number holders)
- [ ] Automatic score tracking (goal detection)
- [ ] Foul detection — planned as a research project

## Author

Khussein — FTC competitor from Kazakhstan 🇰🇿 | Team URAN92 #25300 | This project started as a passion project and is growing into a research project on automated judging in educational robotics.
