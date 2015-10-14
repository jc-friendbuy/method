import sys
sys.path.append("../")
import ipdb

from data import ccle

gene_symbols = ccle.get_all_gene_symbols()
print gene_symbols.size
print gene_symbols.head

selected_symbol = gene_symbols.iloc[0].symbol
print selected_symbol

profile =  ccle.get_profile_for_gene_symbol(selected_symbol)
ipdb.set_trace()
print profile
