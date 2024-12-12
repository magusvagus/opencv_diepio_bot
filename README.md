# Work In Progress

A simple Bot for the browser game diep.io, using Python with the OpenCV computer vision library.


## Development Stages

This is a personal hobby project to learn more about python and
automation, if everything goes well several stages are planned during
development of this tool.

1. Boilerplate and a basic framework (ready)
- Basic image recognition (needs bigger dataset but works)

| Class    | Images  |Instances|   Box(P    |     R     |   mAP50  | mAP50-95) |
|:---------|:-------:|:-------:|:----------:|:---------:|:--------:|----------:|
| all      |   22    |   168   |   0.575    |   0.654   |   0.711  |    0.407  |
| cube     |   21    |    60   |   0.598    |       1   |   0.918  |    0.621  |
| triangle |   22    |    80   |       1    |   0.653   |   0.959  |    0.613  |
| pentagon |   13    |    27   |   0.703    |   0.963   |   0.968  |    0.394  |
| enemy_npc|    1    |     1   |       0    |       0   |       0  |        0  |

- Simple movement and aiming (in developement)
- Interaction with other NPCs/ players
- automated upgrading and leveling

2. Fine tuning of basic functions
- Full dynamic image recognition
- Advanced movements
- Polished aiming

3. Simple terminal UI using python curses
4. Performance tweaks


### Dependencies

<= Python 3.12.6 \
<= pip                   24.3.1 \
<= numpy                 2.1.3 \
<= opencv-contrib-python 4.10.0.84 \
<= xlib                  0.21 \
<= pynput                1.7.7

**YOLOv8**

<= ultralytics           8.3.0


### Current Implementations

- Image data (small)
- Increased image detection using YOLO.
- Basic Aim-bot
- Basic movement prototype

### Installation

**Python dependencies**

```bash
pip install -r requirements.txt
```
