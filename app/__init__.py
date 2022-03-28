from flask import Flask

app = Flask(__name__)

from app.mc_face_detection_ms.controllers import mc_face_detection_ms

app.register_blueprint(mc_face_detection_ms)
