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
| all      |   22    |   168   |    0.94    |   0.739   |   0.977  |    0.793  |
| cube     |   21    |    60   |   0.856    |       1   |   0.963  |    0.895  |
| triangle |   22    |    80   |   0.972    |   0.963   |   0.964  |    0.857  |
| pentagon |   13    |    27   |   0.931    |   0.994   |   0.986  |    0.723  |
| enemy_npc|    1    |     1   |       1    |       0   |   0.995  |    0.697  |

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
