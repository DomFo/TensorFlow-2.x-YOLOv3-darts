#!/bin/bash

xhost +local:root

docker run -p 0.0.0.0:6006:6006 \
  -e DISPLAY=${DISPLAY} \
  --device=/dev/video0:/dev/video0 \
  --env QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --gpus all \
  -it \
  --rm \
  -v $PWD:/tmp \
  -w /tmp yolov3_darts:latest python detect_darts.py ;  # detection_demo.py

xhost -local:root