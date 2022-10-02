# CIS II Project - NRRD reader

# Goal
Adding a gzip uncompressing strategy for the nrrd files.

# Status 
Currently not able to uncompresse files bigger than a GB.

## Initial  Code obtained from 

* https://sourceforge.net/projects/nrrd-cpp/
* https://github.com/mapbox/gzip-hpp


## resources
* https://www.rapidtables.com/convert/number/hex-to-ascii.html
* https://github.com/mapbox/gzip-hpp/blob/master/include/gzip/decompress.hpp

**Uncompressing gzip line by line**

* https://stackoverflow.com/questions/1965751/how-do-i-read-a-huge-gz-file-more-than-5-gig-uncompressed-in-c
* https://stackoverflow.com/questions/23962782/c-c-arbitrary-output-size-when-decompressing-gzip

**Resetting file after reaching eof**

* https://stackoverflow.com/questions/5343173/returning-to-beginning-of-file-after-getline/5343199#5343199

**Get lenght of file**

* https://cplusplus.com/reference/istream/istream/seekg/
