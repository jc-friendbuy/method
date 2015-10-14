"""
Create a modeling pipeline with the configured runners and data.

training_runner: function(model_function, training_data)
validation_runner: function(model_function, validation_data, training_result)
data_iterator: yields(data_set_name, data_set) [where data_set is a data_set-module-created object]
model_functions: list(function(params)), where the params must be provided by the training_runner function (i.e. that one converts from the training data to the correct input variables)
pre_processing_functions: list(function(sub_data_set)) which get chain-applied to the provided data_set (they must understand the data format)
post_processing_functions list(function(training_set, validation_set, model_results))
"""
def create(training_runner, validation_runner, data_iterator, model_functions, pre_processing_functions=None, post_processing_functions=None):
    assert training_runner is not None, "Must have a training runner function"
    assert validation_runner is not None, "Must have a validation runner function"
    assert data_iterator is not None, "Must have a data iterator function"
    assert model_functions is not None and len(model_functions) >= 1,
        "Must specify a list of model functions with at least one element"

    pipeline = dict()
    pipeline["training_runner"] = training_runner
    pipeline["validation_runner"] = validation_runner
    pipeline["data_iterator"] = data_iterator
    pipeline["model_functions"] = model_functions
    pipeline["pre_processing_functions"] = pre_processing_functions or list()
    pipeline["post_processing_functions"] = post_processing_functions or list()
    return pipeline

"""
Run (i.e. train and validate) a configured pipeline.
"""
def run(pipeline):
    all_results = dict()

    training_runner = pipeline["training_runner"]
    validation_runner = pipeline["validation_runner"]
    data_iterator = pipeline["data_iterator"]
    model_functions = pipeline["model_functions"]
    pre_processing_functions = pipeline["pre_processing_functions"]
    post_processing_functions = pipeline["post_processing_functions"]

    for data_set_name, data_set in data_iterator():
        data_set_result = dict()
        data_set_result[data_set] = data_set

        training_data = _pre_process(s.get_training_subset(data_set), pre_processing_functions)
        data_set_result["training_data"] = training_data
        validation_data = _pre_process(ds.get_validation_subset(data_set), pre_processing_functions)
        data_set_result["validation_data"] = validation_data

        all_model_results = dict()
        for model_function in model_functions:
            model_result = dict()

            training_result = _train(training_runner, model_function, training_data)
            model_result["training"] = training_result

            validation_result = _validate(validation_runner, model_function, training_result, validation_data)
            model_result["validation"] = validation_result

            post_processing_result = _post_process(training_data, validation_data, model_result, post_processing_functions)
            model_result["post_processing"] = post_processing_result

            all_model_results[model_function.__name__] = model_result

        data_set_result["models"] = all_model_results
        all_results[data_set_name] = data_set_result

    return all_results

"""
Run training function for a model using training set data.
"""
def _train(training_runner, model_function, training_data):
    return training_runner(model_function, training_data)

"""
Validate a model using validation data and training results.
"""
def _validate(validation_runner, model_function, validation_data, training_result):
    return validation_runner(model_function, validation_data, training_result)

"""
Chain-apply all pre-processing functions on the given data and return the result
(function application)
"""
def _pre_process(data, pre_processing_functions):
    assert pre_processing_functions is not None, "Cannot apply non-existent pre-processing functions"

    processed_data = data
    for pre_processing_function in pre_processing_functions:
        processed_data = pre_processing_function(processed_data)
    return processed_data

"""
Run all post-processing functions on the given data and return the result.
"""
def _post_process(training_data, validation_data, model_result, post_processing_functions):
    assert post_processing_functions is not None,
        "Cannot apply non-existent post-processing functions"

    results = dict()
    for post_processing_function in post_processing_functions:
        results[post_processing_function.__name__] = \
            post_processing_function(training_data, validation_data, model_result)
    return results
