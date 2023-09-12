from pcb import PCB
from algorithms import shortest_job_first, first_come_first_serve, round_robin
from output import append_to_txt_file

class Scheduler:
    def __init__(self, algorithm, traces, timeslot=None):
        self.__traces = traces
        self.__ready_queue = []
        self.__algorithm = algorithm
        self.__timeslot = timeslot
        self.__runtime = 0
        self.__runing_process = None

        append_to_txt_file("./output/all_stats.txt", ["Process-ID,", "Wait Time", "Response Time", "Turnaround Time"])
        append_to_txt_file("./output/wait_time.txt", ["Process-ID,", "Wait Time"])
        append_to_txt_file("./output/schedule.txt", ["Time slot", "Process ID", "CPU Burst"])



    def sortReadyQueue(self):
        match self.__algorithm:
            case "fcfs":
                ready_queue = first_come_first_serve(ready_queue)
            case "sjf":
                ready_queue = shortest_job_first(ready_queue)
            case "rr-fcfs":
                ready_queue = round_robin(ready_queue)
            case "rr-sjf":
                ready_queue = round_robin(ready_queue)
            case "priority":
                ready_queue = priority(ready_queue)
            case _:
                raise ValueError(f"Algorithm {self.__algorithm} is not allowed. Please see README.txt.")

    def runProcess(self):
        if self.__running_process:
            # If there's a running process:
            if self.__timeslot & self.__runing_process.getCPU_burst() > self.__timeslot:
                # If the process has a remaining burst time greater than the timeslot, decrement by timeslot
                increment = self.__timeslot
                self.__runing_process.setCPU_burst(self.__runing_process.getCPU_burst() - increment)
            else:
                # If the process has a remaining burst time less than or equal to the timeslot, decrement by remaining burst
                increment = self.__running_process.getCPU_burst()
                self.__running_process.setCPU_burst(0)
        else:
            # If there's no running process, calculate time until the next process arrival
            increment = self.__traces[0].getArrival_time() - self.__runtime

        return increment
    
    def outputOnTermination(self, pcb):
        response_time = pcb.getFirst_run() - pcb.getArrival_time()
        turnaround_time = self.__runtime - pcb.getArrival_time()
        wait_time = turnaround_time - pcb.getOriginal_cpu_burst() - pcb.getCPU_burst()
        append_to_txt_file("./output/wait_times.txt", [pcb.getPID(), wait_time])
        append_to_txt_file("./output/all_stats.txt", [pcb.getPID(), wait_time, response_time, turnaround_time])

    def run(self):

        if self.__runing_process.getCPU_burst() == 0:
            self.sortReadyQueue()
            self.__runing_process = self.__ready_queue.pop(0)
            if not self.__runing_process.getLast_run():
                self.__runing_process.setLast_run(self.__runtime)
        if self.__runing_process:
            append_to_txt_file("./output/schedule.txt", [self.__runtime, self.__runing_process.getPID(), self.__runing_process.getCPU_burst])
    
        increment = self.runProcess()

        # Add processes from traces with arrival time <= current runtime to ready queue
        while self.__traces[0].getArrival_time() <= self.__runtime:
            process = self.__traces.pop(0)
            self.__ready_queue.append(process)
            
        self.__runtime += increment
        
        # Check if both traces and ready_queue are empty to terminate simulation
        return len(self.__traces) == 0 & len(self.__ready_queue) == 0