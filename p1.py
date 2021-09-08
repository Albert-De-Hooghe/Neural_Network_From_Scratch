inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
biases = 3

if __name__ == "__main__":
    import numpy as np
    output = np.dot(weights, inputs) + biases
    print(output)