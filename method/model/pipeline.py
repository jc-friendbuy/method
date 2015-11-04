#Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Module to create and use modeling pipelines.  The idea here is that the main modeling process
# is taken care of, and the user provides the actual implementation of the steps.

from method.model.data_set_result import DataSetResult

"""
Create a modeling pipeline with the configured runners and data.

training_runner: function(model_function, training_data)
validation_runner: function(model_function, validation_data, training_result)
data_iterator: yields(data_set_name, data_set) [where data_set is a data_set-module-created object]
model_functions: list(function(params)), where the params must be provided by the training_runner function (i.e. that one converts from the training data to the correct input variables)
pre_processing_functions: list(function(sub_data_set)) which get chain-applied to the provided data_set (they must understand the data format)
post_processing_functions list(function(training_set, validation_set, model_results))
"""

class Pipeline(object):

    def __init__(self, training_runner, validation_runner, data_iterator, model_functions, \
                    pre_processing_functions=None, post_processing_functions=None):
        assert training_runner is not None, "Must have a training runner function"
        assert validation_runner is not None, "Must have a validation runner function"
        assert data_iterator is not None, "Must have a data iterator function"
        assert model_functions is not None and len(model_functions) >= 1, \
            "Must specify a list of model functions with at least one element"

        self._training_runner = training_runner
        self._validation_runner = validation_runner
        self._data_iterator = data_iterator
        self._model_functions = model_functions
        self._pre_processing_functions = pre_processing_functions or list()
        self._post_processing_functions = post_processing_functions or list()

    def _get_next_data_set(self):
        for data_set in self._data_iterator:
            yield data_set

    def run(self):
        """
        Run (step through all data sets of) a configured pipeline.
        """
        result = list()
        while True:
            try:
                next_data_set_result = self.step()
                result.append(next_data_set_result)
            except StopIteration:
                break
        return result

    def step(self):
        """
        Step through a single data set, i.e. train and validate it.
        Throws StopIteration when no more data_set items are available.
        """
        try:
            data_set = self._get_next_data_set()
            result = DataSetResult(data_set)
            for model_function in model_functions:
                training_result = self._train(model_function, training_data)
                validation_result = self._validate(model_function, training_result, validation_data)
                result.add_model(model_function, training_result, validation_result)
            return result
        # Specifically catch and re-throw StopIteration to signal the end of the data iterator
        except StopIteration:
            raise

    def _train(self, model_function, training_data):
        """
        Run training function for a model using training set data.
        """
        return self._training_runner(model_function, training_data)

    def _validate(self, model_function, validation_data, training_result):
        """
        Validate a model using validation data and training results.
        """
        return self._validation_runner(model_function, validation_data, training_result)
