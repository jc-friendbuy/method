# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.

import sys
sys.path.append("../")

from data import ccle

print ccle.get_gene_profile_view().size
