# CDS unlisted data retrieval examples
All data produced within the Copernicus Climate Change Service regional reanalysis for Europe and the pre-operational UERRA project are publicly available for download via the Copernicus Climate Data Store API (CDS API).
These are example scripts for retrieving UERRA data that are not included in the [CDS listed datasets](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra).

The request syntax is based on the ECMWF MARS retrieval system. Before running these scripts it is recommended to explore the available data and the corresponding MARS requests via Web-MARS:<br />
[UERRA-HARMONIE data in Web-MARS](http://apps.ecmwf.int/datasets/data/uerra/levtype=sfc/stream=oper/type=an/)<br />
[MESCAN-SURFEX data in Web-MARS](http://apps.ecmwf.int/datasets/data/uerra-mescan-surfex/levtype=sfc/stream=oper/type=an/)<br />
Then modify the time, parameters, levels etc. in the scripts to match your specific needs.

The examples provided here use the python CDS API client.
Information about prerequisites for running these examples can be found at the [CDS website](https://cds.climate.copernicus.eu/api-how-to).

## General information
This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data.
More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-climate-change-service-regional-reanalysis-europe).

The reanalysis data were initially produced within the FP7 pre-operational UERRA project.
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).
