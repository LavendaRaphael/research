import numpy as np

array_devi = np.genfromtxt("model_devi.out", names=True, dtype=None)
tuple_trust = (0.15,0.25)
array_candidate_index = np.where( (array_devi["max_devi_f"]>tuple_trust[0]) & (array_devi["max_devi_f"]<tuple_trust[1]) )[0]
array_failed_index = np.where( array_devi["max_devi_f"]>tuple_trust[1] )[0]

print('---------------candidate')
for int_i in array_candidate_index:
    print( array_devi["step"][int_i], array_devi["max_devi_f"][int_i] )
print('---------------failed')
for int_i in array_failed_index:
    print( array_devi["step"][int_i], array_devi["max_devi_f"][int_i] )
