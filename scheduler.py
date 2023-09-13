from pcb import PCB
from algorithms import shortest_job_first, first_come_first_serve, round_robin, priority
from output import append_to_txt_file, write_to_txt_file

class Scheduler:
    def __init__(self, algorithm, traces, timeslot=None):
        self.__traces = traces
        self.__ready_queue = []
        self.__algorithm = algorithm
        self.__timeslot = timeslot
        self.__runtime = 0
        self.__running_process = None

        # Add headers to output files.
        write_to_txt_file("./output/all_stats.txt", ["Process-ID", "Wait Time", "Response Time", "Turnaround Time"])
        write_to_txt_file("./output/wait_times.txt", ["Process-ID", "Wait Time"])
        write_to_txt_file("./output/schedule.txt", ["Time slot", "Process ID", "CPU Burst"])




    def sortReadyQueue(self):
        match self.__algorithm:
            case "fcfs":
                self.__ready_queue = first_come_first_serve(self.__ready_queue)
            case "sjf":
                self.__ready_queue = shortest_job_first(self.__ready_queue)
            case "rr-fcfs":
                self.__ready_queue = round_robin(self.__ready_queue, "fcfs")
            case "rr-sjf":
                self.__ready_queue = round_robin(self.__ready_queue, "sjf")
            case "rr-priority":
                self.__ready_queue = round_robin(self.__ready_queue, "priority")
            case "priority":
                self.__ready_queue = priority(self.__ready_queue)
            case _:
                raise ValueError(f"Algorithm {self.__algorithm} is not allowed. Please see README.txt.")

    def runProcess(self):
        if self.__running_process:
            # If there's a running process:
            if self.__timeslot and self.__running_process.getCPU_burst() > self.__timeslot:
                # If the process has a remaining burst time greater than the timeslot, decrement by timeslot
                increment = self.__timeslot
                self.__running_process.setCPU_burst(self.__running_process.getCPU_burst() - increment)
            else:
                # If the process has a remaining burst time less than or equal to the timeslot, decrement by remaining burst
                increment = self.__running_process.getCPU_burst()
                self.__running_process.setCPU_burst(0)
        else:
            # If there's no running process, calculate time until the next process arrival
            increment = self.__traces[0].getArrival_time() - self.__runtime

        return increment

    def outputOnTermination(self, pcb):
        # Calculate response time, turnaround time, and wait time for a terminated process
        response_time = pcb.getFirst_run() - pcb.getArrival_time()
        turnaround_time = self.__runtime - pcb.getArrival_time()
        wait_time = turnaround_time - pcb.getOriginal_cpu_burst() - pcb.getCPU_burst()

        # Append process statistics to output files
        append_to_txt_file("./output/wait_times.txt", [pcb.getPID(), wait_time])
        append_to_txt_file("./output/all_stats.txt", [pcb.getPID(), wait_time, response_time, turnaround_time])

    def run(self):
        # Add processes from traces with arrival time <= current runtime to the ready queue
        while len(self.__traces) > 0 and self.__traces[0].getArrival_time() <= self.__runtime:
            process = self.__traces.pop(0)
            self.__ready_queue.append(process)
        
        if len(self.__ready_queue) != 0:
            if self.__running_process:
                self.__ready_queue.append(self.__running_process)
            self.sortReadyQueue()
            self.__running_process = self.__ready_queue.pop(0)
            if not self.__running_process.getFirst_run():
                self.__running_process.setFirst_run(self.__runtime)
            self.__running_process.setLast_run(self.__runtime)

        if self.__running_process:
            # Log running process information in the schedule.txt file
            append_to_txt_file("./output/schedule.txt", [self.__runtime, self.__running_process.getPID(), self.__running_process.getCPU_burst()])
        
        increment = self.runProcess()
            
        self.__runtime += increment

        if self.__running_process:
            if self.__running_process.getCPU_burst() == 0:
                # Output statistics for a terminated process
                self.outputOnTermination(self.__running_process)
                self.__running_process = None
        
        # Check if both traces and ready_queue are empty and there is no running process terminate simulation
        return len(self.__traces) != 0 or len(self.__ready_queue) != 0 or self.__running_process