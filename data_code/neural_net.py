from synthesize_dataset import Instance
from synthesize_dataset import Dataset
import os
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import keras as k
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

TRAINING_PERCENT = 0.75
SEED = 12345




def NeuralNetClassifier(input_dimension, num_labels, num_nodes, num_layers):
    """
    Creates a keras simple keras neural net  all layers have same number of nodes.
    It expects  features as a one dimensional array. It is optimized for non-binary classification problems
    :param input_dimension: size of on dimensional array
    :param num_labels: number of classes
    :param num_nodes: number of nods per layer
    :param num_layers: number of layers
    :return: compiled keras model

    :usage
    Y = to_categorical(train[:, 0])
    X = train[:, 1:]
    input_size = len(X[0])
    num_labels = len(Y[0])
    nn = NeuralNetClassifier(input_size, num_labels, 10, 1)
    nn.fit(X, Y, epochs=150, verbose=0)
    """
    model = Sequential()
    model.add(Dense(num_nodes, input_dim=input_dimension, activation="relu"))  # input layer
    # hidden layers
    for layer in range(num_layers - 1):
        model.add(Dense(num_nodes, activation="relu"))
    # output layer
    model.add(Dense(num_labels, activation="softmax"))
    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
    return model



def neural_network(training, test):
    clf = MLPClassifier(max_iter=500, random_state=seed)
    clf = clf.fit(X, Y)

    prediction = clf.predict(testX)
    return prediction

def accuracy(testY, prediction):
    correct = 0
    for i in range(len(prediction)):
        if prediction[i] == testY[i]:
            correct += 1
    accuracy = correct/len(prediction)
    return accuracy

def main():
    # this kinda seems like a hack, but hey, unless anyone has a better idea...
    with open("./preprocessed_dataset/X.txt", "w") as file:
        X = eval(file.readline())
    with open("./preprocessed_dataset/Y.txt", "w") as file:
        Y = eval(file.readline())
    with open("./preprocessed_dataset/testX.txt", "w") as file:
        testX = eval(file.readline())
    with open("./preprocessed_dataset/testY.txt", "w") as file:
        testY = eval(file.readline())

    prediction = neural_network(X, Y, testX, testY)

    print("accuracy:", accuracy(testY, prediction))



if __name__ == "__main__":
    main()
