import numpy as np
import nrrd

### Some sample numpy data
data = np.zeros((5,4,3,2))
filename = 'test.seg.nrrd'

# Write to a NRRD file
nrrd.write(filename, data)

# Read the data back from file
filename = "Segmentation_LT_144.seg.nrrd"
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)

