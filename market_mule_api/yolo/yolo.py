import os
import threading 
import subprocess

class yolo(threading.Thread):

    def __init__(self,timeout:int,image_path:str) -> None:
        super().__init__(target=self.start,name="yolo thread")
        self.timeout = timeout
        self.darknet_path = os.getcwd() + "/market_mule_api/yolo/darknet"
        self.image_path = image_path
        

    def start(self) -> str:
        if(not os.path.exists(self.darknet_path)):
            print("darknet executable didn't found")
            return None 
        
        command = (
            "./darknet",
            "detect",          
            "cfg/yolov3.cfg",
            "yolov3.weights",
            self.image_path
            )
        
        try:
            process = subprocess.Popen(args=command,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True,
                                    shell=False,
                                    cwd=self.darknet_path)
        except Exception as exp:
            print("Invalid args on Popen")

        try:
            outs, errs = process.communicate(input=None,timeout=self.timeout)
            return self.parser(outs)
        
        except Exception as excep:
            print(excep)
    
    def parser(self,text:str)-> str:
        results = text.split('\n')
        self.time_consumed(results.pop(0))
        results = results[:-1]
        return results
    
    def time_consumed(self,text:str):
        print(text)
