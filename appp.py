from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dignosis',methods = ['POST','GET'])

def dignosis():

    
    gender = int(request.form.get('gender'))
    age = float(request.form.get('age'))
    hypertension = int(request.form.get('hypertension'))
    heart_disease = int(request.form.get('heart_disease'))
    smoking_history = float(request.form.get('smoking_history'))
    bmi = float(request.form.get('bmi'))
    HbA1c_level = float(request.form.get('HbA1c_level'))
    blood_glucose_level = float(request.form.get('blood_glucose_level'))


    outcome = model.predict([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
    diagnosis_result = "Yes , you  have diabtes please concern Doctor" if outcome[0] == 1 else "No,you don't have diabtes"

# gender	age	hypertension	heart_disease	smoking_history	bmi	HbA1c_level	blood_glucose_level	diabetes

    # return render_template('index.html',dignosis = outcome)
    return render_template('index.html', dignosis=str(diagnosis_result))





if __name__ == '__main__':
    app.run(debug=True)




    