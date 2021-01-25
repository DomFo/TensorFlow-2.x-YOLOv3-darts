#!/bin/bash

docker run -p 0.0.0.0:6006:6006 \
  --gpus all \
  -it \
  --rm \
  -v $PWD:/tmp \
  -w /tmp yolov3_darts:latest python detect_darts.py ;
