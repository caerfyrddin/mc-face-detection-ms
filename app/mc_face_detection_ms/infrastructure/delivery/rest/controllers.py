from flask import Blueprint, request
from app.mc_face_detection_ms.domain.worker.face_detection_worker import FaceDetectionWorker

mc_face_detection_ms = Blueprint(
    'mc_face_detection_ms',
    __name__,
    url_prefix = '/face-detection/'
)

@mc_face_detection_ms.route('/get_face_locations', methods = [ 'GET' ])
def get_face_locations():
    path = request.args['path']
    worker = FaceDetectionWorker(path)
    faces = worker.get_face_locations()
    response = {
        "face_locations": faces
    }
    return response