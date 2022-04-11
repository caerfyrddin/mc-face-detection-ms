from curses import raw
import os, cv2, dlib, face_recognition
from werkzeug.exceptions import NotFound, InternalServerError
from config import DATA_DIR

class FaceDetectionWorker:
    
    @staticmethod
    def cv2_is_using_cuda() -> bool:
        return cv2.cuda.getCudaEnabledDeviceCount() > 0

    @staticmethod
    def dlib_is_using_cuda() -> bool:
        return dlib.DLIB_USE_CUDA and dlib.cuda.get_num_devices() > 0

    def get_full_data_path(self) -> str:
        return os.path.join(DATA_DIR, self.path)

    def assert_file_exists(self):
        if not os.path.isfile(self.full_path):
            raise NotFound("No file with specified path was found.")

    def __init__(self, path: str):
        if not (
            FaceDetectionWorker.cv2_is_using_cuda() and
            FaceDetectionWorker.dlib_is_using_cuda()
        ):
            raise InternalServerError("OpenCV or dlib are not using CUDA.")
        self.path = path
        self.full_path = self.get_full_data_path()
        self.assert_file_exists()

    @staticmethod
    def transform_face_location(id: int, face_location: list) -> dict:
        return {
            "id": id,
            "rect": {
                "top":      face_location[0],
                "right":    face_location[1],
                "bottom":   face_location[2],
                "left":     face_location[3]
            }
        }

    def get_face_locations(self) -> list:
        image = face_recognition.load_image_file(self.full_path)
        raw_face_locations = face_recognition.face_locations(image, model = 'cnn')
        face_locations = []
        for i in range(0, len(raw_face_locations)):
            face_locations.append(FaceDetectionWorker.transform_face_location(i + 1, raw_face_locations[i]))
        return face_locations