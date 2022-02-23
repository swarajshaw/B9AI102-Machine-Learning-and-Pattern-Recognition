import pandas as pd
from sklearn import tree
from sklearn import metrics

df = pd.read_csv(
    "C:/Users/Swaraj/PycharmProjects/B9AI102-Machine Learning and Pattern Recognition/Datasets/winequality-red.csv")
# df.head()
quality_mapping = {
    3: 0,
    4: 1,
    5: 2,
    6: 3,
    7: 4,
    8: 5}
# you can use the map function of pandas with
# any dictionary to convert the values in a given
# column to values in the dictionary
df.loc[:, "quality"] = df.quality.map(quality_mapping)
df = df.sample(frac=1).reset_index(drop=True)
df_train = df.head(1000)
df_test = df.tail(599)

# initialize decision tree classifier

clf = tree.DecisionTreeClassifier(max_depth=3)
cols = ['fixed acidity',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol']
# train model
clf.fit(df_train[cols], df_train.quality)
# generate predictions on training set
train_predictions = clf.predict(df_train[cols])
# generate predictions on test set
test_predictions = clf.predict(df_test[cols])
# calc prediction on training dataset
train_accuracy = metrics.accuracy_score(df_train.quality, train_predictions)
# calc prediction on test dataset
test_accuracy = metrics.accuracy_score(df_test.quality, test_predictions)
