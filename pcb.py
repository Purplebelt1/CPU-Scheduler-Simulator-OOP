class PCB:
    def __init__(self, pid, cpu_burst, 
                 arrival_time, priority=None):
        try:
            self.pid = int(pid)
            self.cpu_burst = int(cpu_burst)
            self.original_cpu_burst = int(cpu_burst)
            self.arrival_time = int(arrival_time)
            if priority:
                self.priority = int(priority)
            else:
                self.priority = None
        except:
            raise ValueError("All fields (PID, arrival time, burst time, and priority) must be integers")
        
        if self.cpu_burst < 1:
            raise ValueError("CPU Burst must be greater than 0. Check trace.txt")

        self.first_run = None
        
        self.last_run = -1

    def __str__(self):
        if self.priority is not None:
            return f"Process ID: {self.pid}, Arrival Time: {self.arrival_time}, CPU Burst: {self.cpu_burst}, Priority: {self.priority}"
        else:
            return f"Process ID: {self.pid}, Arrival Time: {self.arrival_time}, CPU Burst: {self.cpu_burst}"

    def setState(self, state):
        self.state = state

    def getFirst_run(self):
        return self.first_run
    
    def setFirst_run(self, value):
        self.first_run = value

    def getState(self):
        return self.state
    
    def getLast_run(self):
        return self.last_run
    
    def setLast_run(self, value):
        self.last_run = value
    
    def getPID(self):
        return self.pid
    
    def getCPU_burst(self):
        return self.cpu_burst
    
    def getOriginal_cpu_burst(self):
        return self.original_cpu_burst

    def setCPU_burst(self, cpu_burst):
        self.cpu_burst = cpu_burst
    
    def getArrival_time(self):
        return self.arrival_time

    def getLast_run(self):
        return self.last_run
    
    def getPriority(self):
        return self.priority
