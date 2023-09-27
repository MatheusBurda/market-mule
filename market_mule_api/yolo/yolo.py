import os
import threading 
import subprocess
from time import sleep


class Yolo(threading.Thread):
    def __init__(self, timeout: int, image_path: str) -> None:
        super().__init__(target=self.start, name="Yolo thread")

        self.timeout = timeout

        self.darknet_path = os.getcwd() + "/market_mule_api/yolo/darknet"
        if not os.path.exists(self.darknet_path):
            raise FileNotFoundError("darknet executable didn't found")

        self.image_path = image_path
        if not os.path.exists(image_path):
            raise FileNotFoundError("Image didn't found")

        self.identified_obj = None

    def run(self):
        command = (
            "./darknet",
            "detect",
            "cfg/yolov3.cfg",
            "yolov3.weights",
            self.image_path,
        )

        process = subprocess.Popen(
            args=command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            shell=False,
            cwd=self.darknet_path,
        )

        outs, errs = process.communicate(input=None, timeout=self.timeout)
        self.identified_obj = self.parser(outs)

    def parser(self, text: str) -> str:
        results = text.split("\n")
        self.time_consumed(results.pop(0))
        results = results[:-1]
        return results

    def time_consumed(self, text: str):
        print(text)


# Exemplo de utilizacao
timeout = 40  # seconds
image_path = "/home/luis/Deskto/market-mule/market_mule_api/yolo/darknet/data/dog.jpg"
yolo = Yolo(timeout, image_path=image_path)
yolo.start()
while yolo.is_alive():
    sleep(5)
obj = yolo.identified_obj
if obj != None:
    print(obj)
