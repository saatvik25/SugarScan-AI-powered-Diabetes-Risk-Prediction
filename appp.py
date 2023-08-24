# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)
# with open('model.pkl', 'rb') as file:
#     model = pickle.load(file)


# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/dignosis',methods = ['POST','GET'])

# def dignosis():

    
#     gender = int(request.form.get('gender'))
#     age = float(request.form.get('age'))
#     hypertension = int(request.form.get('hypertension'))
#     heart_disease = int(request.form.get('heart_disease'))
#     smoking_history = float(request.form.get('smoking_history'))
#     bmi = float(request.form.get('bmi'))
#     HbA1c_level = float(request.form.get('HbA1c_level'))
#     blood_glucose_level = float(request.form.get('blood_glucose_level'))


#     outcome = model.predict([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
#     diagnosis_result = "Yes , you  have diabtes please concern Doctor" if outcome[0] == 1 else "No,you don't have diabtes"

# # gender	age	hypertension	heart_disease	smoking_history	bmi	HbA1c_level	blood_glucose_level	diabetes

#     # return render_template('index.html',dignosis = outcome)
#     return render_template('index.html', dignosis=str(diagnosis_result))





# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn import preprocessing

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Preprocess function
def preprocess_inputs(data):
    label_encoder = preprocessing.LabelEncoder()
    data['gender'] = label_encoder.fit_transform(data['gender'])
    data['smoking_history'] = label_encoder.fit_transform(data['smoking_history'])

    data['hypertension'] = data['hypertension'].apply(lambda x: 1 if x.lower() == "yes" else 0)
    data['heart_disease'] = data['heart_disease'].apply(lambda x: 1 if x.lower() == "yes" else 0)
    
    return data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form.get('gender')
    age = float(request.form.get('age'))
    hypertension = request.form.get('hypertension')
    heart_disease = request.form.get('heart_disease')
    smoking_history = request.form.get('smoking_history')
    bmi = float(request.form.get('bmi'))
    HbA1c_level = float(request.form.get('HbA1c_level'))
    blood_glucose_level = float(request.form.get('blood_glucose_level'))
    
    data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'smoking_history': [smoking_history],
        'bmi': [bmi],
        'HbA1c_level': [HbA1c_level],
        'blood_glucose_level': [blood_glucose_level]
    })
    
    data = preprocess_inputs(data)
    prediction = model.predict(data)
    result = "Yes" if prediction[0] == 1 else "No"
    
    return render_template("index.html", prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
