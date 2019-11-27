# Create forcing data for NEMO-Nordic

These scripts are an example of how the UERRA data can be used for input to other model systems, in this case the NEMO-Nordic (a regional ocean model).

The objectives of the scripts
-----------------------------
These scripts will:

1. download the needed,
2. extract the region needed for NEMO-Nordic,
3. convert the units as needed for NEMO-Nordic,
4. save the final files as netCDF.


Instructions
------------
Basically, users have only to adopt the "Configure section" in the
main script - Create_NEMO_forcing_from_UERRA.py

1. Set the dates your are interested in.
2. Define directories for downloaded data, the final data, and
   a directory for temporary files.

Then, all you have to do is to run the main script...
Create_NEMO_forcing_from_UERRA.py


Good to know
------------
The scripts need some time to run. Especially the downloading of data
from the MARS archive takes time. Here, we are talking about days if
you want to produce forcing data for longer periods (several years).
A rough estimate is about six hours for each year. However, this depends
on your system as well as the load on MARS.
You will need some disk space. For each year you will need around 50GB
space.


Technical details
-----------------
The scripts were developed and tested with Python 2.7.9.
The scripts use [CDO](http://mpimet.mpg.de/cdo) commands to a large degree so the CDO python bindings need to be installed.

Below is info from the cdo -V command:<br>
Climate Data Operators version 1.7.0 (http://mpimet.mpg.de/cdo)<br>
Features: DATA PTHREADS OpenMP4 HDF5 NC4/HDF5 OPeNDAP Z PROJ.4 SSE2<br>
Libraries: HDF5/1.8.14 proj/4.7<br>
Filetypes: srv ext ieg grb grb2 nc nc2 nc4 nc4c CDI library version : 1.7.0<br> CGRIBEX library version : 1.7.3 <br>
GRIB_API library version : 1.14.0 <br>
netCDF library version : 4.3.2<br>
HDF5 library version : 1.8.14<br>

Moreover, to fetch data from the MARS archive, you will need the
corresponding modules. Please find out on [ECMWF's website](https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Public+Datasets).
Otherwise, used modules should be standard.


Overview on the order of called routines
----------------------------------------
Create_NEMO_forcing_from_UERRA.py<br>
==> Get_UERRA_data.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> a) Get_UERRA_data.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Forecasts<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> b) Get_UERRA_data.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Analyses<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> c) Get_UERRA_data.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Precipitation (differences incorporated)<br>
==> Convert_for_NEMO.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> a) Convert_for_NEMO.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Precipitation<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> b) Convert_for_NEMO.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Parameters with analysis<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> c) Convert_for_NEMO.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Radiation<br>
&nbsp;&nbsp;&nbsp;&nbsp;==> d) Convert_for_NEMO.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==> Humidity<br>



## General information
This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data.
More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra).

The reanalysis data were initially produced within the FP7 pre-operational UERRA project.
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).
