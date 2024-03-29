import numpy as np

'''Actuation function'''

def sigmoid(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

def step(x):
    if x >= 0.5:
        return 1
    else:
        return 0

'''Inputs'''

x = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])

'''Outputs'''

y = np.array([[0],
              [0],
              [1],
              [1]])

'''Nodes'''

input_nodes = 3
output_node = 1

'''Random seed'''

np.random.seed(1)

'''Synapses'''

syn0 = 2 * np.random.random((input_nodes,output_node))

'''Bias'''

bias_o = np.random.randn()

'''Learning rate & Iteration'''

learning_rate = 0.1
iteration = 100000

'''Training loop'''

for i in range(iteration):

    # Layers and Propagation

    l0 = x
    l1 = sigmoid(np.dot(l0, syn0) + bias_o)

    # Error and Back propagation

    l1_error = y - l1
    if (i % (iteration/10)) == 0:
        print('Error: ' + str(np.mean(np.abs(l1_error * 100))) + ' % ')
        
    l1_delta = l1_error * sigmoid(l1, deriv=True) * learning_rate

    # Correction

    syn0 += l0.T.dot(l1_delta)

'''Print result'''

print('-------------------')
print('Actual outputs: ' + str(y.T))
print('Output after training: ' + str(l1.T))

'''Inputs test'''

A = float(input('Inputs A : '))
B = float(input('Inputs B : '))
C = float(input('Inputs C : '))

x = np.array([A,B,C])

'''Prediction'''

l0 = x
l1 = sigmoid(np.dot(l0, syn0) + bias_o)

output = step(l1)
print('Predicted output: ' + str(output))
