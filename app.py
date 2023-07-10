import os
import webui
from modules.api.api import Api
from modules.api.models import StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI

class InferlessPythonModel:
    def initialize(self):
        webui.initialize()

    def infer(self, prompt):
        folder_path = "models/Stable-diffusion/"
        absolute_path = os.path.abspath(folder_path)
        folder_contents = os.listdir(absolute_path)
        print("Folder contents:", flush=True)
        for item in folder_contents:
            print(item, flush=True)
        api = Api()
        arg = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt)
        return api.text2imgapi(txt2imgreq=arg)
        
    def finalize(self):
        pass
