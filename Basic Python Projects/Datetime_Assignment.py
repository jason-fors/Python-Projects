"""
Simple program to find out if the branches in NYC, Portland and London are open or closed.
The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

Find sout the current times in the Portland HQ and NYC and London branches.
Compares that time with each branch's hours to see if they are open or closed, and 
prints out to the screen the three branches and whether they are open or closed.
"""


from datetime import *
from pytz import *


# Get current UTC time
utc_now = utc.localize(datetime.utcnow())

# Create values for the time in Portland and NYC (London is UTC), and format.
portlandDT = utc_now.astimezone(timezone("US/Pacific"))
portlandTime = portlandDT.time().strftime('%H:%M:%S')
nyDT = utc_now.astimezone(timezone("US/Eastern"))
nyTime = nyDT.time().strftime('%H:%M:%S')
londonTime = utc_now.time().strftime('%H:%M:%S')

# Determine if the London and NYC branch offices are open.
if nyDT.hour < 5 and nyDT.hour >= 9:
    nyOpen = "open"
else:
    nyOpen = "closed"

if utc_now.hour < 5 and utc_now.hour >= 9:
    londonOpen = "open"
else:
    londonOpen = "closed"


# Present times and branch status to user
print("Current local time in Portland is {}.".format(portlandTime))
print("Current local time in New York is {0}. The NYC branch office is {1}.".format(nyTime, nyOpen))
print("Current local time in London is {0}. The London branch office is {1}.".format(londonTime, londonOpen))


