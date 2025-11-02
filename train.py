import pandas as pd 
import joblib
from sklearn.model_selection  import train_test_split 
from sklearn import svm 
from sklearn import metrics 
import os


iris = pd.read_csv("data/data.csv")
iris = iris.sample(frac=1, random_state=None).reset_index(drop=True)

train, test = train_test_split(iris, test_size=0.3, random_state=42) 
train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] 
train_y = train.Species 
test_X = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] 
test_y = test.Species 


model = svm.SVC()
model.fit(train_X, train_y)


filename = 'application/artifacts/svm_iris_model.joblib'
os.makedirs(os.path.dirname(filename), exist_ok=True)
joblib.dump(model, filename)
print(f"\nModel successfully saved as: {filename}")


# prediction = model.predict(test_X)
# print('The accuracy of the SVM is: ', metrics.accuracy_score(prediction, test_y))