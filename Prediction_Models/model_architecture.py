# Python codes for explaining the implementation of our prediction models described in Section 5
import tensorflow as tf
from tensorflow.keras.layers import Input, BatchNormalization, Dropout, Dense, LSTM, GRU, RNN
from tensorflow.keras import Sequential, Model
from tensorflow.keras.regularizers import l2

def creatModel():
    global model
    model = Sequential([
        Input(shape=(MAX_UTT, MAX_SEQ)), # MAX_UTT: MAX utterance per session, MAX_SEQ: MAX sequence per utterance time length
        LSTM(units=128, return_sequences=True), # first layer of LSTM
        LSTM(units=128, return_sequences=False), # second layer of LSTM, we set 'return_sequences' to false since only the last hidden state will be used.
        Dense(units=64, kernel_initializer='glorot_uniform', activation='relu'),
        Dense(units=1, activation='sigmoid', kernel_regularizer=l2(0.001)) # output unit
    ])
    model.build(input_shape=(None, MAX_UTT, MAX_SEQ))
    model.compile(loss='mean_absolute_error', optimizer=tf.optimizers.Adam(lr=0.001))
    print(model.summary())

creatModel()