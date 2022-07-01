from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('classifier1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    Nitrogen = (request.form.get('Nitrogen'))
    Potassium = (request.form.get('Potassium'))
    Phosphorous = (request.form.get('Phosphorous'))

    # prediction
    result = model.predict(np.array([[Nitrogen,Potassium,Phosphorous]]))
    if result[0] == 0:
        result = 'TEN-TWENTY SIX-TWENTY SIX'
    elif result[0] == 1:
        result = 'Fourteen-Thirty Five-Fourteen'
    elif result[0] == 2:
        result = 'Seventeen-Seventeen-Seventeen'
    elif result[0] == 3:
        result = 'TWENTY-TWENTY'
    elif result[0] == 4:
        result = 'TWENTY EIGHT-TWENTY EIGHT'
    elif result[0] == 5:
        result = 'DAP'
    else:
        result = 'UREA'




    return render_template('index.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)