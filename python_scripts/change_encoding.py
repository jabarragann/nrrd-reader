import numpy as np
import nrrd


# Read the data back from file
filename = "Segmentation_LT_144.seg.nrrd"
readdata, header = nrrd.read(filename)

header["encoding"] = "raw"

print(readdata.shape)
print(header["encoding"])

new_filename = "Segmentation144.raw.nrrd"
nrrd.write(new_filename, readdata, header)
