# VisionX-AI – AI-Powered Assistant for Visually Impaired

VisionX-AI is a team-based AI and computer vision project designed to assist
visually impaired users in understanding their surroundings through object
detection and text recognition, with audio feedback planned as part of the
complete system.

## My Contribution

My contribution focuses on the AI components of VisionX-AI:

### Object Detection – YOLOv8
- Implemented YOLOv8-based object detection.
- Detects objects and provides bounding boxes and confidence scores.
- Applied confidence-threshold filtering to retain reliable detections.

###Text Recognition – EasyOCR
- Developed the `ocr_reader` module for text recognition using EasyOCR.
- Processes visual input to detect and extract readable text.
- Integrated OCR functionality into the VisionX-AI workflow.
  
## Tech Stack

- Python
- YOLOv8
- EasyOCR
- OpenCV
- Computer Vision
- Deep Learning

## My Workflow

Visual Input
    ↓
OpenCV Processing
    ↓
YOLOv8 Object Detection
    ↓
Confidence Filtering
    ↓
EasyOCR Text Recognition
    ↓
Processed Output

## Project Status

**In Progress**

VisionX-AI is being developed collaboratively as a team project.
This repository focuses specifically on my individual contribution to
the computer vision and AI components.

## Future Integration

The complete project is planned to include:

- Real-time camera-based processing
- Integration of object detection and OCR
- Text-to-speech/audio feedback
- End-to-end assistance for visually impaired users
