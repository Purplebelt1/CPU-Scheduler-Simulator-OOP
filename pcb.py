class PCB:
    def __init__(self, pid, cpu_burst, 
                 arrival_time, last_run, priority=None):
        #Checks if pid is an integer
        if type(pid) != int:
             raise ValueError("PID must be an integer") 
        self.pid = int(pid)

        #Checks if CPU burst is an integer
        if type(cpu_burst) != int:
             raise ValueError("CPU burst must be an integer") 
        self.cpu_burst = int(cpu_burst)

        #Checks if arrival time is an integer
        if type(arrival_time) != int:
             raise ValueError("Arrival time must be an integer") 
        self.arrival_time = int(arrival_time)

        #Checks if last run is an integer
        if type(last_run) != int:
             raise ValueError("Last run must be an integer") 
        self.last_run = int(last_run)

        #Checks if priority is used and priority is an integer
        if priority is not None and type(priority) != int:
             raise ValueError("Priority must be an integer") 
        self.priority = priority

    #Sets formatting for printing a PCB
    def __str__(self):
        if self.priority is not None:
            return f"Process ID: {self.pid}, Arrival Time: {self.arrival_time}, CPU Burst: {self.cpu_burst}, Priority: {self.priority}"
        else:
            return f"Process ID: {self.pid}, Arrival Time: {self.arrival_time}, CPU Burst: {self.cpu_burst}"

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    
    def getPID(self):
        return self.pid
    
    def getCPU_burst(self):
        return self.cpu_burst

    def setCPU_burst(self, cpu_burst):
        self.cpu_burst = cpu_burst
    
    def getArrival_time(self):
        return self.arrival_time

    def getLast_run(self):
        return self.last_run
    
    def getPriority(self):
        return self.priority
