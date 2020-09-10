import numpy as np
import pandas as pd 
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_scorec
from sklearn.model_selection import train_test_split

train_df = pd.read_csv("../dataset/mnist_train.csv")
test_df = pd.read_csv("../dataset/mnist_test.csv")

train_data = train_df.values

#8:2 -> 학습데이터 : 검증데이터
x_train, y_train, x_test, y_test = train_test_split(train_data[0:,1:], train_data[0:, 0], test_size=0.2, random_state=0 )


#randomforest classifier
model1 = RandomForestClassifier(n_estimators = 500)
rdc = model1.fit(x_train, y_train)
output1 = rdc.predict(x_test)

#GradientBoostingClassfier

#