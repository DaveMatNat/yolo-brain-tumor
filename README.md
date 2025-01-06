# YOLO Brain Tumor Detection

This project implements a YOLOv5 object detection model to identify brain tumors in MRI images. The model is deployed through a Flask web application, allowing users to upload MRI scans and receive real-time predictions on tumor presence.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Example](#example)
- [Reference](#reference)

---

## Project Overview

This project uses a YOLOv5 object detection model to identify brain tumors in MRI images. The deployment is facilitated through a Flask web application, enabling users to upload MRI scans and receive real-time predictions on tumor presence.


---

## Dataset

The model is trained on the [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) from Kaggle. This dataset comprises images categorized into three types of brain tumors: meningioma, glioma, and pituitary tumors. The dataset is instrumental in training the model to accurately detect and classify different tumor types.

---

## Features

- **Model Deployment:** Utilizes a pre-trained YOLOv5 model for detecting brain tumors.
- **Web Interface:** Provides an intuitive interface for uploading MRI images and viewing detection results.
- **Flask Framework:** Employs Flask to serve the model and handle user interactions.

---

## Installation

Follow the steps below to set up the project on macOS:

1. Install **Conda** if you haven’t already. You can download it from [Anaconda's official website](https://www.anaconda.com/products/distribution).

2. Clone this Repo:
   ```bash
   git clone https://github.com/DaveMatNat/yolo-brain-tumor.git
   ```
   ```bash
   cd yolo-brain-tumor
   ```

3. Create a new Conda environment:
    ```bash
    conda create --name BrainTumor
    ```
4.	Activate the Conda environment:
    ```bash
    conda activate BrainTumor
    ```
5. Install python version 3.10.16:
   ```bash
   conda install python=3.10.16
   ```
6. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Run the Web Application:
   ```bash
   python3 webapp.py --port 5001
   ```
Once these steps are complete, the application should be running on http://localhost:5001

## Example

<img width="404" height="360" alt="image" src="https://github.com/user-attachments/assets/91798f9c-6a37-42eb-a8cc-9c8919622990" />
<img width="599" alt="image" src="https://github.com/user-attachments/assets/ddd4b732-0e6b-49e9-9fb4-340111b13085" />


## Reference
- https://github.com/ultralytics/yolov5
- https://github.com/jzhang533/yolov5-flask
- https://github.com/avinassh/pytorch-flask-api-heroku

### Yolov5 Object Detection Model Deployment Using Flask
This repo contains example apps for exposing the [yolo5](https://github.com/ultralytics/yolov5) with custom object detection model(sea.pt)
