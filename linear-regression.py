import numpy as np
import glob
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn import preprocessing
from numpy import mean
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    malware = glob.glob("./images" + '/malware/*.png')
    goodware = glob.glob("./images" + '/goodware/*.png')

    x = []
    y = []
    for path in malware:
        img = np.asarray(Image.open(path).resize((8,8))).flatten()
        x.append(img)
        y.append(0)

    for path in goodware:
        img = np.asarray(Image.open(path).resize((8,8))).flatten()
        x.append(img)
        y.append(1)

    x = np.array(x)
    y = np.array(y)

    scaler = preprocessing.StandardScaler().fit(x)
    scaler.mean_
    scaler.scale_

    x_train,x_test,y_train,y_test, indices_train, indices_test=train_test_split(scaler.transform(x), y, range(x.shape[0]), test_size=0.2)

    clf = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    
    print("Accuracy Score: {0:.3f}".format(accuracy_score(y_test, y_pred)))
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))





if __name__ == "__main__":
    main()
