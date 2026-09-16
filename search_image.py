import pickle
import faiss
from PIL import Image
import open_clip
import torch
import matplotlib.pyplot as plt

# Load model
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

# Query image
query_image = r"C:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot 2026-09-16 153457.png"

# Create embedding
image = preprocess(
    Image.open(query_image).convert("RGB")
).unsqueeze(0)

with torch.no_grad():
    embedding = model.encode_image(image)

embedding = embedding.cpu().numpy().astype("float32")

# Search Top 10
distances, indices = index.search(embedding, 10)

print("\nTop Results:")
for rank, idx in enumerate(indices[0]):
    print(f"{rank + 1}. {filenames[idx]}")

# -----------------------------
# Display Query + Recommendations
# -----------------------------

plt.figure(figsize=(18, 6))

# Query image
query_img = Image.open(query_image)

plt.subplot(2, 6, 1)
plt.imshow(query_img)
plt.title("Query")
plt.axis("off")

# Top 5 results
for pos, idx in enumerate(indices[0][:5]):
    img = Image.open(filenames[idx])

    plt.subplot(2, 6, pos + 2)
    plt.imshow(img)
    plt.title(f"Rank {pos + 1}")
    plt.axis("off")

plt.tight_layout()
plt.show()