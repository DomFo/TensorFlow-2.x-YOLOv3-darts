FROM tensorflow/tensorflow:latest-gpu
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-dev ffmpeg libsm6 libxext6
