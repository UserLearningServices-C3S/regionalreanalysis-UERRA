from cdo import *
cdo=Cdo()

import shutil
import os
import glob
import sys


# What needs to be done with the raw data?
# 1. Reduce the domain to fit the Baltic/North Sea.
# 2. Change some units.
#    a) humidity: from relative [%] to specific [kg/kg]
#    b) wind: from speed and direction to u and v
#    c) precipitation: from kg/m^2 to kg/m^2/s



def precipitation(yearStart, monthStart, yearEnd, monthEnd, workdir, downdir, finaldir):
    """
    Prepare precipitation for NEMO-Nordic. Both rain and snow.
    Extract area, make 12h values (24fc-12fc), change the unit from kg/m^2 to kg/m^2/s.
    Merge all data for one year.
    """
    for year in list(range(yearStart, yearEnd + 1)):
        print "Working on precipitation, year: " , year
#        for month in list(range(monthStart, monthEnd + 1)):
        for month in list(range(monthStart, 13)):
            print "month: ", month
            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

# 1. Reduce the domain to fit the Baltic/North Sea.
            outfile3= workdir+"UERRA_precip_diff_%04d%02d.grb" % (year, month)
            infile2 = downdir+"RR24-12_UERRA_%04d%02d_fc.grb" % (year, month)
            cdo.selindexbox("200,405,280,470", 
                            input=" -setgridtype,curvilinear "+infile2, 
                            output=outfile3, options = '-f nc')


            if year == yearEnd and month == monthEnd:
                # Done with the last month.
                break

# Merge monthly files to a yearly file.
        outfile4=workdir+"UERRA_precip_diff_%04d.grb" % (year)
        cdo.mergetime(input=workdir+"UERRA_precip_diff_%04d??.grb" % (year), 
                      output=outfile4)
        
# Split up rain and snow and change the units. Copy to final destination.
        cdo.splitname(input=outfile4, output=workdir+"UERRA_precip_")

        outfile =workdir+"rain_y"+str(year)+".nc"
        cdo.setname("RAIN",   input=" -divc,43200 "+workdir+"UERRA_precip_tp.nc", output=outfile)
        shutil.copy(outfile, finaldir+"Precip")

        snowfile=workdir+"snow_y"+str(year)+".nc"
        cdo.setname("SNOW",   input=" -divc,43200 "+workdir+"UERRA_precip_sf.nc", output=snowfile)
        shutil.copy(snowfile, finaldir+"Snow")

# Clean up
        for fl in glob.glob(workdir+"UERRA*.nc"):
            os.remove(fl)
        for fl in glob.glob(workdir+"UERRA*.grb"):
            os.remove(fl)



def param_with_analysis(yearStart, monthStart, yearEnd, monthEnd, workdir, downdir, finaldir):
    """
    Prepare all parameters which are avail for the analysis; T2m, SLP, wind.
    Extract area, merge analysis and forecasts. Change the units for wind.
    From wind speed and direction to u/v components in m/s.
    Merge all data for one year for each parameter.
    """
    for year in list(range(yearStart, yearEnd + 1)):
        print "Working on temperature, SLP and wind, year: " , year
#        for month in list(range(monthStart, monthEnd + 1)):
        for month in list(range(monthStart, 13)):
            print "month: ", month
            sys.stdout.flush()
            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

# 1. Reduce the domain to fit the Baltic/North Sea.
            infile1 =downdir+"UERRA_an_%04d%02d.grb" % (year, month)
            outfile1=workdir+"UERRA_an_%04d%02d.nc" % (year, month)
            cdo.selindexbox("200,405,280,470", 
                            input=" -setgridtype,curvilinear "+infile1, 
                            output=outfile1, options = '-f nc')
            infile2 =downdir+"UERRA_fc_%04d%02d.grb" % (year, month)
            outfile2=workdir+"UERRA_fc_%04d%02d.nc" % (year, month)
# For parameters available at the analysis time, forecasts valid at 0, 6, 12, and 18 are not needed.
            cdo.selindexbox("200,405,280,470", 
                            input=" -setgridtype,curvilinear -selhour,1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,20,21,22,23 -selname,wdir,10si,msl,2t "+infile2, 
                            output=outfile2, options = '-f nc')

            if year == yearEnd and month == monthEnd:
                # Done with the last month.
                break


# Merge monthly files to a yearly file.
        print "Merge ", year, "and finalize the preparation."
        sys.stdout.flush()
        outfile3=workdir+"UERRA_analysis_%04d.nc" % (year)
        cdo.mergetime(input=workdir+"UERRA_fc_%04d??.nc" % (year)+" "+workdir+"UERRA_an_%04d??.nc" % (year), 
                      output=outfile3, options = '-O')
# Make sure it is really only one year.
        yearfile=workdir+"UERRA_exact_one_year_%04d.nc" % (year)
        cdo.selyear(year, input=outfile3, output=yearfile, options = '-O')
        
        cdo.splitname(input=yearfile, output=workdir+"UERRA_analysis_%04d_" % (year))

