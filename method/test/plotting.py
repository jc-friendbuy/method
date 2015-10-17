# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.

import sys
sys.path.append("../")

import seaborn as sns
from data import ccle

profile_view = ccle.get_gene_profile_view()
sns.pairplot(profile_view, x_vars=["snpCopyNumber2Log2"], y_vars=["quantileNormalizedRMAExpression"])
sns.plt.show()
