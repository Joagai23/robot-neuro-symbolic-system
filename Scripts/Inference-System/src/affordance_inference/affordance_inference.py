from ..perception_model.perception import PerceptionModel
from ..reasoning_system.reasoning import ReasoningSystem
from PIL import Image
import io
import pandas as pd
from pandas import concat, DataFrame

class AffordanceInference:
    '''
    Affordance Inference class to provide the Docker Container with all the logic and functionality
    '''
    def __init__(self) -> None:
        print("Starting Affordance Inference System...")
        self.perception_model = PerceptionModel()
        self.reasoning_system = ReasoningSystem()

    def evaluate_image(self, image_bytes:bytearray, camera:str, jar:str) -> dict:
        image = Image.open(io.BytesIO(bytes(image_bytes)))
        image_caption = self.perception_model.generate_caption(image=image)
        
        df = pd.read_csv('C:/Jorge/Universidad/JU/2/Thesis/Scripts/Inference-System/src/reasoning_system/quick_robot_evaluation_captions.csv')
        df.loc[len(df.index)] = [jar, camera, image_caption]
        df.to_csv('C:/Jorge/Universidad/JU/2/Thesis/Scripts/Inference-System/src/reasoning_system/quick_robot_evaluation_captions.csv', index=False)

        return image_caption, self.reasoning_system.infer_affordances(caption=image_caption)