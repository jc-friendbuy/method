# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Module for dataset handling.  A dataset is composed of training and validation data.

class DataSet(object):

    def __init__(self, name, training_data, validation_data):
        self._name = name
        self._training_data = training_data
        self._validation_data = validation_data

    @property
    def name(self):
        return self._name

    @property
    def training_data(self):
        return self._training_data

    @property
    def validation_data(self):
        return self._validation_data
