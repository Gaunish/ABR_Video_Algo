# Task3: Replace the legacy chunk
For the fluctuating available network bandwidth, the ABR can replace a previously downloaded low-quality chunk. In this task, we provide the **best speed** ABR to download the chunks, but after each chunk is downloaded, you can use CustomReplace.py to check whether there is a chunk that can be replaced with the available bandwidth.

The return values of this function should be the relative postion of the replacable chunck, and new quality.

You need to submit **CustomReplace.py** in this task.

Based on the simulation result, please answer the following questions:

1. How much better total played bitrate your replacement method can achieve?
2. Does your replacement method prolong the total play time, why?

**Rubric**: `(total played time <=298) and (total played bitrate >= 484583)`

