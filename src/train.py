import pandas as pd
import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load data
df = pd.read_csv('../data/student-por.csv')

# Split data into train, val nad test datsets 80-20-20 ratio
df_train_full, df_test = train_test_split(df, test_size=0.1, random_state=1)
df_train, df_val = train_test_split(df_train_full, test_size=0.11, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train["G3"].values
y_val = df_val["G3"].values
y_test = df_test["G3"].values

del df_train["G3"]
del df_val["G3"]
del df_test["G3"]

# Features to model
features = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       'Walc', 'health', 'absences']

# Transform categorical variables
train_dict = df_train[features].to_dict(orient='records')
dict_vect = DictVectorizer(sparse=False)

X_train = dict_vect.fit_transform(train_dict)

# Train the data
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)

# save the model as pickle file
with open('model_rf.pkl', 'wb') as file:
    pickle.dump(model_rf, file)
    
# Save the dict_vect transformer as pickle file
with open('dict_vect.pkl', 'wb') as file:
    pickle.dump(dict_vect, file)