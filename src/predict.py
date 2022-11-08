import pickle
import sklearn

# define model and transformer paths
model_file = 'model_rf.pkl'
dv_file = 'dict_vect.pkl'

#Provide the input
student = {'school': 'MS',
 'sex': 'F',
 'age': 18,
 'address': 'U',
 'famsize': 'GT3',
 'Pstatus': 'T',
 'Medu': 1,
 'Fedu': 2,
 'Mjob': 'other',
 'Fjob': 'other',
 'reason': 'course',
 'guardian': 'father',
 'traveltime': 1,
 'studytime': 2,
 'failures': 1,
 'schoolsup': 'no',
 'famsup': 'yes',
 'paid': 'no',
 'activities': 'yes',
 'nursery': 'yes',
 'higher': 'yes',
 'internet': 'yes',
 'romantic': 'yes',
 'famrel': 3,
 'freetime': 4,
 'goout': 4,
 'Dalc': 2,
 'Walc': 3,
 'health': 5,
 'absences': 9}

# load the model file
with open(model_file, 'rb') as f:
    model = pickle.load(f)
    
# load the transformer
with open(dv_file, 'rb') as f:
    dict_vect = pickle.load(f)

# Transform the X values
X = dict_vect.transform(client)

# Predict the instance 
prediction = model.predict(X)
print(f"Predicted grade of the student: {prediction}")