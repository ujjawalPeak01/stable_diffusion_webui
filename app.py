import webui
from modules.api.api import Api
from modules.api.models import StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI

class InferlessPythonModel:
    def initialize(self):
        webui.initialize()

    def infer(self, prompt):
        api = Api()
        arg = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt)
        return api.text2imgapi(txt2imgreq=arg)
        
    def finalize(self):
        pass
