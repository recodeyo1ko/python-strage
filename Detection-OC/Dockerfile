# nvidiaのpytorchを使用する
# FROM nvcr.io/nvidia/pytorch:21.08-py3
FROM pytorch/pytorch

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 v4l-utils && \
    # pipのアップデート
    pip install --upgrade pip && \
    pip install opencv-python && \
    pip install ultralytics

# 作業するディレクトリを変更
WORKDIR ${ROOT}
COPY . ${ROOT}
