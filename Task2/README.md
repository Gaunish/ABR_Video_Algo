# Task2: Reduce the Oscillation during the play

Besides playback time and total played bitrate, oscillation can also be a concern. Here, the oscillation means the changes in the played quality. In this task, you are required to implement an Abr to smooth the played quality. In sabre.py, you can cast some class variables in the [__init__() function of the Abr class](https://gitlab.oit.duke.edu/xz234/cs514ece558-lab/-/blob/main/Task2/sabre.py#L471).

$`oscillation`$ is calculated with the following way (suppose quality array's index start with 0, and it has $`T`$ chunks in total):

```math
oscillation = \sum^{T-1}_{t=1} (q_{t} - q_{t-1})^2
```

You need to submit the **CustomAbr.py** and **sabre.py**. 

Based on the simulation result, please answer the following questions:

1. Why does the provided [CustomAbr.py](https://gitlab.oit.duke.edu/xz234/cs514ece558-lab/-/blob/main/Task2/CustomAbr.py) perform badly in $`oscillation`$?
2. How does your CustomAbr.py solve this problem?

**Rubric**: `(oscillation <=25) and (total played bitrate >= 451521) and (total play time <= 597.5)`

