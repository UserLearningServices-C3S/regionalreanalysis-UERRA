#!/bin/bash -e

subdir=(Wind)
subdir2=(T2m Humidity)


dir=$1
year=$2
eyear=$3


while [ $year -le $eyear ]; do
    for xsubdir in ${subdir[*]}; do
	cd $dir/$xsubdir/
	for i in `ls *$year*.nc`; do
	    height=`ncdump -h $i | grep 'float' | grep height`
	    if [ ! -z "$height" ]; then
		echo $i
		ncwa -O -a height $i tmp.nc
		ncks -O -C -x -v lon_bnds,lat_bnds,time_bnds,height tmp.nc $i
		rm tmp.nc
	    fi
	done
    done
    year=$(( $year + 1 ))
done



year=$2
while [ $year -le $eyear ]; do
    for xsubdir in ${subdir2[*]}; do
	cd $dir/$xsubdir/
	for i in `ls *$year*.nc`; do
	    height=`ncdump -h $i | grep 'float' | grep height`
	    if [ ! -z "$height" ]; then
		echo $i
		ncwa -O -a height_2 $i tmp.nc
		ncks -O -C -x -v lon_bnds,lat_bnds,time_bnds,height_2 tmp.nc $i
		rm tmp.nc
	    fi
	done
    done
    year=$(( $year + 1 ))
done
