from flask import Flask, jsonify, request, redirect, render_template
import utils

app = Flask(__name__)

@app.route("/")
def Home():
    # print("hello flask")
    return render_template("index.html")



@app.route("/predict", methods=["GET","POST"])
def predictions():
    print("loading..")
    data = request.form

    if request.method == "POST":
        x1 = float(data['SepalLengthCm'])
        x2 = float(data['SepalWidthCm'])
        x3 = float(data['PetalLengthCm'])
        x4 = float(data['PetalWidthCm'])

        predict = utils.predictions(x1,x2,x3,x4)

        return render_template("result.html", result = predict)

        # return jsonify({"Predictions are :- ": f"{predict}"})
    else:
        return jsonify({"Message": "NO Predictions"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)