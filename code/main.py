import numpy as np
import pandas as pd


def importation(name_file, name_ref):
    x = pd.read_csv(name_file)
    ref = pd.read_csv(name_ref)
    return x, ref


whales, whales_ref = importation(
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data.csv", 
    "../dataset/large marine fauna/blue whales/Blue whales Eastern North Pacific 1993-2008 - Argos Data-reference-data.csv")

print(whales)
print(whales_ref)