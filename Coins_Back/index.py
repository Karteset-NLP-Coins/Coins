import flask
import helpers
import torch
from flask import jsonify, request
from flask_cors import CORS


MODEL_PATH_1 = './models/model1'
MODEL_PATH_2 = './models/model2'
MODEL_PATH_3 = './models/model3'
MODEL_PATH_4 = './models/model4'
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# few things are missing:
# 1. the model, we need to save the model as torch.save(model)
# 2. the transformation function, we need to convert the image to the size of the images it was trained on
# size of the image transformation: 256 X 256


@app.route('/api/predict-leaves-or-thorns', methods=['POST'])
def predict_first():
    if (request.method == "POST"):
        # load the model
        # model = torch.load(MODEL_PATH_1)
        # set eval mode so that the model will not learn
        # model.eval()
        # get the file from request
        # image = request.form['file']
        # run prediction
        # prediction = helpers.run_prediction(model, image)
        # return the prediction
        # return jsonify(result=prediction)
        return jsonify(result='dog')


@app.route('/predict-2', methods=['POST'])
def predict_second():
    if (request.method == "POST"):
        # load the model
        model = torch.load(MODEL_PATH_2)
        # set eval mode so that the model will not learn
        model.eval()
        # get the file from request
        image = request.form['file']
        # run prediction
        prediction = helpers.run_prediction(model, image)
        # return the prediction
        return jsonify(result=prediction)


if __name__ == '__main__':
    app.run(port=3500)
