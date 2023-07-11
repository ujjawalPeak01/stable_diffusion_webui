import os
import webui
from modules.api.api import Api
from modules.api.models import StableDiffusionTxt2ImgProcessingAPI, StableDiffusionImg2ImgProcessingAPI

class InferlessPythonModel:
    def initialize(self):
        file_path = "/var/nfs-mount/model_cache/a111/modules/"
        if not os.path.exists(file_path):
            cmd = "git clone https://github.com/ujjawalPeak01/stable_diffusion_webui /var/nfs-mount/model_cache/a111/modules/"
            os.system(cmd)
        webui.initialize()

    def infer(self, inputs):
        api = Api()
        arg = StableDiffusionTxt2ImgProcessingAPI(prompt=inputs["prompt"])
        response = api.text2imgapi(txt2imgreq=arg)
        result = {}
        print(response.images[0], flush=True)
        result["generated_image_base64"] = response.images[0]
        return result
        
    def finalize(self):
        pass
