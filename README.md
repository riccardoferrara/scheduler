# scheduler
Schedule a job giving the time of execution and eventually repeat every X hours 
type: scheduler.py -h to have the help below:

usage: scheduler.py [-h] [-T START_TIME] [-H REPEAT_DELAY] [-J SET_JOB]
                    [-R REPEAT]

optional arguments:
  -h, --help            show this help message and exit
  -T START_TIME, --start_time START_TIME
                        set start time in the format hh:mm (default is 06:00)
  -H REPEAT_DELAY, --repeat_delay REPEAT_DELAY
                        set start every how many hours between two
                        syncronisation (default is 4)
  -J SET_JOB, --set_job SET_JOB
                        set the job you want to give to the prompt
  -R REPEAT, --repeat REPEAT
                        set if repeat the job (default is True)
                        
# exemple:
If you want to launch the command "chdir" at 12:00:
  scheduler.py -T 12:00 -R False -J chdir

If you want to repeat this job every two hours:
  scheduler.py -T 12:00 -J chdir -H 2
