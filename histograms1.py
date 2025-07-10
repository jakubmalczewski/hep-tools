import uproot as up
import pandas as pd
from matplotlib import pyplot as plt
import mplhep as hep

hep.style.use("LHCb2")
plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.dpi"] = 200
plt.rcParams["font.size"] = 12

output_dir = "output/"

variables = [
    "Lc_IP_OWNPV",
    "Lc_IPCHI2_OWNPV",
    "Lc_FD_OWNPV",
    "Lc_FDCHI2_OWNPV", 
    "Lc_ENDVERTEX_CHI2",
    "Lc_PT",
    "Lc_M"
]

# For many small files, it is convenient to access them as Pandas DataFrames.
# Use filter_name=variables to load only needed variables
mc_batches = []
for batch in up.iterate(["Lc2pemu_MC_MagDown.root", "Lc2pemu_MC_MagUp.root"], filter_name=variables, library="pd"):
    mc_batches.append(batch) # batch is a DataFrame object

df_mc = pd.concat(mc_batches)

# For big files it is much faster to access them via uproot TTree, as all the data is NOT loaded into the memory at once. 
tree_data = up.open("Lc2pemu_Data.root:DecayTree") 

for var in variables:
    plt.figure()
    h, bins = np.histogram(tree_data[var], bins=50)
    hep.histplot(h, bins=bins, label="data", density=True)

    h, bins = np.histogram(df_mc[var], bins=bins)
    hep.histplot(h, bins=bins, label="mc", density=True)

    plt.xlabel(var)
    plt.ylabel("Count [a.u.]")
    plt.savefig(f"{output_dir}/{var}.png")