def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

file = 'd:\data_public\cifar\cifar-10-batches-py\test_batch'
unpickle(file)
print(dict)