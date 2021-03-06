# About
Source code to perform first-order CPA on traces provided by [ASCAD](https://github.com/ANSSI-FR/ASCAD).

Traces used in source codes have not been modified from original hdf5 files except min-max normalization.

To use npy files we used in the experiment, please refer to this [link](https://fsa.fir.riec.tohoku.ac.jp/fircloud/index.php/s/lbYsMUJAOFzJ6DG).

| file name             | description           |
| ---------------- | ---------------- |
| makeHWtable_ASCAD_fix.py | makes a hypothetical power consumption table for fixed key database  |
| makeHWtable_ASCAD_var.py | makes a hypothetical power consumption table for variable key database         |
| CPA_ASCAD_fix.py | performs CPA on fixed_key_database   |
| CPA_ASCAD_var.py | performs CPA on variable_key_database         |
| ASCAD_fix_atk+pro_plaintext_3rdbyte.npy | 3rd byte of plaintexts correspond to traces in fixed_key_database  |
| ASCAD_fix_HWtable.npy | table of hypothetical power consumption for fixed_key_database         |
| ASCAD_fix_atk+pro_traces_norm.npy | min-max normalized traces from fixed_key_database   |
| ASCAD_var_atk_plaintext_3byte.npy |3rd byte of plaintexts correspond to traces in variable_key_database         |
| ASCAD_var_HWtable.npy | table of hypothetical power consumption for variable_key_database         |
| ASCAD_var_atk_traces_norm.npy | min-max normalized traces from variable_key_database   |



CPA results would be as followed:


![figure](https://user-images.githubusercontent.com/49137368/80730020-01a74d80-8b44-11ea-8bc9-530afef33a77.jpg)
