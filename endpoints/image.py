import logging
from flask import request, Response
from flask_api import status
from image_store import add_image, get_image
import json

log = logging.getLogger("ocr.endpoints.image")


def register_endpoint(app):
    @app.route('/image', methods=['POST'])
    def image_post():
        log.info("Received image POST")

        if "image" not in request.files:
            log.error("Image file missing")
            return Response(response="image file missing", status=status.HTTP_400_BAD_REQUEST)

        image_file_data = request.files["image"].read()
        if not check_image_file(image_file_data):
            log.error("uploaded file is not a valid image file")
            return Response(response="uploaded file is not a valid image file",
                            status=status.HTTP_400_BAD_REQUEST)

        id, secret = add_image(image_file_data)

        return Response(response=json.dumps({"id": id, "secret": secret}), status=status.HTTP_200_OK)

    @app.route('/image', methods=['GET'])
    def image_get():
        if not ("id" in request.args and "secret" in request.args):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        img = get_image(request.args["id"], request.args["secret"])
        if img is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(response=img, status=status.HTTP_200_OK)

    # TODO: delete image endpoint


def check_image_file(img):
    # TODO check image for actually being one
    return True
