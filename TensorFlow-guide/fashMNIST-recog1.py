#tensorflow and tf.keras first tutorial project
#anthony bennett | started 16/08/2019
#https://www.tensorflow.org/tutorials/keras/basic_classification

#imports
import tensorflow as tf
from tensorflow import keras

#helper libs
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

#import our dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(test_images[0])