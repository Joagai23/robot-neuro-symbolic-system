from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class PerceptionModel:
    '''
    Class to load and manage perception queries
    '''

    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("./src/perception_model")
        self.model = BlipForConditionalGeneration.from_pretrained("./src/perception_model").to("cuda")

    def generate_caption(self, image: Image) -> str:
        inputs = self.processor(images=image, return_tensors="pt").to("cuda")
        pixel_values = inputs.pixel_values

        generated_ids = self.model.generate(pixel_values=pixel_values, max_length=50)
        return self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]