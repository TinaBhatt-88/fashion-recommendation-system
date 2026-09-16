import os

print("Level 1:")
print(os.listdir("images"))

print("\nLevel 2:")
print(os.listdir("images/images")[:20])

print("\nTotal:")
print(len(os.listdir("images/images")))