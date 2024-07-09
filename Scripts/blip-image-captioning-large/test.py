import requests
import time
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

image_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images'

processor = BlipProcessor.from_pretrained(".")
model = BlipForConditionalGeneration.from_pretrained(".").to("cuda")

raw_image = Image.open(image_dir + '/7.jpg').convert('RGB')

start_time = time.time()

inputs = processor(raw_image, return_tensors="pt").to("cuda")
out = model.generate(**inputs, max_new_tokens = 100)
print(processor.decode(out[0], skip_special_tokens=True))

print("--- %s seconds ---" % (time.time() - start_time))