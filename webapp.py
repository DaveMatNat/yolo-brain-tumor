"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""
import argparse
import io
import os
from PIL import Image

import torch, json
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)

        # for debugging
        data = results.pandas().xyxy[0].to_json(orient="records")
        mydata = json.loads(data)

		

        #return data

        results.render()  # updates results.imgs with boxes and labels
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            img_base64.save("static/image.jpg", format="JPEG")
        #return redirect("static/image0.jpg")
        return render_template("result.html", label=mydata, imagesource='static/image.jpg')

    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

   #  model = torch.hub.load(
#         "ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True, autoshape=True
#     )  # force_reload = recache latest code
    model = torch.hub.load('./yolov5', 'custom', path='best.pt', source='local')
    model.eval()
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
