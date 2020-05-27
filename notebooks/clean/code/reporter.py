import pandas as pd
import numpy as np
from sklearn.metrics import classification_report,accuracy_score, f1_score, confusion_matrix, recall_score
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os.path


def giveScore(trainedInstance,X_train,y_train_target,X_test,y_test_target, print_report=False, labels=None):
    predictions_test = trainedInstance.predict(X_test)
    predictions_train = trainedInstance.predict(X_train)
    if print_report:
        print("Cross Validation Score..")
        print(classification_report(y_test_target, predictions_test, target_names=labels))
        print("Training Score..")
        print(classification_report(y_train_target, predictions_train,target_names=labels))
    print('Acc:{}; f1:{}; recall:{};'.format(
        accuracy_score(predictions_test,y_test_target),
        f1_score(predictions_test,y_test_target,average='micro'),
        recall_score(predictions_test,y_test_target,average='micro')))
    print("Confusion Matrix on Cross Validation set")
    return pd.DataFrame(confusion_matrix(y_test_target, predictions_test),columns=labels,index=labels).rename_axis("Truth").rename_axis("Pred", axis="columns")

def giveWordCloud(data_preprocess,stopwords):
    plt.figure(figsize=(20,10))

    text = data_preprocess[:,1]

    cloud_toxic = WordCloud(
        stopwords=stopwords,
        background_color='black',
        collocations=False,
        width=2500,
        height=1800
    ).generate(" ".join(text))

    plt.axis('off')
    plt.title("Frecuencia de palabras en Description",fontsize=10)
    plt.imshow(cloud_toxic);
    
def writePathologicalCases(path,truth,pred,X_test,y_test,predictions):
    truth_filter = np.array(y_test == truth).reshape(-1,)
    pred_filter = np.array(predictions == pred)

    aux = pd.DataFrame(np.array(X_test)[truth_filter & pred_filter],columns=['Title','Description','Truth'])
    aux['Pred'] = pred
    
    header = not (os.path.exists(path)) #if no file then header, else header should be already there.
    
    aux.to_csv(path, mode='a', header=header)
    return aux