
from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)
model = pickle.load(open('REDWINE.pkl', 'rb'))

    
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = MinMaxScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        #fixed_acidity = float(request.form["fixed_acidity"])
        volatile_acidity = float(request.form["volatile_acidity"])
        citric_acid = float(request.form["citric_acid"])
        #residualsugar = float(request.form["residualsugar"])
        #chlorides = float(request.form["chlorides"])
        #free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
        #density = float(request.form["density"])
        #pH = float(request.form["pH"])
        sulphates = float(request.form["sulphates"])
        alcohol = float(request.form["alcohol"])

        prediction = model.predict([[volatile_acidity,  citric_acid, total_sulfur_dioxide, sulphates, alcohol]])
        

        if prediction==1.0:
            quality=("good")
        else:
            quality=("bad")
        return render_template('index.html',prediction_text="The Quality of wine is {}".format(quality))


        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()