# Work In Progress

A simple Bot for the browser game diep.io, using Python with the OpenCV computer vision library.


## Development Stages

This is a personal hobby project to learn more about python and
automation, if everything goes well several stages are planned during
development of this tool.

1. Boilerplate and a basic framework (ready)
- Basic image recognition (needs bigger dataset but works)

>Class  |   Images | Instances |  Box(P    |    R    |    mAP50  |  mAP50-95) \
> all      |   21    |  164   |   0.213    |  0.506    |  0.379   |   0.131 \
> class_0  |   20    |   59   |   0.132    |      1    |  0.581   |    0.22 \
> class_1  |    21   |    79  |    0.507   |   0.519   |   0.502  |    0.168 \
> class_2  |    12   |    26  |        0   |       0   |   0.054  |  0.00579

- Simple movement and aiming (in developement)
- Interaction with other objects/ players
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

YOLOv8 \

<= ultralytics           8.2.103

### Current Implementations

- Image data (small)
- Increased image detection using YOLO.

