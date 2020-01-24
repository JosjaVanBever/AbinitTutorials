# Import abipy modules
from abipy import abilab
from abipy.abilab import Structure
import abipy.data as abidata

# get structure from file
structure = Structure.from_file("opto_GSR.nc")

# TEST: visualize structure
# print(structure)
#structure.visualize("vesta")
print(structure.to_abivars())
print(structure.abi_string)
#structure.plot()

# get structure form MP
si2_mp = Structure.from_mpid("mp-149")

# generate differences
dfs = abilab.dataframes_from_structures([structure, si2_mp], index=["calc", "MP"])
#print(dfs.lattice)

# print structure to cif file
#print(structure.convert(fmt="cif"))
#structure.to(filename="Si.cif")

# get info about structure
print(structure.reciprocal_lattice.rsplit(' '))

print(structure.to_abivars()['rprim'][0])
