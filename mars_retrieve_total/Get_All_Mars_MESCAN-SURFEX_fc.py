#!/usr/bin/env python

import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

def retrieve_uerra_lfpw():
    """
       A function to demonstrate how to iterate efficiently over several years and months etc
       for a particular UERRA request for origin Meteo France.
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month.
    """
    yearStart = 2015
    yearEnd   = 2015
    monthStart =  1
    monthEnd   = 12
    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(monthStart, monthEnd + 1)):
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "ofile_%04d%02d.grb" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            uerra_lfpw_request(requestDates, target)

def uerra_lfpw_request(requestDates, target):
    """
        A UERRA request for origin Meteo France, surface level, forecast fields.
        Request cost per day is 412 fields, 750 Mbytes.
    """
    server.retrieve({
        "expect": "any",
        "class": "ur",
        "stream": "oper",
        "type": "fc",
        "dataset": "uerra",
        "origin" : "lfpw",
        "date": requestDates,
        "expver": "prod",
        "levtype": "sfc",
        "param": "33/134/146/147/167/169/173/175/176/177/207/235/3066/174008/228141/228144/228228/260242/260260/260264/260364/260430/260509",
        "step": "1/2/3/4/5/6",
        "target": target,
        "time": "00/06/12/18"
    })


if __name__ == '__main__':
    retrieve_uerra_lfpw()
