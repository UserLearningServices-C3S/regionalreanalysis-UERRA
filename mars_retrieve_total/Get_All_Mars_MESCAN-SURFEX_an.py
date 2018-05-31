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
        A UERRA request for origin Meteo France, surface level, analysis fields.
        Request cost per day is 25 fields, 72 Mbytes.
    """
    server.retrieve({
        "expect": "any",
        "class": "ur",
        "stream": "oper",
        "type": "an",
        "dataset": "uerra",
        "origin" : "lfpw",
        "date": requestDates,
        "expver": "prod",
        "levtype": "sfc",
        "param": "167/172/207/228002/228228/260242/260260",
        "target": target,
        "time": "00/06/12/18"
    })


if __name__ == '__main__':
    retrieve_uerra_lfpw()
