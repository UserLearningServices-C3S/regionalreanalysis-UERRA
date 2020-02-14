#!/usr/bin/env python

# GRIB
import pygrib

# Date
from datetime import datetime

# Plot
import matplotlib
import pylab as plt
import matplotlib.colors as clr
from mpl_toolkits.basemap import Basemap

# CDO
from cdo import *
cdo   = Cdo()

# NetCDF
import netCDF4
from netCDF4 import Dataset

# path to data
data_path = ''
# file name
data_file = 'download.grib'

# select dates to plot
year = [2005]
month = [1]
day = [8,9]
hour = [0,6,12,18]

# plot GRIB or netCDF and animate or not
grib = True
netcdf = False
animate = False

def select_date(data):
    """
    a function to compare dates and return an array of locations to select datest
    """
    sel_data = []
    i = 0
    for d in data:
        if d.year in year and d.month in month and d.day in day and d.hour in hour:
            sel_data.append(i)
        i = i+1
 
    return sel_data

def plotting(lon, lat, wind, MSLP, title=None, savename=None, levels=None, cmap=None):
    """
    A function to plot wind and pressure data
    """
    plt.figure(figsize=(10,10))

    m = Basemap(llcrnrlon=-15, llcrnrlat=40, urcrnrlon=25, urcrnrlat=75, resolution='l')
    x, y = m(lon, lat) # koordinater grid

    draw_extras(m) # draw coastlines, countries, rivers

    # Wind
    CS_wind = m.contourf(x, y, wind, extend='max', levels=levels, cmap=cmap)
    cbar = m.colorbar(CS_wind) 
    cbar.ax.set_title('[m/s]')

    # MSLP
    CS_mslp = m.contour(x, y, MSLP/100, levels=range(950,1050,5), colors='k', linewidths=1)
    plt.clabel(CS_mslp, inline=1, forntsize=10, fmt='%i', zoder=0)

    if title:
        plt.title(title)  

    if savename:
        plt.savefig(savename)   
    
    plt.show()

def draw_extras(m):
    """
    A function to draw coastlines, countries, rivers
    """
    m.drawcountries(linewidth=0.4, color='k', zorder=4)
    m.drawcoastlines(linewidth=0.4, color='k', zorder=4)

def to_netcdf(data):
    """
    A function to transform data to netCDF-file
    Return data as netCDF
    """
    nc_data = cdo.setgridtype('curvilinear', input=data, options='-f nc')

    return nc_data

def read_netcdf(data, variable):
    """
    A function to read data from netCDF-file
    Return time, longitude, latitude and value of 'variable'
    """
    nc_fid = Dataset(data, 'r')

    time_var = nc_fid.variables['time']
    dtime = netCDF4.num2date(time_var[:],time_var.units)
    lats = nc_fid.variables['lat'][:]
    lons = nc_fid.variables['lon'][:]
    data = nc_fid.variables[variable][:].squeeze()

    return dtime, lons, lats, data

if __name__ == '__main__':
    
    if grib:
        grb_data = pygrib.open(data_path+data_file) # read GRIB

        wind = grb_data.select(name='10 metre wind speed') # select wind data
        MSLP = grb_data.select(name='Mean sea level pressure') # select pressure data

        sel_data = select_date(wind) # select time

        for i in sel_data:
            lats, lons = wind[i].latlons() # read longitude and lattitude from GRIB
            
            values_wind = wind[i].values        
            values_MSLP = MSLP[i].values
            
            time = datetime(wind[i].year, wind[i].month, wind[i].day, wind[i].hour)          
            title = 'Storm ' + time.strftime('%Y-%b-%d %H:%M')
            savename = data_path + 'Storm_' + time.strftime('%Y%m%d_%H%M') + '.png'
            
            levels = [0,0.3,1.6,3.4,5.5,8,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
            colors = ['#5EBC32','#ffff00','#AF111A','#764285']
            cmap = clr.LinearSegmentedColormap.from_list('wind speed', colors, N=256)
            plotting(lons, lats, values_wind, values_MSLP, title=title, savename=savename, levels=levels, cmap=cmap) #plotting GRIB-data

    if netcdf:
        nc_data = to_netcdf(data_path+data_file) # transform GRIB to netCDF
  
        [time, lons, lats, wind] = read_netcdf(nc_data, '10si') # read wind data from netCDF
        [time, lons, lats, MSLP] = read_netcdf(nc_data, 'msl') # read pressure data from netCDF
        
        sel_data = select_date(time) # select time

        for i in sel_data: 
            values_wind = wind[i,:,:]
            values_MSLP = MSLP[i,:,:]
           
            title = 'Storm ' + str(time[i].strftime('%Y-%b-%d %H:%M'))
            savename = data_path + 'Storm_' + str(time[i].strftime('%Y%m%d_%H%M')) + '.png'

            levels = [0,0.3,1.6,3.4,5.5,8,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
            colors = ['#5EBC32','#ffff00','#AF111A','#764285']
            cmap = clr.LinearSegmentedColormap.from_list('wind speed', colors, N=256)
            plotting(lons, lats, values_wind, values_MSLP, title=title, savename=savename, levels=levels, cmap=cmap) #plotting NetCDF-data

    if animate:
        figurename = data_path + 'Storm_*.png'
        animationname = data_path + 'stormanimation.gif'
        subprocess.call('convert -delay 100 ' + figurename + ' ' + animationname, shell=True)
