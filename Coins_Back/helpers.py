def transform_image(image):
    return "new image"


def run_prediction(model, image):
    # transform the requested image
    transformed_image = transform_image(image)
    # run the image on the model
    prediction = model.predict(transformed_image)
    return prediction
