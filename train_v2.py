import numpy as np
import pickle, random
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras import optimizers

# 13264 - 829 - 3316

with open("bn_encodings_lo.pkl", "rb") as f:
    bn_data = pickle.load(f)
with open("en_encodings_lo.pkl", "rb") as g:
    en_data = pickle.load(g)
data = bn_data[:6632] + en_data[:6632]

train = open("train.txt", "w", encoding="utf-8")
data = np.array(data, dtype=int)

print(data)

target = []
for x in range(6632):
    target.append([0])
for y in range(6632):
    target.append([1])
target = np.array(target, dtype=int)

combined = list(zip(data, target))
random.Random(10).shuffle(combined)

data[:], target[:] = zip(*combined)

model = Sequential()
model.add(Embedding(36, 15, input_length=15))
model.add(LSTM(15, return_sequences=True))
model.add(LSTM(17, return_sequences=True))
model.add(LSTM(40))
model.add(Dense(1, activation='sigmoid'))
adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(data, target, epochs=500, batch_size=1658)
model.save('model_P_15_17_40_1.h5')
print(model.summary())
predicts = open("pred.txt", "w", encoding="utf-8")

preds = []
for pred in model.predict(data):
    preds.append(round(pred[0]))

for x in range(1000):
    predicts.write(str(target[x]) + "\t" + str(preds[x]) + "\n")
predicts.close()

# ACCURACY
plt.plot(history.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.show()

# LOSS
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()
