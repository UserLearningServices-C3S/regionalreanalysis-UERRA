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
        A UERRA request for origin SMHI, model level, analysis fields.
        Request cost per day is 1040 fields, 713 Mbytes.
    """
    server.retrieve({
        "class": "ur",
        "stream": "oper",
        "type": "an",
        "dataset": "uerra",
        "origin" : "eswi",
        "date": requestDates,
        "expver": "prod",
        "levtype": "ml",
        "levelist": "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65",
        "param": "130/131/132/133",
        "target": target,
        "time": "00/06/12/18"
    })


if __name__ == '__main__':
    retrieve_uerra_eswi()
