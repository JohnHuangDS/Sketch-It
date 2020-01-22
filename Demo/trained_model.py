import glob
from keras.models import model_from_json
from settings import Settings

class Trained_Model:
    """Class for loading and using a trained model"""
    def __init__(self):
        """Initialize attributes"""

        #initialize model
        self.settings = Settings()
        self.cnn_model = self._load_cnn_model()

    def _load_cnn_model(self):

        #get path names
        path = r'trained-models/'

        #load model json
        model_json = glob.glob(path +'/*.json')
        json_file = open(model_json[0])
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        #load weights
        model_weights = glob.glob(path+'/*.h5')
        loaded_model.load_weights(model_weights[0])
        loaded_model.compile(loss = 'sparse_categorical_crossentropy',
            optimizer = 'Adam',
            metrics = ['accuracy']
            )

        return(loaded_model)

    def predict_image(self, frame):
        """Returns a string of the predicted class"""

        #defining img size for prediction using keras
        img_rows = 28
        img_cols = 28

        #creating the right img size for keras
        test_img = frame.reshape(1, img_rows, img_cols, 1)

        #predict class
        prediction = self.cnn_model.predict_classes(test_img)[0]
        predicted_class = (self.settings.categories[prediction])
        return(predicted_class)