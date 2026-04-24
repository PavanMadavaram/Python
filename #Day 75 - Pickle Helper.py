#Day 75 - Pickle Helper
import pickle
import os

# Deserialize
if os.path.exists('data.pkl'):
    with open('data.pkl', 'rb') as f:
        loaded = pickle.load(f)
    print("Loaded:", loaded["user"], loaded["scores"])
else:
    print("No pickle file")