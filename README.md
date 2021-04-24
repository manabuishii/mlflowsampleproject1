# mlflowsampleproject1
MLFlow Sample Project

## Setup software

- conda
- docker

## git clone

```
git clone https://github.com/manabuishii/mlflowsampleproject1.git
```

## Setup mlflow environment

```
conda create -n mlflow20210424
conda activate mlflow20210424
conda install python==3.8.3
pip install mlflow
pip install boto3
```

## Download data

```
mlflow run -e download_data .
```

Output

```
2021/04/24 15:59:58 INFO mlflow.projects: === Run (ID 'cdcf6e9bbfc34e07922c8a6e803b019e') succeeded ===
```

## Run workflow

```
mlflow run -e fastqc_trimming . -P download_run_id=cdcf6e9bbfc34e07922c8a6e803b019e
```

### Run without clone

```
mlflow run -e download_data https://github.com/manabuishii/mlflowsampleproject1 --version main
```