from synthesize_dataset import Instance
from synthesize_dataset import Dataset
import os
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

TRAINING_PERCENT = 0.75
SEED = 12345

def neural_network(training, test):
    clf = MLPClassifier(max_iter=500, random_state=seed)
    clf = clf.fit(X,Y)

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
