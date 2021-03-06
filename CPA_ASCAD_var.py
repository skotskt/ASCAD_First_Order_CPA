import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt

if __name__ == '__main__':
	HWtable = np.load("ASCAD_var_HWtable.npy") #Generated by makeHWtable_ASCAD_var.py
	trace = np.load("ASCAD_var_atk_traces_norm.npy") #Attack traces of variable_key_database. Normalized(the value is limited to [0,1]) for use in machine learning.
	corr = np.zeros((256, len(trace)), dtype=np.float32)
	for i in tqdm(range(256)):
		for j in range(len(trace)):
			corr[i][j] = np.corrcoef(HWtable[i, :j], trace[:j, 188])[0][1] #Calculate correlation coefficient for each key candidate. i denotes key candidate and j denotes number of traces.
		plt.plot(range(len(trace)), np.abs(corr[i]), color="lightgrey" if i!=34 else "red", zorder=1 if i!=34 else 256) #Plot the result of CPA. "34" is correct key value, so emphasized.

	plt.show()
