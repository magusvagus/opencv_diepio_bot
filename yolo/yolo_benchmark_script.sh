#!/bin/bash

# make sure to use absolute file paths

# path to model
model=model=/home/ed/programming/python/opencv_bot/opencv_diepio_bot/runs/detect/yolo_v8n_diep2k2/weights/best.pt

# path to dataset
data=data=/home/ed/programming/python/opencv_bot/opencv_diepio_bot/yolo/config.yaml

# script
yolo task=detect mode=val $model $data imgsz=1280
