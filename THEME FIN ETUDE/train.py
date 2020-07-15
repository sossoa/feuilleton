# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:42:43 2020

@author: aitam
"""


import numpy as np
import pandas as pd
import tensorflow.keras as keras

import tensorflow as tf


#df_sans = pd.read_csv('sans_feuilleton.csv ', header =None)
#df_avec = pd.read_csv('avec_feuilleton.csv ', header =None)
df_sans=np.genfromtxt('sans_feuilleton.csv',delimiter=',',dtype=None)
df_avec=np.genfromtxt('avec_feuilleton.csv',delimiter=',',dtype=None)


width = 29
height = 20
nbr=int(df_avec.shape[0]/2)
nbr=2




x_train= np.concatenate((df_avec[:nbr, :width*height],df_sans[:nbr, :width*height]),axis=0)
y_train= np.concatenate((df_avec[:nbr, width*height:],df_sans[:nbr, width*height:]),axis=0)
x_test= np.concatenate((df_avec[nbr:, :width*height],df_sans[nbr:, :width*height]),axis=0)
y_test= np.concatenate((df_avec[nbr:, width*height:],df_sans[nbr:,width*height :]),axis=0)




# y_train= df_avec.iloc[:nbr, width*height:].append(df_sans.iloc[:nbr, width*height:])
# x_test= df_avec.iloc[nbr:, :width*height].append(df_sans.iloc[nbr:, :width*height])
# y_test= df_avec.iloc[nbr:, width*height:].append(df_sans.iloc[nbr:,width*height :])


# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)
# y_train = tf.keras.utils.normalize(y_train, axis=1)
# y_test = tf.keras.utils.normalize(y_test, axis=1)




model = keras.Sequential([
    keras.layers.Dense(width*height, activation='relu', name="layer_in"),
    keras.layers.Dense(width*height, activation='relu', name="layer_hidd"),
    keras.layers.Dense(2, activation='softmax', name="layer_out")
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])


model.fit(x_train, y_train, epochs=3)

# evaluer le model avec les donnee test 
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)

model.save('testing.model')