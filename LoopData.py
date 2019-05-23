import numpy as np
np_1 = np.array([10,20,30,40,50,60,70,80])
np_2 = np.array([1,2,3,4,5,6,7,8])
# 1 bmi = np_1/np_2**2
# 1 for val in bmi:
meas = np.array([np_1, np_2])
for val in np.nditer(meas):
    print(val)
# 2 print(meas)