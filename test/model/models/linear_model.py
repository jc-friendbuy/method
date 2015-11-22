# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.

import sys
sys.path.append("../")

import ipdb
import time
import matplotlib.pyplot as plt
from ccle.data import ccle
from model.models import linear

_MODELS_TO_RUN = 10

def run():
    gene_symbols = ccle.get_all_gene_symbols()[:_MODELS_TO_RUN]
    print "Running model on %s genes." % len(gene_symbols)

    profile_iterator = (ccle.get_profile_for_gene_symbol(symbol) for symbol in gene_symbols)

    def lin_model(profile):
        x = profile["snpCopyNumber2Log2"].reshape(len(profile), 1)
        y = profile["quantileNormalizedRMAExpression"].reshape(len(profile), 1)

        plt.scatter(x, y, color='black')
        plt.plot(x, linear(x, y), color='blue', linewidth=3)
        plt.savefig(get_file_name("linear"))
        plt.clf()


    current = 0
    for profile in profile_iterator:
        if current == _MODELS_TO_RUN:
            break
        current += 1
        lin_model(profile)

def get_file_name(model_type):
    return "/Users/jc/Desktop/dumps/%s/%s.jpg" % (model_type, str(time.time()).replace(".", ""))

result = run()
