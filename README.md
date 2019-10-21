# Copernicus Climate Change Service regional reanalysis for Europe - User Examples

This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data. More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra).

The reanalysis data used here were initially produced within the FP7 pre-operational UERRA project.<br />
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).

## CDS retrieval examples
All data produced within the Copernicus Climate Change Service regional reanalysis for Europe and the pre-operational UERRA project are publicly available for download. The analyses are listed in the [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra) and can be downloaded via the Copernicus Climate Data Store API (CDS API).
The examples provided here use the python CDS API client.
Information about prerequisites for running these examples can be found at the [CDS website](https://cds.climate.copernicus.eu/api-how-to).

The folder ["cds_retrieve_analyses_examples"](cds_retrieve_analyses_examples/) contains an example python script for retrieving analysis data from the Copernicus Climate Change Service regional reanalysis for Europe via the CDS API.<br />
Modify the date, time and parameter to match your specific needs.

## MARS retrieval examples
All the data produced are publicly available for download via the ECMWF MARS system.
The examples provided here uses the python ECMWF Web-API client.
Information about prerequisites for running these examples can be found at the [ECMWF website](https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Public+Datasets).

The folder ["mars_retrieve_examples"](mars_retrieve_examples/) contains example python scripts for retrieving temperature and 24 hour precipitation data from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the ECMWF MARS system.<br />
Modify the time, parameters, levels etc. to match your specific needs.

The folder ["mars_retrieve_total"](mars_retrieve_total/) contains python scripts for retrieving all datasets from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the ECMWF MARS system.<br />
The scripts are provided as a complete base showing all available data. Please note that this means a lot of data. Modify the time, parameters, levels etc. to match your specific needs.

## Create forcing data for NEMO-Nordic
The folder ["create_forcing_for_NEMO"](create_forcing_for_NEMO/) contains a script system, which can be used to prepare forcing data for NEMO-Nordic (a regional ocean model). The scripts retrieve hourly data from MARS and mix analyses and forecasts. Then, the data is post-processed for the usage with NEMO-Nordic. For instance, relative humidity is transferred to specific humidity. At the end, the data is stored in netcdf-format as needed by NEMO.
