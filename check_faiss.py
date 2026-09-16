import faiss

index = faiss.read_index("faiss_index.bin")

print("Total vectors:", index.ntotal)