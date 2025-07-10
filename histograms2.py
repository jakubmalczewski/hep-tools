import numpy as np
import uproot as up
import pandas as pd
from matplotlib import pyplot as plt
import mplhep as hep
from dataclasses import dataclass

hep.style.use("LHCb2")
plt.rcParams["figure.figsize"] = [10, 8]
plt.rcParams["figure.dpi"] = 200
plt.rcParams["font.size"] = 12

output_dir = "output/"

mc_files = ["Lc2pemu_MC_MagDown.root", "Lc2pemu_MC_MagUp.root"]
data_file = "Lc2pemu_Data.root:DecayTree"


@dataclass
class Variable:
    """Histogram parameters"""
    name: str                   # required field
    bins: int = 50              # can be a number of bins or array with edges
    xlabel: str | None = None
    density: bool = True        # should we normalized the distribution?
    yscale: str = "linear"
    xscale: str = "linear"

    def __post_init__(self):
        if self.xlabel is None:
            # use a variable name as a label of the x-axis, if the label was not provided 
            self.xlabel = self.name


variables = [
    Variable("Lc_IP_OWNPV", bins=np.linspace(0,0.3,50)),
    Variable("Lc_IPCHI2_OWNPV", bins=np.linspace(0,15,50)),
    Variable("Lc_FD_OWNPV", bins=np.linspace(0,20,50)),
    Variable("Lc_FDCHI2_OWNPV", bins=np.linspace(0,1000,50)), 
    Variable("Lc_ENDVERTEX_CHI2"),
    Variable(
        "Lc_PT", 
        bins=np.linspace(0,10000,50), 
        xlabel="Transverse momentum [MeV/c]",
        ),
    Variable(
        "Lc_M", 
        density = False, 
        yscale="log",
        ),
]

all_names = [var.name for var in variables]
mc_batches = []
for batch in up.iterate(mc_files, filter_name=all_names, library="pd"):
    mc_batches.append(batch)
df_mc = pd.concat(mc_batches)

tree_data = up.open(data_file) 

for var in variables:
    plt.figure()
    h, bins = np.histogram(tree_data[var.name], bins=var.bins)
    hep.histplot(h, bins=bins, label="data", density=var.density)

    h, bins = np.histogram(df_mc[var.name], bins=bins)
    hep.histplot(h, bins=bins, label="mc", density=var.density)

    plt.yscale(var.yscale)
    plt.xscale(var.xscale)
    plt.xlabel(var.xlabel)
    plt.ylabel("Count [a.u.]")
    plt.legend()
    plt.savefig(f"{output_dir}/{var.name}.png")