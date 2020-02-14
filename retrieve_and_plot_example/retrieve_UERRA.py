#!/usr/bin/env python
import cdsapi

# Change the variables for year, month and day to a time as you wish
year = ['2005']
month = ['01']
day = ['6','7','8','9','10']

c = cdsapi.Client()

def uerra_request(reqYear, reqMonth, reqDates):
    """
        A UERRA request for the variables in the array 'variables'.
        Origin uerra_harmonie, single levels, analysis fields.
        Request cost per day is 8 fields, ca 5 Mbytes.
    """

    c.retrieve(
        'reanalysis-uerra-europe-single-levels',
        {
            'origin': 'uerra_harmonie',
            'variable': ['10m_wind_speed','mean_sea_level_pressure'],
            'year': reqYear,
            'month': reqMonth,
            'day': reqDates,
            'time': ['00:00','06:00','12:00','18:00'],
            'format': 'grib',
        },
        'download.grib')

if __name__ == '__main__':
    uerra_request(year, month, day)