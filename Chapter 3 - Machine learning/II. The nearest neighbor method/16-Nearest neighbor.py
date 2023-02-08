import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

X = MinMaxScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

y_predict = np.empty(len(y_test), dtype=np.int64)


lines = []

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3 
    
    for i, test_item in enumerate(X_test):
        distances = [dist(train_item, test_item) for train_item in X_train]

        sdistances = np.argsort(distances)

        ylist = []
        for index in range(0, 3):
            lines.append(np.stack((test_item, X_train[sdistances[index]])))
            ylist.append(y_train[sdistances[index]])
        y_predict[i] = np.round(np.mean(ylist))
    
    print(y_predict)

main(X_train, X_test, y_train, y_test)