-====Input Configuration====-

Within the "./input" directory, you will find a file named `conf.xml`. This file serves as the configuration document for your CPU scheduler simulator. It defines various parameters and settings for the simulation. Here's a breakdown of the elements within `conf.xml`:

Algorithm

The `<algorithm>` tag allows you to choose the sorting algorithm for the ready queue. There are six valid inputs for the `algorithm` element, and the letter case does not matter:

- `fcfs` (First Come First Serve)
- `sjf` (Shortest Job First)
- `priority` (Priority)
- `rr-fcfs` (Round Robin First Come First Serve)
- `rr-sjf` (Round Robin Shortest Job First)
- `rr-priority` (Round Robin Priority)

Choose the desired algorithm by specifying one of the above options within the `<algorithm>` tags.

Trace File Path

The `<trace_file_path>` tag specifies the file path for the trace file that contains information about processes, their arrival times, CPU burst times, and, if necessary, priority values. This path is relative to the location of the `main.py` file in your project.

By default, the trace file is expected to be located in the `/input` directory. However, you can change the file path in `conf.xml` to point to a different location as needed.

Time Slice

The `<time_slice>` tag allows you to configure the time slice for the CPU scheduler. You can set it to either a positive integer to represent a preemptive kernel with time slices or set it to `Null` to indicate a non-preemptive kernel.

Trace File (trace.txt)

The trace file, typically named `trace.txt`, is used by the CPU scheduler simulator to define the processes to be simulated, their arrival times, CPU burst times, and, if required by the selected algorithm, priority values. Here's an example of the format for the `trace.txt` file:

------------------------------
Process ID, CPU Burst, Arrival Time, Priority
0,2,0
1,4,1
2,3,2
3,22,3
------------------------------


- The first line of the `trace.txt` file is reserved for headers, specifying the information columns.
- For all subsequent lines, you need to provide the following information:
  - Process ID: An identifier for the process.
  - CPU Burst: The time it takes for the process to complete its execution.
  - Arrival Time: The time at which the process arrives.
  - Priority (optional): Required only if the selected algorithm is `priority` or `rr-priority`. Specify the priority value for each process.

Please ensure that your `trace.txt` file adheres to this format.

These configuration settings, combined with the trace file, will govern the behavior of your CPU scheduler simulator.


-====Output Files====-

The CPU scheduler simulator generates three output files, all of which can be found in the "/outputs" directory.

1. all_stats.txt

`all_stats.txt` contains individual performance metrics for the processes that were run in the simulation. These metrics are as follows:

- Wait Time: The total time a process spends waiting in the ready queue before it gets CPU time.
- Response Time: The time it takes for a process to receive CPU time from the moment it arrives.
- Turnaround Time: The total time taken by a process from arrival to completion.

Here's an example of how `all_stats.txt` would look after the simulation:

------------------------------
Process-ID,Wait Time,Response Time,Turnaround Time
0,0,0,2
1,1,1,5
2,4,4,7
3,6,6,28
------------------------------

- The first row contains headers indicating the content of each column.
- Subsequent rows represent individual processes, with the following information in order: Process ID, Wait Time, Response Time, and Turnaround Time.

2. wait_time.txt

`wait_time.txt` is similar to `all_stats.txt` but focuses solely on the wait times of the processes. It contains the following information:

- Process ID: An identifier for the process.
- Wait Time: The total time the process spends waiting in the ready queue.

Here's an example of how `wait_time.txt` would look:

------------------------------
Process-ID,Wait Time
0,0
1,1
2,4
3,6
------------------------------

- The first row includes headers for clarity.
- Subsequent rows list individual processes, with their respective Process ID and Wait Time.

3. schedule.txt

`schedule.txt` provides a detailed log of the running processes, including when they were scheduled and their remaining CPU burst times. It contains the following information:

- Time Slot: The time slot indicates how much time has elapsed since the simulator started.
- Process ID: An identifier for the process being scheduled.
- CPU Burst: The remaining CPU burst time for the process.

Here's an example of how `schedule.txt` would look:

------------------------------
Time slot,Process ID,CPU Burst
0,0,2
2,1,4
5,1,1
6,2,3
9,3,22
12,3,19
15,3,16
18,3,13
21,3,10
24,3,7
27,3,4
30,3,1
------------------------------

- The first row contains headers, indicating the content of each column.
- Subsequent rows provide information about the processes scheduled at various time slots, including Time Slot, Process ID, and CPU Burst.


-====Execution====-

To run the CPU scheduler simulator, follow these steps:

1. Open your console or terminal.

2. Navigate to the directory containing the simulator's source code and configuration files.

3. Ensure that you have configured the `conf.xml` file in the "./input" directory to specify the desired simulation parameters, including the selected algorithm, trace file path, and time slice (if applicable).

4. Run the `main.py` script from the console by entering the following command:

--------------
python3 main.py
--------------

The simulator will execute based on the settings provided in the conf.xml file and the input data from trace.txt.

Once the simulation is complete, you will find the output files, including all_stats.txt, wait_time.txt, and schedule.txt, in the "./outputs" directory.