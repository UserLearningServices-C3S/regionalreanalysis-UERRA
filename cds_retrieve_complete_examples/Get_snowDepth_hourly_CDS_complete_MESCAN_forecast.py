#!/usr/bin/env python

import cdsapi
import calendar

c = cdsapi.Client()

def retrieve_uerra():
    """
       A function to demonstrate how to iterate efficiently over several years and months etc
       for a particular UERRA request for origin Meteo France.
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'targetFile' to organise the requested data in files as you wish.
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
            requestDates = ['{:04}'.format(year)+'{:02}'.format(month)+'{:02}'.format(i) for i in range(1, numberOfDays+1)]
            targetFile = "ofile_%04d%02d.grb" % (year, month)
            uerra_request(requestDates, targetFile)


def uerra_request(requestDates, target):
    """
        A UERRA request for snow depth every hour.
        Origin Meteo France, surface level, forecast fields.
        Request cost per day is 24 fields, 46.1 Mbytes.
    """
    c.retrieve(
        'reanalysis-uerra-europe-complete',
        {
          'class':'ur',
          'database':'external',
          'stream':'oper',
          'format':'grib',
          'type':'fc',
          'step':'1/2/3/4/5/6',
          'origin':'lfpw',
          'date': requestDates,
          'expver':'prod',
          'levtype':'sfc',
          'param':'3066',
          'time':'00/06/12/18'
          },
        target)


if __name__ == '__main__':
    retrieve_uerra()
