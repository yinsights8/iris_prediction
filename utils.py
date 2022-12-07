import pickle
import config
import os


model_folder_path = config.Model_Folder_Path

if not os.path.exists(model_folder_path):
    os.mkdir(model_folder_path)

def predictions(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):

    clf_model = pickle.load(open(f"{model_folder_path}/model.pkl", "rb"))

    predict = clf_model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    print(f"Predictios are:- {predict[0]}")
    pred = predict[0]

    if pred == 0:
        return "Iris-setosa"

    elif pred == 1:
        return "Iris-versicolor"

    else:
        return "Iris-virginica"


# predictions(1,2,3,4)