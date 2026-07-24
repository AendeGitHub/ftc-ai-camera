# FTC AI Spectator Camera 🤖📹

Real-time robot detection and tracking for **FIRST Tech Challenge** matches, built with a custom-trained YOLOv8 model.

> Built by an FTC competitor — tested on my own team's matches in Kazakhstan.

<!-- DEMO GIF WILL GO HERE -->

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
4. **Evaluation** — tested on 2 held-out tournaments (Hawaii, Hartland) the model never saw during training

Dataset is public on [Roboflow Universe](https://universe.roboflow.com/husein-maxut/find-ftc-robot)).

## Project structure
