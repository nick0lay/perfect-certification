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

## Deployment
Deployment configuration saved to prefect.yaml! You can now deploy using this deployment configuration with:

        $ prefect deploy -n weather-flow-deployment

You can also make changes to this deployment configuration by making changes to the prefect.yaml file.

To execute flow runs from this deployment, start a worker in a separate terminal that pulls work from the 'weather-pool' work pool:

        $ prefect worker start --pool 'weather-pool'

To schedule a run for this deployment, use the following command:

        $ prefect deployment run 'Weather Flow/weather-flow-deployment'

## Execution
To execute flow runs from this deployment, start a worker in a separate terminal that pulls work from the 'weather-pool' work pool:

        $ prefect worker start --pool 'weather-pool'

To schedule a run for this deployment, use the following command:

        $ prefect deployment run 'Weather Flow/weather-flow-deployment'