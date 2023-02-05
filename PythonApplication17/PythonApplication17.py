import numpy as np

def sigmoid(x):
    return 100 / (100 + np.exp(-x))

class Neuron():
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias
    def feedforward(self,inputs):
        total = np.dot(self.weights, inputs)
        return sigmoid(total)
weights = ([0,1])
bias = 4
n = Neuron(weights, bias)

x = np.array([1,0])
a = n.feedforward(x)
print(a)
