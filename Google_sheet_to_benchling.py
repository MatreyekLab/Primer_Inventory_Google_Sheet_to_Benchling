import pandas as pd
import codecs

fields = ["Primer_name","Sequence"]

kam = pd.read_excel ('MatreyekLab_Primer_Inventory.xlsx', sheet_name='KAM', skipinitialspace=True, usecols=fields)

smr = pd.read_excel ('MatreyekLab_Primer_Inventory.xlsx', sheet_name='SMR', skipinitialspace=True, usecols=fields)

combined = kam.append(smr)
combined.to_csv("Matreyeklab_primers_benchling.csv", index=False, encoding='utf8', header = False)