from keras.models import load_model
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import encoder as en
import numpy as np


def roundup(value):
    if value <= 0.95:
        return 0
    else:
        return 1

model = load_model('model_P_15_15_40_1.h5')

words = []
for line in open("new_test_data.txt", encoding="utf-8").read().split("\n")[:1400]:
    words.append(line.lower().strip())

outputs = []
a = open("fuzzy_output.txt", "w", encoding="utf-8")
for word in words:
    enc = np.array([en.encode(word)])
    prediction = model.predict(enc)[0]
    outputs.append(int(roundup(prediction[0])))
#    outputs.append(int(round(prediction[0])))
#    outputs.append(prediction[0])

for index in range(1400):
    a.write(words[index] + "\t" + str(outputs[index]) + "\n")
    # a.write(str(outputs[index]) + "\n")

labels = [0] * 700 + [1] * 700

y_TRUE = np.array(labels)
y_PRED = np.array(outputs)

accuracy = accuracy_score(y_TRUE, y_PRED)
precision = precision_score(y_TRUE, y_PRED)
recall = recall_score(y_TRUE, y_PRED)
f_score = f1_score(y_TRUE, y_PRED, average='macro')

print("accuracy = ", accuracy)
print("precision = ", precision)
print("recall = ", recall)
print("f1-score = ", f_score)
