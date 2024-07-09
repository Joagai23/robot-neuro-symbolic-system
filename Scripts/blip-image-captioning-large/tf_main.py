import tensorflow as tf
import requests
from PIL import Image
from transformers import AutoProcessor, BlipProcessor, TFBlipForConditionalGeneration, BlipForConditionalGeneration
import time

def check_gpu():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

def load_model():
    processor = AutoProcessor.from_pretrained('.')
    model = TFBlipForConditionalGeneration.from_pretrained('.')
    return model, processor

def fetch_image():
    example_img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
    return Image.open(requests.get(example_img_url, stream=True).raw)

def image_to_text(model: TFBlipForConditionalGeneration, processor: AutoProcessor, image: Image):
    inputs = processor(image, return_tensors='tf')
    outputs = model.generate(**inputs, max_new_tokens = 100)
    print(processor.decode(outputs[0], skip_special_tokens=True))

def main():
    check_gpu()
    model, processor = load_model()
    image = fetch_image()
    print("start")
    start_time = time.time()
    image_to_text(model, processor, image)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()