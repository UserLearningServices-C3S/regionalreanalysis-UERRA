# Copernicus Climate Change Service regional reanalysis for Europe - User Examples

This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data. More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-climate-change-service-regional-reanalysis-europe).

The reanalysis data used here were initially produced within the FP7 pre-operational UERRA project.<br />
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).

## CDS retrieval examples
All data produced within the Copernicus Climate Change Service regional reanalysis for Europe and the pre-operational UERRA project are publicly available for download via the Copernicus Climate Data Store API (CDS API).
The examples provided here use the python CDS API client.
Information about prerequisites for running these examples can be found at the [CDS website](https://cds.climate.copernicus.eu/api-how-to).

The folder ["cds_listed_retrieve_examples"](cds_listed_retrieve_examples/) contains an example python script for retrieving CDS listed data from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the CDS API.<br />This is an example of the syntax used for retrieving data that are listed as [CDS datasets](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra).<br />
Modify the date, time and parameter to match your specific needs.

The folder ["cds_unlisted_retrieve_examples"](cds_unlisted_retrieve_examples/) contains example python scripts for retrieving unlisted data from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the CDS API.<br />These are examples of the syntax used for retrieving data that are not listed as [CDS datasets](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra).<br />
Modify the time, parameters, levels etc. to match your specific needs.


## MARS retrieval examples
All the data produced are still also publicly available for download via the ECMWF MARS system.
The examples provided here uses the python ECMWF Web-API client.
Information about prerequisites for running these examples can be found at the [ECMWF website](https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Public+Datasets).

The folder ["mars_retrieve_examples"](mars_retrieve_examples/) contains example python scripts for retrieving temperature and 24 hour precipitation data from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the ECMWF MARS system.<br />
Modify the time, parameters, levels etc. to match your specific needs.

The folder ["mars_retrieve_total"](mars_retrieve_total/) contains python scripts for retrieving all datasets from the Copernicus Climate Change Service regional reanalysis for Europe reanalysis via the ECMWF MARS system.<br />
The scripts are provided as a complete base showing all available data. Please note that this means a lot of data. Modify the time, parameters, levels etc. to match your specific needs.
