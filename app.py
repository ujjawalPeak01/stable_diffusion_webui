import webui
from modules.api.api import Api
from modules.api.models import StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI

class InferlessPythonModel:
    def initialize(self):
        webui.initialize()

    def infer(self, prompt):
        api = Api()
        arg = StableDiffusionTxt2ImgProcessingAPI(prompt=prompt)
        result = {}
        print(response.images[0], flush=True)
        result["generated_image_base64"] = response.images[0]
        return result
        
    def finalize(self):
        pass
