#!/usr/bin/env python

import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

def retrieve_uerra_eswi():
    """
       A function to demonstrate how to iterate efficiently over several years and months etc
       for a particular UERRA request for origin SMHI.
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month.
    """
    yearStart = 2016
    yearEnd   = 2016
    monthStart =  1
    monthEnd   = 12
    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(monthStart, monthEnd + 1)):
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "ofile_%04d%02d.grb" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            uerra_eswi_request(requestDates, target)

def uerra_eswi_request(requestDates, target):
    """
        A UERRA request for origin SMHI, surface level, forecast fields.
        Request cost per day is 1064 fields, 757 Mbytes.
    """
    server.retrieve({
        "expect": "any",
        "class": "ur",
        "stream": "oper",
        "type": "fc",
        "dataset": "uerra",
        "origin" : "eswi",
        "date": requestDates,
        "expver": "prod",
        "levtype": "sfc",
        "param": "33/49/134/146/147/151/167/169/173/175/176/177/201/202/207/235/3073/3074/3075/228141/228144/228164/228228/260057/260242/260259/260260/260264/260509",
        "target": target,
        "time": "00/06/12/18",
        "step": "1/2/3/4/5/6/9/12/15/18/21/24/27/30"
    })


if __name__ == '__main__':
    retrieve_uerra_eswi()
