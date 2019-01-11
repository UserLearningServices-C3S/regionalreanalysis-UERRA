#!/usr/bin/env python

import cdsapi
import calendar

c = cdsapi.Client()

def retrieve_uerra_eswi():
    """
       A function to demonstrate how to iterate over several years and months etc
       for a particular UERRA request for origin SMHI.
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
            numberOfDays = calendar.monthrange(year, month)[1]
            targetFile = "ofile_%04d%02d.grb" % (year, month)
            requestDates = ['{:02}'.format(i) for i in range(1, numberOfDays+1)]
            requestMonth = '{:02}'.format(month)
            requestYear = '{:04}'.format(year)
            uerra_eswi_request(requestYear, requestMonth, requestDates, targetFile)

def uerra_eswi_request(reqYear, reqMonth, reqDates, target):
    """
        A UERRA request for 2 metre temperature every 6th hour.
        Origin SMHI, surface level, analysis fields.
        Request cost per day is 4 fields, 1.8 Mbytes.
    """

    c.retrieve(
        'reanalysis-uerra-single-levels',
        {
            'format':'grib',
            'variable':'2m_temperature',
            'year':reqYear,
            'month':reqMonth,
            'day':reqDates,
            'time':['00:00','06:00','12:00','18:00'],
            'origin':'smhi'
        },
        target)

if __name__ == '__main__':
    retrieve_uerra_eswi()
