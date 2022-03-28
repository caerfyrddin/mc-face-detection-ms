from flask import Blueprint, request

mc_face_detection_ms = Blueprint('mc_face_detection_ms', __name__, url_prefix='/face-detection/')

# FIXME: remove GET method
@mc_face_detection_ms.route('/process', methods = [ 'GET', 'POST' ])
def process():
    return 'Works!'
