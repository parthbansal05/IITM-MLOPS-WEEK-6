import pandas as pd 
import joblib

iris = pd.read_csv("data.csv")
print(iris.head())

model = joblib.load('svm_iris_model.joblib')

from sklearn.model_selection  import train_test_split
from sklearn import svm 
from sklearn import metrics 

train, test = train_test_split(iris, test_size=0.3, random_state=42)

train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
train_y = train.Species 

test_X = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] 
test_y = test.Species

model.fit(train_X, train_y)

prediction = model.predict(test_X)
print('The accuracy of the SVM is: ', metrics.accuracy_score(prediction, test_y))


filename = 'svm_iris_model.joblib'
joblib.dump(model, filename)
print(f"\nModel successfully saved as: {filename}")
