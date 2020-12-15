import time
from datetime import datetime
import argparse
from functions import hours2seconds, str2bool
import os

# Default values:
start_time = '06:00'
repeat_delay = 4
set_job = 'date'
repeat = True

def loadUserOptions():
    parser = argparse.ArgumentParser()
    parser.add_argument("-T", "--start_time", help="set start time in the format hh:mm (default is 06:00)")
    parser.add_argument("-H", "--repeat_delay", help="set start every how many hours between two syncronisation (default is 4)")
    parser.add_argument("-J", "--set_job", help="set the job you want to give to the prompt")
    parser.add_argument("-R", "--repeat", help="set if repeat the job (default is True)")
    args = parser.parse_args()
    if args.start_time:
        global start_time
        # start_time = datetime.strptime(start_time, '%H:%M')
        start_time = args.start_time
    if args.repeat_delay:
        global repeat_delay
        repeat_delay = float(args.repeat_delay)
    if args.set_job:
        global set_job
        set_job = args.set_job
    if args.repeat:
        global repeat
        repeat = str2bool(args.repeat)

def timeFromNow(start_time):
    fmt = '%H:%M'
    now_time = datetime.now().strftime("%H:%M")
    tdelta = datetime.strptime(start_time, fmt) - datetime.strptime(now_time, fmt)
    return tdelta

def terminalJob(command):
    if os.name == 'nt':
        os.system('cmd /c "' + command + '"')
    if os.name == 'posix':
        os.system(command)

loadUserOptions()
t_delta = timeFromNow(start_time)
print('Countdown for the next job: %s' % t_delta)
time.sleep(t_delta.seconds)

if not repeat:
    terminalJob(set_job)
    exit()

# this loop works 24h 
while repeat:
    terminalJob(set_job)
    time.sleep(hours2seconds(repeat_delay))
    
