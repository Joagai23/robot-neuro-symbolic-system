import requests
import time
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

image_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images'

processor = AutoProcessor.from_pretrained("C:/Jorge/Universidad/JU/2/Thesis/Scripts/blip-image-captioning-large/FINE_TUNE")
model = BlipForConditionalGeneration.from_pretrained("C:/Jorge/Universidad/JU/2/Thesis/Scripts/blip-image-captioning-large/FINE_TUNE").to("cuda")

raw_image = Image.open(image_dir + '/14.jpg')

start_time = time.time()

'''inputs = processor(raw_image, return_tensors="pt").to("cuda")
out = model.generate(**inputs, max_new_tokens = 100)
print(processor.decode(out[0], skip_special_tokens=True))'''

inputs = processor(images=raw_image, return_tensors="pt").to("cuda")
pixel_values = inputs.pixel_values

generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_caption)

print("--- %s seconds ---" % (time.time() - start_time))