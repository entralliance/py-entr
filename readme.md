# py-entr
The ENTR Alliance's python package to load data from an ENTR Warehouse to perform analysis on these data using OpenOA.

## Quickstart:
We recommend using the [ENTR Runtime](https://github.com/entralliance/entr_runtime) Docker Image if you are new to the ENTR project. This image redistributes py-entr alongside its dependencies and example data, and is the easiest way to get started using py-entr.

## Features:

- Python classes `entr.connector.PySparkEntrConnector` and `entr.connector.PyHiveEntrConnector` that facilitate connecting and reading data from an entr warehouse to Pandas through the `pandas_query` function.
- An OpenOA PlantData constructur: `entr.plantdata.from_entr` constructor, which flexibly creates an OpenOA PlantData object from a query schema. *This constructor is used by openoa.plant.from_entr if both openoa and pyentr are installed.*
- Pyspark user defined function (UDF) `entr.udf.aep_spark_map` which distributes the OpenOA AEP computation over a spark data warehouse using the Spark DataFrame API.

## Example Notebooks

This repo contains example notebooks in the `/examples` directory.

- TODO: Just copied in the entr notebooks from OpenOA for now, need to update these.

## Contriubuting to py-entr:

To contribute to this repository, please fork it into your own account, create a new branch from `dev` with the prefix `feature/`, and then submit a pull request into the `dev` branch when you're ready.

