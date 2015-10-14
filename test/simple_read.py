import sys
sys.path.append("../")

from data import ccle

print ccle.get_gene_profile_view().size
