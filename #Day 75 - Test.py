#Day 75 - Test
import pickle
test_data = [1, 2, 3]
pickled = pickle.dumps(test_data)
unpickled = pickle.loads(pickled)
print("Pickle test:", unpickled == [1, 2, 3])
print("Day 75 test ok")