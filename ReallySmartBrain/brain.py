# Use the tensorflow venv

from imageai.Prediction import ImagePrediction #ImageAI library
import os # for the file paths
execution_path=os.getcwd() # get current working directory, from the command prompt. where u're at.

prediction = ImagePrediction()
prediction.setModelTypeAsResNet() # decide what model u want to use (they're the same but more or less 
                                      # accurate and slower or faster bc of file size). u have to download it
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5")) # set the path to the model file 
                                                                         # u downloaded
prediction.loadModel() # load the model

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
        # accuracy                                                                          # how many predictions we want it to give us
for eachPrediction, eachProbability in zip(predictions, probabilities): # zip the predictions & probabilities
    print(eachPrediction , " : " , eachProbability) # print what we want