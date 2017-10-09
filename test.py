from NN import NN
import numpy as np
import json
model  = None

def test(X,y):
    global model 
    accuracies = []
    costs = []
    for i in range(0,X.shape[0],64):
        end = min(i+64,X.shape[0])
        model.test(X[i:end],y[i:end],accuracies,cost)
    
    accuracies = np.array(accuracies)
    costs = np.array(costs)
    print("Accuracy : ",np.mean(accuracies))
    print("Cost : ",np.sum(costs))
    
if __name__ == "__main__":
    global model
    model = NN.load("model1.pkl")
    data = json.load(open("data/data.json","rb"))
    
    validX = np.array(data['validX'])
    validY = np.array(data['validY'],dtype=np.int32)
    
    testX = np.array(data['testX'])
    testY = np.array(data['testY'],dtype=np.int32)
    
    test(validX,validY)