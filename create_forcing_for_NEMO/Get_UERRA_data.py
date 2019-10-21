"""
Module to receive the data from MARS.
"""

import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

import os.path
import sys

from cdo import *
cdo=Cdo()


def retrieve_uerra_forecasts(yearStart, monthStart, yearEnd, monthEnd, download_dir):
    """     
       A function to get all UERRA data from forecast files needed to drive NEMO.

       Needed: yearStart,monthStart,yearEnd,monthEnd, download_dir
               First year and month, last year and month.
    """

    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(1, 13)):
            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

            if year == yearEnd and month > monthEnd:
                # Done with the last month.
                break

            ### Parameters wind direction, wind speed, humidity,
            ### MSLP, short and long wave radiation, and 2m temperature
            target = download_dir+"UERRA_fc_%04d%02d.grb" % (year, month)
            if os.path.isfile(target):
                print target + " is already on place."
                continue


            ### get forecast valid at 00UTC on 1st of January from previous year
            if month == 1:
                syear  = year - 1
                smonth = 12
                sday   = 31
                startDate = '%04d%02d%02d' % (syear, smonth, sday)
            else:
                startDate = '%04d%02d%02d' % (year, month, 1)

            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            requestDates = (startDate + "/TO/" + lastDate)

            print (" ")
            print ("***")
            print "Submit request for forecast data, dates: ", requestDates
            sys.stdout.flush()

            server.retrieve({
                    "class": "ur",
                    "stream": "oper",
                    "type": "fc",
                    "dataset": "uerra",
                    "origin" : "eswi",
                    "date": requestDates,
                    "expver": "prod",
                    "levtype": "sfc",
                    #         direct/speed/humi/SLP/swr/lwr/T2m
                    "param": "260260/207/260242/151/169/175/167",
                    "target": target,
                    "time": "00/06/12/18",
                    "step": "1/2/3/4/5/6",
                    })
 



def retrieve_uerra_precip(yearStart, monthStart, yearEnd, monthEnd, download_dir):
    """     
       A function to get all UERRA data from forecast files needed to drive NEMO.

       Needed: yearStart,monthStart,yearEnd,monthEnd, download_dir
               First year and month, last year and month.
    """

    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(1, 13)):
            sys.stdout.flush()

            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

            if year == yearEnd and month > monthEnd:
                # Done with the last month.
                break

            ### target file as well as interstage files
            target = download_dir+"RR24-12_UERRA_%04d%02d_fc.grb" % (year, month)
            target12 = download_dir+"UERRA_precip_12h_%04d%02d.grb" % (year, month)
            target24 = download_dir+"UERRA_precip_24h_%04d%02d.grb" % (year, month)
            if os.path.isfile(target):
                print target + " is already on place."
                continue


            ### start last day of previous month since we need 24fc for precip
            pmonth = month - 1  # previous month
            if pmonth == 0:
                syear  = year - 1
                smonth = 12
                sday   = 31
                startDate = '%04d%02d%02d' % (syear, smonth, sday)
            else:
                syear  = year
                smonth = pmonth
                sday   = calendar.monthrange(year, pmonth)[1]
                startDate = '%04d%02d%02d' % (syear, smonth, sday)

            if os.path.isfile(target12) and os.path.isfile(target24):
                print "Precipitation data were already downloaded but processing needed."
            else:

#            startDate = '%04d%02d%02d' % (year, month, 1)
                numberOfDays = calendar.monthrange(year, month)[1]
                lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
                requestDates = (startDate + "/TO/" + lastDate)


                print "retrieve precipitation data for ", requestDates
                server.retrieve({
                        "class": "ur",
                        "stream": "oper",
                        "type": "fc",
                        "dataset": "uerra",
                        "origin" : "eswi",
                        "date": requestDates,
                        "expver": "prod",
                        "levtype": "sfc",
                        #         RR/snow
                        "param": "228228/228144",
                        "target": target12,
                        "time": "00/12",
                        "step": "12",
                        })

                print "retrieve precipitation data for ", requestDates
                server.retrieve({
                        "class": "ur",
                        "stream": "oper",
                        "type": "fc",
                        "dataset": "uerra",
                        "origin" : "eswi",
                        "date": requestDates,
                        "expver": "prod",
                        "levtype": "sfc",
                        #         RR/snow
                        "param": "228228/228144",
                        "target": target24,
                        "time": "00/12",
                        "step": "24",
                        })
 
            cdodiff = cdo.sub(input=target24+' '+target12)
            sdate = str(syear)+'-'+str(smonth)+'-'+str(sday)
            cdodate = cdo.settaxis(sdate+',18:00:00,12hours', input=cdodiff)
            cdo.selmon(month, input=' -setmisstoc,0 -setvrange,0,10000 ' + cdodate, output = target)




def retrieve_uerra_analyses(yearStart, monthStart, yearEnd, monthEnd, download_dir):
    """     
       A function to get all UERRA data from analysis files needed to drive NEMO.

       Needed: yearStart,monthStart,yearEnd,monthEnd, download_dir
               First year and month, last year and month.
    """

    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(1, 13)):
            sys.stdout.flush()

            if year == yearStart and month < monthStart:
                # Before the start date.
                continue

            if year == yearEnd and month > monthEnd:
                # Done with the last month.
                break

            ### Parameters wind direction, wind speed, humidity,
            ### MSLP, short and long wave radiation, and 2m temperature
            target = download_dir+"UERRA_an_%04d%02d.grb" % (year, month)
            if os.path.isfile(target):
                print target + " is already on place."
                continue

            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            requestDates = (startDate + "/TO/" + lastDate)

            print "retrieve forecast data for ", requestDates
            server.retrieve({
                    "class": "ur",
                    "stream": "oper",
                    "type": "an",
                    "dataset": "uerra",
                    "origin" : "eswi",
                    "date": requestDates,
                    "expver": "prod",
                    "levtype": "sfc",
                    #         direct/speed/SLP/T2m
                    "param": "260260/207/151/167",
                    "target": target,
                    "time": "00/06/12/18",
                    })

            
