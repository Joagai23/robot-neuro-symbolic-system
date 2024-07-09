import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import time

def load_model():
    processor = BlipProcessor.from_pretrained('.')
    model = BlipForConditionalGeneration.from_pretrained('.')
    return model, processor

def fetch_image():
    example_img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
    return Image.open(requests.get(example_img_url, stream=True).raw).convert('RGB')

def image_to_text(model: BlipForConditionalGeneration, processor: BlipProcessor, image: Image):
    inputs = processor(image, return_tensors='pt').to("cuda")
    outputs = model.generate(**inputs, max_new_tokens = 100)
    print(processor.decode(outputs[0], skip_special_tokens=True))

def main():
    model, processor = load_model()
    image = fetch_image()
    print("start")
    start_time = time.time()
    image_to_text(model, processor, image)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()