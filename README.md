## Data

## Yolov5 Object Detection Model Deployment Using Flask
This repo contains example apps for exposing the [yolo5](https://github.com/ultralytics/yolov5) with custom object detection model(sea.pt)

## Installation

Follow the steps below to set up the project on macOS:

1. Install **Conda** if you haven’t already. You can download it from [Anaconda's official website](https://www.anaconda.com/products/distribution).

2. Clone this Repo:
   ```bash
   git clone https://github.com/DaveMatNat/yolo-brain-tumor.git
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

## Reference
- https://github.com/ultralytics/yolov5
- https://github.com/jzhang533/yolov5-flask
- https://github.com/avinassh/pytorch-flask-api-heroku