### T2m
# Change the parameter name and copy to final destination.
        infile=workdir+"UERRA_analysis_%04d_2t.nc" % (year)
        tfile =workdir+"tair_y"+str(year)+".nc"
        cdo.setname("TAIR", input=infile, output=tfile)
        shutil.copy(tfile, finaldir+"T2m/")

### MSLP
# Change the parameter name and copy to final destination.
        infile=workdir+"UERRA_analysis_%04d_msl.nc" % (year)
        pfile =workdir+"pres_y"+str(year)+".nc"
        cdo.setname("PRES", input=infile, output=pfile)
        shutil.copy(pfile, finaldir+"MSLP/")


### Wind
# Convertion from speed and direction into u+v components
# Then, copy to final destination.
        infile1=workdir+"UERRA_analysis_%04d_10si.nc" % (year)
        infile2=workdir+"UERRA_analysis_%04d_wdir.nc" % (year)
        cdo.chname("10si,speed", input=infile1, output=workdir+"UERRA_analysis_%04d_speed.nc" % (year))
        wfile  =workdir+"speedy_y"+str(year)+".nc"
        cdo.merge(input=infile2+" "+workdir+"UERRA_analysis_%04d_speed.nc" % (year), output=wfile)

        zzfile  =workdir+"uv_y"+str(year)+".nc"
        cdo.expr('\'U=(-1)*speed*sin(0.01745329252*wdir);V=(-1)*speed*cos(0.01745329252*wdir);\'', 
                 input=wfile, output=zzfile)
        shutil.copy(zzfile, finaldir+"Wind/")

        sys.stdout.flush()

        for fl in glob.glob(workdir+"UERRA*.nc"):
            os.remove(fl)


def radiation(yearStart, monthStart, yearEnd, monthEnd, workdir, downdir, finaldir):
    """
    Prepare long and shortwave radiation.
    Change the unit from J/m2 to W/m2 by dividing with 3600s.
    """
    for year in list(range(yearStart, yearEnd + 1)):
        print "Working on radiation, year: " , year
        for month in list(range(monthStart, 13)):
#        for month in list(range(monthStart, monthEnd + 1)):
            print "month: ", month
            sys.stdout.flush()
            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

            infile2 =downdir+"UERRA_fc_%04d%02d.grb" % (year, month)
            outfile2=workdir+"UERRA_fc_%04d%02d.nc" % (year, month)
            cdo.selindexbox("200,405,280,470", 
                            input=" -setgridtype,curvilinear -selname,ssrd,strd "+infile2, 
                            output=outfile2, options = '-f nc')

            cdo.splithour(input=outfile2, output=workdir+"hour_")

            cdo.sub(input=workdir+"hour_02.nc"+" "+workdir+"hour_01.nc", output=workdir+"hourly_02.nc")
            cdo.sub(input=workdir+"hour_03.nc"+" "+workdir+"hour_02.nc", output=workdir+"hourly_03.nc")
            cdo.sub(input=workdir+"hour_04.nc"+" "+workdir+"hour_03.nc", output=workdir+"hourly_04.nc")
            cdo.sub(input=workdir+"hour_05.nc"+" "+workdir+"hour_04.nc", output=workdir+"hourly_05.nc")
            cdo.sub(input=workdir+"hour_06.nc"+" "+workdir+"hour_05.nc", output=workdir+"hourly_06.nc")
            cdo.sub(input=workdir+"hour_08.nc"+" "+workdir+"hour_07.nc", output=workdir+"hourly_08.nc")
            cdo.sub(input=workdir+"hour_09.nc"+" "+workdir+"hour_08.nc", output=workdir+"hourly_09.nc")
            cdo.sub(input=workdir+"hour_10.nc"+" "+workdir+"hour_09.nc", output=workdir+"hourly_10.nc")
            cdo.sub(input=workdir+"hour_11.nc"+" "+workdir+"hour_10.nc", output=workdir+"hourly_11.nc")
            cdo.sub(input=workdir+"hour_12.nc"+" "+workdir+"hour_11.nc", output=workdir+"hourly_12.nc")
            cdo.sub(input=workdir+"hour_14.nc"+" "+workdir+"hour_13.nc", output=workdir+"hourly_14.nc")
            cdo.sub(input=workdir+"hour_15.nc"+" "+workdir+"hour_14.nc", output=workdir+"hourly_15.nc")
            cdo.sub(input=workdir+"hour_16.nc"+" "+workdir+"hour_15.nc", output=workdir+"hourly_16.nc")
            cdo.sub(input=workdir+"hour_17.nc"+" "+workdir+"hour_16.nc", output=workdir+"hourly_17.nc")
            cdo.sub(input=workdir+"hour_18.nc"+" "+workdir+"hour_17.nc", output=workdir+"hourly_18.nc")
            cdo.sub(input=workdir+"hour_20.nc"+" "+workdir+"hour_19.nc", output=workdir+"hourly_20.nc")
            cdo.sub(input=workdir+"hour_21.nc"+" "+workdir+"hour_20.nc", output=workdir+"hourly_21.nc")
            cdo.sub(input=workdir+"hour_22.nc"+" "+workdir+"hour_21.nc", output=workdir+"hourly_22.nc")
            cdo.sub(input=workdir+"hour_23.nc"+" "+workdir+"hour_22.nc", output=workdir+"hourly_23.nc")
            cdo.sub(input=workdir+"hour_00.nc"+" "+workdir+"hour_23.nc", output=workdir+"hourly_00.nc")

            os.rename(workdir+"hour_01.nc", workdir+"hourly_01.nc")
            os.rename(workdir+"hour_07.nc", workdir+"hourly_07.nc")
            os.rename(workdir+"hour_13.nc", workdir+"hourly_13.nc")
            os.rename(workdir+"hour_19.nc", workdir+"hourly_19.nc")

            outfile2=workdir+"hourly_%04d%02d.nc" % (year, month)
            cdo.mergetime(input=workdir+"hourly_??.nc", output=outfile2)

            if year == yearEnd and month == monthEnd:
                # Done with the last month.
                break

        print ("Almost done... merge and then copy.")
        sys.stdout.flush()
            
        infile=workdir+"hourly_%04d??.nc" % (year)
        allrad=cdo.mergetime(input=infile)

        # Make sure it is really only one year.
        yearfile=workdir+"UERRA_exact_one_year_%04d.nc" % (year)
        cdo.selyear(year, input=allrad, output=yearfile, options = '-O')
        
        solfile =workdir+"solrad_y"+str(year)+".nc"
        lonfile =workdir+"lwdrad_y"+str(year)+".nc"
        cdo.setname("SOLRAD",   input=" -divc,3600 -selname,ssrd "+yearfile, output=solfile)
        cdo.setname("LWRAD_DN", input=" -divc,3600 -selname,strd "+yearfile, output=lonfile)

        shutil.copy(solfile, finaldir+"Radiation/")
        shutil.copy(lonfile, finaldir+"Radiation/")



