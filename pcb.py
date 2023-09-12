class PCB:
    def __init__(self, pid, cpu_burst, 
<<<<<<< HEAD
                 arrival_time, priority=None):
=======
                 arrival_time, last_run, priority=None):
        #Checks if pid is an integer
>>>>>>> 0e5f245886899bbaa39870269aa57385cce3dfe9
        if type(pid) != int:
             raise ValueError("PID must be an integer") 
        self.pid = int(pid)

        #Checks if CPU burst is an integer
        if type(cpu_burst) != int:
             raise ValueError("CPU burst must be an integer") 
        self.cpu_burst = int(cpu_burst)
<<<<<<< HEAD
        self.original_cpu_burst = int(cpu_burst)
        
        if type(arrival_time) != int:
             raise ValueError("Arrival time must be an integer") 
        self.arrival_time = int(arrival_time)
                     
=======

        #Checks if arrival time is an integer
        if type(arrival_time) != int:
             raise ValueError("Arrival time must be an integer") 
        self.arrival_time = int(arrival_time)

        #Checks if last run is an integer
        if type(last_run) != int:
             raise ValueError("Last run must be an integer") 
        self.last_run = int(last_run)

        #Checks if priority is used and priority is an integer
>>>>>>> 0e5f245886899bbaa39870269aa57385cce3dfe9
        if priority is not None and type(priority) != int:
             raise ValueError("Priority must be an integer") 
        self.priority = priority

<<<<<<< HEAD
        self.first_run = None
        self.last_run = -1

=======
    #Sets formatting for printing a PCB
>>>>>>> 0e5f245886899bbaa39870269aa57385cce3dfe9
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
