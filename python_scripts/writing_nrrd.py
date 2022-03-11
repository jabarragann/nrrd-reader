import numpy as np
import nrrd

### Some sample numpy data
data = data = np.linspace(1, 60, 60).reshape((3, 10, 2))

header={'encoding': 'raw'}
filename = 'test.seg.nrrd'

# Write to a NRRD file
nrrd.write(filename, data, header)

# Read the data back from file
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)

