## Create Conda environment
```
conda create -n perfect python=3.11
conda activate perfect
```

Install prefect
```
pip install prefect
```

Deactivate environment
```
conda deactivate
```

Remove environment
```
conda env remove --name perfect
```

```
prefect server start
prefect cloud login
```


```
prefect profile ls
```

prefect profile create --name default --key <key>
prefect profile inspect default
prefect profile use default

Profile file
```
~/.prefect/profiles.toml
```

```
prefect deploy
perfect worker start -p my_pool
```