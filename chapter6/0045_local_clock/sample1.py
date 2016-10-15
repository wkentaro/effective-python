# -----------------------------------------------------------------------------
from time import localtime, strftime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
from time import mktime, strptime

time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)
# -----------------------------------------------------------------------------
