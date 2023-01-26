from numpy import loadtxt
import tensorflow
from keras.models import load_model

CUTOFF = 0.7

def runModel(mainDIR):
    cnn = load_model('vgg16Run.h5')
    prediction = cnn.predict(mainDIR)
    print(prediction)

    for i in prediction:
        if(i > CUTOFF):
            species = prediction.get
        
