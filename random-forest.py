import numpy as np
import glob
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from numpy import mean
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time

def main():
    begin = time.time()
    malware = glob.glob("./processed-images" + '/malware/*.png')
    goodware = glob.glob("./processed-images" + '/goodware/*.png')

    x = []
    y = []
    for path in malware:
        img = np.asarray(Image.open(path)).flatten()
        x.append(img)
        y.append(0)

    for path in goodware:
        img = np.asarray(Image.open(path)).flatten()
        x.append(img)
        y.append(1)

    x = np.array(x)
    y = np.array(y)

    scaler = preprocessing.StandardScaler().fit(x)
    scaler.mean_
    scaler.scale_

    x_train,x_test,y_train,y_test, indices_train, indices_test=train_test_split(scaler.transform(x), y, range(x.shape[0]), test_size=0.2)

    clf = RandomForestClassifier(n_jobs=2, random_state=0)

    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    end = time.time()

    print("Accuracy Score: {0:.3f}".format(accuracy_score(y_test, y_pred)))
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print("Total runtime: {0:.3f}s".format(end-begin))

if __name__ == "__main__":
    main()
