#!/usr/bin/python3

import numpy as np
import nrrd
import argparse
from pathlib import Path


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True, help="input file")
    parser.add_argument("--out", required=True, help="output file")
    parser.add_argument(
        "--encoding", required=True, choices=["raw", "gzip"], help="encoding. [raw or gzip]"
    )
    args = parser.parse_args()

    inputfile = Path(args.infile)
    outputfile = Path(args.out)
    encoding = args.encoding

    if not inputfile.exists():
        raise ValueError("input file does not exist")

    readdata, header = nrrd.read(inputfile)

    print(f"data shape: {readdata.shape}")
    print(f"current encoding {header['encoding']}")
    print(f"future encoding {encoding}")

    header["encoding"] = encoding
    nrrd.write(str(outputfile), readdata, header)
