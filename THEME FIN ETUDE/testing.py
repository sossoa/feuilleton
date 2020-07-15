# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:56:03 2020

@author: aitam
"""

import tensorflow as tf

#choisir une image a classer 

x_test='test/test.png'



new_model = tf.keras.models.load_model('testing.model')
predictions = new_model.predict(x_test)
print(predictions)