def humidity(yearStart, monthStart, yearEnd, monthEnd, workdir, downdir, finaldir):
    """
    Prepare specific humidity.
    Change from relative to specific humidity based on the August-Roche-Magnus formula.
    https://en.wikipedia.org/wiki/Clausius-Clapeyron_relation, 2017-08-10
    with e_s(T) saturation vapor pressure [in hPa]
    e_s(T) = 6.1094*exp((17.625*TAIR)/(243.04+TAIR))   !temperature in Celsius
    and vapor pressure [e]
    e = e_s(T) * RH         !RH=0...1
    and specific humidity s
    s = 0.622*e / (p-0.378*e)
    """
    for year in list(range(yearStart, yearEnd + 1)):
        print "Working on humidity, year: " , year
        # T2m and MSLP are needed for computation
        # copy these files from the final destination.
        # Hence, these parameters need to be prepare before!!!
        cpfile=finaldir+"T2m/tair_y%04d.nc" % (year)
        shutil.copy(cpfile, workdir)
        split_file=workdir+"tair_y%04d.nc" % (year)
        outfile=workdir+"tair_y%04d_" % (year)
        cdo.splitmon(input=split_file, output=outfile)

        cpfile=finaldir+"MSLP/pres_y%04d.nc" % (year)
        shutil.copy(cpfile, workdir)
        split_file=workdir+"pres_y%04d.nc" % (year)
        outfile=workdir+"pres_y%04d_" % (year)
        cdo.splitmon(input=split_file, output=outfile)

        for month in list(range(monthStart, 13)):
            print "month: ", month
            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

# 1. Reduce the domain to fit the Baltic/North Sea.
            fc_infile =downdir+"UERRA_fc_%04d%02d.grb" % (year, month)
            outfile2  =workdir+"UERRA_fc_%04d%02d.nc" % (year, month)

            cdo.selindexbox("200,405,280,470", 
                            input=" -setgridtype,curvilinear -selname,r "+fc_infile, 
                            output=outfile2, options = '-f nc')

            cdo.merge(input=workdir+"pres_y%04d_%02d.nc" % (year, month) + " " 
                      +workdir+"tair_y%04d_%02d.nc" % (year, month) + " " + outfile2,
                      output=workdir+"all_param_%04d_%02d.nc" % (year, month), 
                      options = ' -O')
 
            cdo.expr('\'SHUMID=0.622*(6.1094*exp((17.625*(TAIR-273.15))/(243.04+(TAIR-273.15)))*r/100)/(PRES/100-0.377*(6.1094*exp((17.625*(TAIR-273.15))/(243.04+(TAIR-273.15)))*r/100));\'' , 
                     input= workdir+"all_param_%04d_%02d.nc" % (year, month), 
                     output=workdir+"shum_%04d_%02d.nc" % (year, month))

            if year == yearEnd and month == monthEnd:
                # Done with the last month.
                break

# Merge all monthly files into a yearly file and copy to final destination
        cdo.mergetime(input=workdir+"shum_%04d_??.nc" % (year), 
                      output=workdir+"shumid_y%04d.nc" % (year)) 
        shutil.copy(workdir+"shumid_y%04d.nc" % (year), finaldir+"/Humidity/shumid_y%04d.nc" % (year))



