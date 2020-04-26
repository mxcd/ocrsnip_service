import logging
from flask import request, Response
from flask_api import status
from image_store import add_image, get_image
import cv2
import numpy as np
import pytesseract
import json

log = logging.getLogger("ocr.endpoints.snip")


def register_endpoint(app):
    @app.route('/snip', methods=['GET'])
    def snip():
        if not ("id" in request.args and "secret" in request.args
                and "x1" in request.args and "y1" in request.args and "x2" in request.args and "y2" in request.args):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        id = request.args["id"]
        secret = request.args["secret"]
        x1 = float(request.args["x1"])
        y1 = float(request.args["y1"])
        x2 = float(request.args["x2"])
        y2 = float(request.args["y2"])

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        img = get_image(id, secret)
        if img is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            text = get_snip_text(img, x1, y1, x2, y2)
            return Response(status=200, response=text)


def get_snip_text(img, x1, y1, x2, y2):
    img = cv2.imdecode(np.frombuffer(img, np.uint8), -1)
    width = img.shape[1]
    height = img.shape[0]
    x1 = x1 * width
    x2 = x2 * width
    y1 = y1 * height
    y2 = y2 * height
    patch = img[int(y1):int(y2), int(x1):int(x2)]
    rgb_patch = cv2.cvtColor(patch, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(rgb_patch, lang='deu', config='--psm 6')
    return text
