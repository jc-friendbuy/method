
def create():
    return dict()

def add_training_data_subset(data_set, input_data, output_data):
    _add_data_subset(data_set, "training", input_data, output_data)
    return data_set

def add_validation_data_subset(data_set, input_data, output_data):
    _add_data_subset(data_set, "validation", input_data, output_data)
    return data_set

def _add_data_subset(data_set, label, input_data, output_data):
    assert label not in data_set, "Trying to rewrite %s dataset" % label
    data_set[label] = _create_data_subset_from_input_and_output_data(input_data, output_data)

def _create_data_subset_from_input_and_output_data(input_data, output_data):
    subset = dict()
    subset["inputs"] = input_data
    subset["outputs"] = output_data
    return subset

def get_training_subset(data_set):
    return data_set["training"]

def get_validation_subset(data_set):
    return data_set["validation"]
