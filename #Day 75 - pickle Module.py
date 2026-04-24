#Day 75 - pickle Module
import pickle

# Serialize object
data = {"user": "dev", "scores": [95, 87, 92]}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

print("Pickled data saved!")