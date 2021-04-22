import argparse
import os
from random import random, randint
import mlflow
from mlflow import log_metric, log_param, log_artifacts
import subprocess
import tempfile

parser = argparse.ArgumentParser(description='analysis2 step')
parser.add_argument('--fq1', type=str, default="")
parser.add_argument('--fq2', type=str, default="")
parser.add_argument('--download_run_id', type=str, default="")
args = parser.parse_args()


#local_dir = "/tmp/artifact_downloads"
local_dir = tempfile.mkdtemp()

if not os.path.exists(local_dir):
    os.mkdir(local_dir)


fq1 = args.fq1
fq2 = args.fq2
download_run_id = args.download_run_id

client = mlflow.tracking.MlflowClient()

apath = client.download_artifacts(download_run_id,"",local_dir)

fq1_file = apath+"/"+os.path.basename(fq1)
fq2_file = apath+"/"+os.path.basename(fq2)

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("fq1", fq1)
    log_param("fq2", fq2)
    log_param("download_run_id", download_run_id)

    # Log a metric; metrics can be updated throughout the run

    # Log an artifact (output file)
    if not os.path.exists("outputs2"):
        os.makedirs("outputs2")
    res = subprocess.run(["cwltool", "https://raw.githubusercontent.com/ddbj/sapporo-service/master/tests/resources/cwltool/trimming_and_qc_remote.cwl", "--fastq_1",fq1_file, "--fastq_2", fq2_file],cwd="outputs2")
    
    #with open("outputs/test.txt", "w") as f:
    #    f.write("hello world!")
    #
    #TODO: cwlを実行する
    log_artifacts("outputs2")
