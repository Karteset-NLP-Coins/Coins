import flask
import helpers
import torch
import torchvision
from flask import jsonify, request
from flask_cors import CORS
from PIL import Image

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

crown_model = None
emperor_model = None

crown_coding = {0: 'radiate', 1: 'laureate'}
emperor_coding = {'nerva': 0, 'hadrian': 1, 'titus': 2, 'trajan': 3, 'antoninus': 4, 'lucius': 5, 'vespasian': 6, 'domitian': 7, 'marcus': 8}


@app.route('/api/predict-leaves-or-thorns', methods=['POST'])
def predict_first():
    if (request.method == "POST"):
        # get the file from request
        image = request.files["image"]
        real_img = Image.open(image.stream)
        # run prediction
        prediction = helpers.run_prediction(crown_model, real_img)
        prediction_real = crown_coding[int(prediction)]
        return jsonify(result=prediction_real)


@app.route('/api/predict_emperor', methods=['POST'])
def predict_second():
    if (request.method == "POST"):
        # get the file from request
        image = request.files["image"]
        real_img = Image.open(image.stream)
        # run prediction
        prediction = helpers.run_prediction(emperor_model, real_img)
        prediction_real = emperor_coding[int(prediction)]
        return jsonify(result=prediction_real)


def initialize_models():
    MODEL_PATH_1 = './models/crown_model_f.pth'
    MODEL_PATH_2 = './models/crown_model_f.pth'
    MODEL_PATH_3 = './models/model3'
    MODEL_PATH_4 = './models/model4'
    # load the models
    # crown model
    global crown_model
    crown_model = torchvision.models.resnet18() 
    in_featuers = crown_model.fc.in_features
    crown_model.fc = torch.nn.Linear(in_featuers, 2)
    state_dict = torch.load(MODEL_PATH_1, map_location="cpu")
    crown_model.load_state_dict(state_dict)
    
    # emperor model
    # global emperor_model
    # emperor_model = torchvision.models.resnet18() 
    # in_featuers = emperor_model.fc.in_features
    # emperor_model.fc = torch.nn.Linear(in_featuers, 9)
    # state_dict = torch.load(MODEL_PATH_2, map_location="cpu")
    # emperor_model.load_state_dict(state_dict)

if __name__ == '__main__':
    initialize_models()
    app.run(host='localhost',port=3500)
