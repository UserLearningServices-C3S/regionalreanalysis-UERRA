#!/usr/bin/env python

#########################################
### Configure section
#########################################
YYYY1=2017  # first year
MM1  =1     # first month
YYYY2=2017  # last year
MM2  =12    # last month

# workdir: a directory where the processing takes place and
# intermediate data is stored.
# ATTENTION: The workdir will be cleaned while running the script!!!
workdir="/scratch/local/"

# finaldir: That's where the final data will be placed.
finaldir="UERRA/NEMO-Nordic/"

# download_dir: A directory where the raw data downloaded from MARS will be stored.
# This needs to be cleaned manually if you do not want to keep it.
download_dir="Download/For_NEMO/"



#########################################
### Import modules
#########################################

import sys
import os

# This is needed if the job is sent via slurm.
# At least at the NSC HPC centre in Linkoping/Sweden.
if not '' in sys.path:
    sys.path.insert(0,'')

# Modules written for NEMO-Nordic conversion
import Get_UERRA_data
import Convert_for_NEMO


#########################################
### Create directories if needed
#########################################
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)
    print ("Download directory %s created." % download_dir)
else:
    print ("Download directory %s exists already." % download_dir)

if not os.path.isdir(finaldir):
    os.makedirs(finaldir)
    print ("Final directory %s created." % finaldir)
if not os.path.exists(finaldir+'Humidity'):
    os.makedirs(finaldir+'Humidity')
if not os.path.exists(finaldir+'MSLP'):
    os.makedirs(finaldir+'MSLP')
if not os.path.exists(finaldir+'Precip'):
    os.makedirs(finaldir+'Precip')
if not os.path.exists(finaldir+'Radiation'):
    os.makedirs(finaldir+'Radiation')
if not os.path.exists(finaldir+'Snow'):
    os.makedirs(finaldir+'Snow')
if not os.path.exists(finaldir+'T2m'):
    os.makedirs(finaldir+'T2m')
if not os.path.exists(finaldir+'Wind'):
    os.makedirs(finaldir+'Wind')
if not os.path.isdir(workdir):
    os.makedirs(workdir)
    print ("Work directory %s created." % workdir)
else:
    print ("Work directory %s exists already." % workdir)


#########################################
### # Getting forecasts, analysis and precipitation from the MARS archive.
#########################################
Get_UERRA_data.retrieve_uerra_forecasts(YYYY1, MM1, YYYY2, MM2, download_dir)
sys.stdout.flush()   # Write output to standard out immediately - otherwise,
                     # there might be some internal storage before writing the output.
Get_UERRA_data.retrieve_uerra_analyses(YYYY1, MM1, YYYY2, MM2, download_dir)
sys.stdout.flush()
Get_UERRA_data.retrieve_uerra_precip(YYYY1, MM1, YYYY2, MM2, download_dir)
sys.stdout.flush()



#########################################
### Prepare the data for NEMO-Nordic
#########################################
Convert_for_NEMO.precipitation     (YYYY1, MM1, YYYY2, MM2, workdir, download_dir, finaldir)
sys.stdout.flush()
Convert_for_NEMO.radiation (YYYY1, MM1, YYYY2, MM2, workdir, download_dir, finaldir)
sys.stdout.flush()
Convert_for_NEMO.param_with_analysis (YYYY1, MM1, YYYY2, MM2, workdir, download_dir, finaldir)
sys.stdout.flush()
Convert_for_NEMO.humidity (YYYY1, MM1, YYYY2, MM2, workdir, download_dir, finaldir)
sys.stdout.flush()




#########################################
### Remove height dimension for temperature, wind and humidity
#########################################
# Use the bash script with NCO commands to remove the height dimension
script=os.getcwd()+"/remove_height.sh"
print "If you want to remove the height dimension you can use the bash-script remove_height.sh."
print "You can call it as follows..."
print script, finaldir, str(YYYY1), str(YYYY2)
