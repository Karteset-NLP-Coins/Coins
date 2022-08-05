def transform_image(image):
    import torchvision.transforms as transforms
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)
    Test_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)

    ])
    new_image = Test_transform(image)
    new_image = new_image.reshape(1,3, 256, 256)
    return new_image


def run_prediction(model, image):
    import torch
    # transform the requested image
    transformed_image = transform_image(image)
    # run the image on the model
    with torch.no_grad():
        model.eval()
        output = model.forward(transformed_image)
        _, y_hat = output.max(1)
        predicted_idx = str(y_hat.item())
    return predicted_idx

