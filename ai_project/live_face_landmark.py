# 라이브 스트림 샘플 코드
# https://developers.google.com/mediapipe/solutions/vision/face_landmarker/python#live-stream
# 가이드
# https://developers.google.com/mediapipe/solutions/vision/face_landmarker#configurations_options




# STEP 0. read bytes from http

# STEP 1: Install packages
from typing import Union
from fastapi import FastAPI

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: load inference module/ Create an FaceLandmarker object.
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode
model_path = 'models/face_landmarker.task'

app = FastAPI()

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
# detector = vision.FaceLandmarker.create_from_options(options)


# Create a face landmarker instance with the live stream mode:
def print_result(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('face landmarker result: {}'.format(result))


# STEP 3: prepare input data
# 입력을 이미지 파일이나 numpy 배열로 준비한 다음 객체로 변환하세요 
# mediapipe.Image. 입력이 비디오 파일이거나 웹캠의 라이브 스트림인 경우 
# OpenCV 와 같은 외부 라이브러리를 사용하여 입력 프레임을 numpy 배열로 로드할 수 있습니다.
mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)
    


with FaceLandmarker.create_from_options(options) as landmarker:
    print(landmarker)
  # The landmarker is initialized. Use it here.
  # ..

# STEP 4 : Inference
# Send live image data to perform face landmarking.
# The results are accessible via the `result_callback` provided in
# the `FaceLandmarkerOptions` object.
# The face landmarker must be created with the live stream mode.
detection_result = landmarker.detect_async(mp_image, frame_timestamp_ms)


# STEP 4: Detect objects in the input image.

# STEP 5: Process the detection result. In this case, visualize it.