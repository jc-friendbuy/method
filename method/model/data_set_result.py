
from method.data.data_set import DataSet

class DataSetResult(object):

    def __init__(self, data_set):
        assert isinstance(data_set, DataSet)
        self._data_set = data_set
        self._model_data = dict()

    @property
    def data_set(self):
        return self._data_set

    def add_model(self, model_function, training_result, validation_result):
        assert model_function.__name__ not in self._model_data
        self._model_data[model_function] = (training_result, validation_result)

    def get_model_results(self, model_function):
        return self._model_data[model_function]

    def iteritems(self):
        for key, value in self._model_data.iteritems():
            yield key, value
