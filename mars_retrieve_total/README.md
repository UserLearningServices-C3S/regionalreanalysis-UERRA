# MARS retrieval examples
All data produced within the Copernicus Climate Change Service regional reanalysis for Europe and the pre-operational UERRA project are publicly available for download via the ECMWF MARS system. These are example python scripts for retrieving all the datasets within the reanalysis. Please note that these requests can result in the retrieval of a lot of data. The scripts are provided as a complete base showing all available data.

Before running these scripts it is recommended to explore the available data and the corresponding MARS requests via Web-MARS:<br />
[UERRA-HARMONIE data in Web-MARS](http://apps.ecmwf.int/datasets/data/uerra/levtype=sfc/stream=oper/type=an/)<br />
[MESCAN-SURFEX data in Web-MARS](http://apps.ecmwf.int/datasets/data/uerra-mescan-surfex/levtype=sfc/stream=oper/type=an/)<br />
Then modify the time, parameters, levels etc. in the scripts to match your specific needs.

The examples provided here use the python ECMWF Web-API client.
Information about prerequisites for running these examples can be found at the [ECMWF website](https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Public+Datasets).
The examples are based on the [UERRA SMHI retrieval efficiency Web-API example](https://software.ecmwf.int/wiki/display/WEBAPI/UERRA+SMHI+retrieval+efficiency).

## General information
This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data.
More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra).

The reanalysis data were initially produced within the FP7 pre-operational UERRA project.
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).
