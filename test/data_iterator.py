import sys
sys.path.append("../")

import ipdb
from data import data_iterator

def test():
    for data in data_iterator.iterate_over_all_gene_profile_data():
        ipdb.set_trace()
        pass

test()
