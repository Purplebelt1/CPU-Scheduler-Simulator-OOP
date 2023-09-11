class Scheduler:
    def __init__(self, algorithm, ready_queue, traces, timeslot=None):
        self.__traces = traces
        self.__ready_queue = ready_queue
        self.__algorithm = algorithm
        self.__timeslot = timeslot
        self.__runtime = 0
        self.__runing_process = None

    def run(self):
        if self.__running_process:
            # If there's a running process:
            if self.__timeslot & self.__runing_process.get_cpu_burst() > self.__timeslot:
                # If the process has a remaining burst time greater than the timeslot, decrement by timeslot
                increment = self.__timeslot
                self.__runing_process.set_cpu_burst(self.__runing_process.get_cpu_burst() - increment)
            else:
                # If the process has a remaining burst time less than or equal to the timeslot, decrement by remaining burst
                increment = self.__running_process.get_cpu_burst()
                self.__running_process.set_cpu_burst(0)
        else:
            # If there's no running process, calculate time until the next process arrival
            increment = self.__traces[0].get_arrival_time() - self.__runtime

        # Add processes from traces with arrival time <= current runtime to ready queue
        while self.__traces[0].get_arrival_time() <= self.__runtime:
            process = self.__traces.pop(0)
            self.__ready_queue.append(process)

        if self.__runing_process.get_cpu_burst() == 0:
            # If the running process has completed find a new one (need to see algorithms.py before implementation)
            pass
            
        self.__runtime += increment
        
        # Check if both traces and ready_queue are empty to terminate simulation
        return len(self.__traces) == 0 & len(self.__ready_queue) == 0