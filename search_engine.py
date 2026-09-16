import pickle
import faiss
import open_clip
import torch
from PIL import Image
import numpy as np

# Load model once
model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32",
    pretrained="laion2b_s34b_b79k"
)

model.eval()

# Load FAISS index
index = faiss.read_index("faiss_index.bin")

# Load filenames
with open("filenames.pkl", "rb") as f:
    filenames = pickle.load(f)


def search_similar_images(image_path, top_k=5):

    image = preprocess(
        Image.open(image_path).convert("RGB")
    ).unsqueeze(0)

    with torch.no_grad():
        embedding = model.encode_image(image)

    embedding = embedding.cpu().numpy().astype("float32")

    distances, indices = index.search(embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(filenames[idx])

    return results