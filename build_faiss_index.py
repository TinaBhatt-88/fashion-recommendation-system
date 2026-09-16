import numpy as np
import faiss

# Load embeddings
embeddings = np.load("embeddings.npy")

print("Embeddings shape:", embeddings.shape)

# Convert to float32
embeddings = embeddings.astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Total vectors in index:", index.ntotal)

# Save index
faiss.write_index(index, "faiss_index.bin")

print("FAISS index saved successfully!")