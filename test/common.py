__FLOAT64_DIFFERENCE_EPSILON = 0.01

def assert_values_are_within_epsilon_distance(x, y):
    assert abs(x - y) <= __FLOAT64_DIFFERENCE_EPSILON
