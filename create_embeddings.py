import os
import pickle
import numpy as np
from PIL import Image
from tqdm import tqdm
import torch
import open_clip

# Load OpenCLIP model
model, _, preprocess = open_clip.create_model_and_transforms(
    'ViT-B-32',
    pretrained='laion2b_s34b_b79k'
)

model.eval()

image_folder = "images/images"


image_files = os.listdir(image_folder)

embeddings = []
filenames = []

for file in tqdm(image_files):
    try:
        image_path = os.path.join(image_folder, file)

        image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0)

        with torch.no_grad():
            embedding = model.encode_image(image)

        embedding = embedding.cpu().numpy().flatten()

        embeddings.append(embedding)
        filenames.append(image_path)

    except Exception as e:
        print("Error:", file, e)

embeddings = np.array(embeddings)

np.save("embeddings.npy", embeddings)

with open("filenames.pkl", "wb") as f:
    pickle.dump(filenames, f)

print("Embeddings Shape:", embeddings.shape)
print("Done!")