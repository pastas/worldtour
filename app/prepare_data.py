"""This script is used to prepare data to display in the Pastas worldtour map."""
import pandas as pd
import pastas as ps
import os

df = pd.DataFrame(
    columns=["name", "lat", "lon", "description", "url", "image", "author"]
)

mls = {}

for fname in os.listdir("./data/models"):
    if fname.endswith(".pas"):
        ml = ps.io.load(os.path.join("./data/models", fname))
        mls[fname] = ml
