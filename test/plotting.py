import sys
sys.path.append("../")

import seaborn as sns
from data import ccle

profile_view = ccle.get_gene_profile_view()
sns.pairplot(profile_view, x_vars=["snpCopyNumber2Log2"], y_vars=["quantileNormalizedRMAExpression"])
sns.plt.show()
