import os

JOKE = "My coding agent fixed the crash in seconds — by deleting the feature that crashed."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
