import pickle

test_data = ['Save me!', 'Save me!', 'Save me!']

f = open('test.data', 'w')
pickle.dump(test_data, f)
f.close()

print(pickle.dump)