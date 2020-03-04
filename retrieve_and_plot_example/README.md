# Retrieve and plot UERRA data
These scripts are an example of how to retrieve UERRA data from CDS API and plot GRIB or netCDF data with Python.

## The objectives of the scripts
These scripts will:

1. Retrieve data with CDS API.
2. Plot GRIB or netCDF data.
3. Make an animation.

## Instructions

1. Set the dates your are interested in.
2. Define directory for the downloaded file.
3. Set GRIB or netCDF and whether to animate or not.
4. Run retrive_UERRA.py to retrieve data.
5. Run plot_UERRA.py to plot the data.

## Good to know
The scripts need some time if you are downloading a lot of data.

## Technical details
The scripts were developed and tested with Python 2.7.9 in Linux.

Used modules:  
pygrib version : 2.0.0  
netCDF4 version : 1.1.3  
matplotlib version : 1.4.2  
pylab  
datetime  
cdsapi  

The plot script use the [CDO program](http://mpimet.mpg.de/cdo) and it's python bindings to transform from GRIB to netCDF.  
If you don't need to transform you don't need CDO.  
  
Below is info from the cdo -V command:  
Climate Data Operators version 1.7.0 (http://mpimet.mpg.de/cdo)  
Features: DATA PTHREADS OpenMP4 HDF5 NC4/HDF5 OPeNDAP Z PROJ.4 SSE2  
Libraries: HDF5/1.8.14 proj/4.7  
Filetypes: srv ext ieg grb grb2 nc nc2 nc4 nc4c  
CDI library version : 1.7.0  
CGRIBEX library version : 1.7.3  
GRIB_API library version : 1.14.0  
netCDF library version : 4.3.2  
HDF5 library version : 1.8.14  

Moreover, to fetch data from CDS, you will need an account at [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/).

## General information
This project contains example code for users of the Copernicus Climate Change Service regional reanalysis for Europe (C3S_322_Lot1) data.
More information about the service can be found at the [Copernicus Climate Change Service regional reanalysis for Europe website](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra).

The reanalysis data were initially produced within the FP7 pre-operational UERRA project.
More information about the reanalyses systems and data can be found at the [UERRA website](http://www.uerra.eu/).
These scripts belong to a lesson at [Copernicus user lerning service (ULS)](https://uls.climate.copernicus.eu/).
