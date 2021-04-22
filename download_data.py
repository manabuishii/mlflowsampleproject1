import argparse
import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts, log_text
import subprocess


OUTPUTDIR="outputs"

entrypoint = "download_data"
parser = argparse.ArgumentParser(description='analysis2 step')
parser.add_argument('--fq1', type=str, default="")
parser.add_argument('--fq2', type=str, default="")
parser.add_argument('--nthreads', type=int, default=1)
args = parser.parse_args()

#fq1="https://raw.githubusercontent.com/pitagora-network/DAT2-cwl/develop/test/data/DRR024501_1.fastq"
fq1 = args.fq1
fq2 = args.fq2
#fq2="https://raw.githubusercontent.com/pitagora-network/DAT2-cwl/develop/test/data/DRR024501_2.fastq"



if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("fq1", fq1)
    log_param("fq2", fq2)

    # Log an artifact (output file)
    if not os.path.exists(OUTPUTDIR):
        os.makedirs(OUTPUTDIR)
    # with open("outputs/test.txt", "w") as f:
    #     f.write("hello world!")
    res_fq1 = subprocess.run(["curl", "-O", "-L", "-s", fq1],cwd=OUTPUTDIR)
    res_fq2 = subprocess.run(["curl", "-O", "-L", "-s", fq2],cwd=OUTPUTDIR)

    log_artifacts(OUTPUTDIR)

    # Log text
    #log_text("fq1_filename", os.path.basename(fq1))
    #log_text("fq2_filename", os.path.basename(fq2))

