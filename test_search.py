from search_engine import search_similar_images

results = search_similar_images(
    r"C:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot 2026-09-16 153457.png"
)

for r in results:
    print(r)