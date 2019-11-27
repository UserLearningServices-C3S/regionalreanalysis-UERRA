# CDS analyses data retrieval examples
All data produced within the Copernicus Climate Change Service regional reanalysis for Europe and the pre-operational UERRA project are publicly available for download.

This is an example of retrieving UERRA analyses data from one of the [CDS listed datasets](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra). Please note that this retrieval method is only applicable for analyses data. All other data (e.g. hourly forecasts) must be downloaded via the methods described in the ["cds_retrieve_complete_examples"](./../cds_retrieve_complete_examples/) folder or the ["mars_retrieve_examples"](./../mars_retrieve_examples/) folder.

Before running this script it is recommended to explore the available data and the corresponding CDS API requests by browsing the [CDS datasets](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=uerra).
Then modify the time, parameter and data origin in the script to match your specific needs.

The example provided here uses the python CDS API client.
Information about prerequisites for running this example can be found at the [CDS website](https://cds.climate.copernicus.eu/api-how-to).

## General information
This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data.
More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra).

The reanalysis data were initially produced within the FP7 pre-operational UERRA project.
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).
