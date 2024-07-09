from datasets import load_dataset
from torch.utils.data import Dataset, DataLoader
from transformers import AutoProcessor, BlipForConditionalGeneration

image_dir = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images'
dataset_file = 'C:/Jorge/Universidad/JU/2/Thesis/Datasets/Images/annotations/metadata.csv'

dataset = load_dataset(path=image_dir, data_dir="annotations", split="train")
dataset[0]["image"]

class ImageCaptioningDataset(Dataset):
    def __init__(self, dataset, processor):
        self.dataset = dataset
        self.processor = processor

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        encoding = self.processor(images=item["image"], text=item["text"], padding="max_length", return_tensors="pt")
        # remove batch dimension
        encoding = {k:v.squeeze() for k,v in encoding.items()}
        return encoding