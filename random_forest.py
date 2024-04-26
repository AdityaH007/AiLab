import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.common import random_state
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler,MinMaxScaler


from matplotlib import rc_params, rcParams
import warnings

warnings.filterwarnings("ignore")

rcParams["figure.figsize"]=10,6
np.random.seed(42)

data=pd.read_csv("./pima.csv")

x= data.drop("class",axis=1)
y=data["class"]

scaler=StandardScaler()
X_scaled=scaler.fit_transform(x)

X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,stratify=y,test_size=0.10,random_state=4)

classifier = RandomForestClassifier(n_estimators=100)

classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

print("accuracy_score:",accuracy_score(y_test,y_pred))

feature_importances_df=pd.DataFrame(
        {"feature":list(x.columns),"importance":classifier.feature_importances_}
        ).sort_values("importance",ascending=False)

sns.barplot(x=feature_importances_df.feature,y=feature_importances_df.importance)
plt.xlabel("Feature Importance Score")
plt.ylabel("Features")
plt.title("Visualizing Important features")
plt.xticks(
        rotation=45,horizontalalignment="right",fontweight="light",fontsize="x-large")
plt.show()

X = data.drop(["class", "triceps_skinfold_thickness"], axis=1)
y = data["class"]

# standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# split into train and test set
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, stratify=y, test_size=0.10, random_state=42
)

clf = RandomForestClassifier(n_estimators=100)

# Train the model using the training sets
clf.fit(X_train, y_train)

# prediction on test set
y_pred = clf.predict(X_test)

# Calculate Model Accuracy,
print("Accuracy:", accuracy_score(y_test, y_pred))

