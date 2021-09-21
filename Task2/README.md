# Task2: Reduce the Oscillation during the play

Besides playback time and total played bitrate, oscillation can also be a concern. In this task, you are required to implement an Abr to smooth the played quality. You need to submit the CustomAbr.py and sabre.py. In sabre.py, you can cast some class variables in the [__init__() function of the Abr class](https://gitlab.oit.duke.edu/xz234/cs514ece558-lab/-/blob/main/Task2/sabre.py#L471).

Score = Total Played Bitrate/ (Total Play Time* Oscillation^2)

**Rubric**: `(oscillation <=25) and (total played bitrate >= 451521)`
