from flask import Flask
import endpoints.image
import endpoints.snip
from flask_cors import CORS
import logging

log = logging.getLogger("ocr.service")

port = 5000


def start_service():
    app = Flask(__name__)
    CORS(app)
    endpoints.image.register_endpoint(app)
    endpoints.snip.register_endpoint(app)

    log.info("Starting service at port {}".format(port))
    app.run(port=port, host="0.0.0.0", threaded=True)
