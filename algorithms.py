import PCB from pcb.py

def first_come_first_serve(ready_queue):
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getArrival_time)
    if len(sorted_queue) == 0:
        return None
    else:
        return sorted_queue

def shortest_job_first(ready_queue, type = "NPR"):
    if(type == "NPR"):
        sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst)
        if len(sorted_queue) == 0:
            return None
        else:
            return sorted_queue
    elif(type == "PRE"):
        sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst)
        if len(sorted_queue) == 0:
            return None
        if(sorted_queue[0].getCPU_burst > pcb.getCPU_burst in sorted_queue):
            sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst)
        return sorted_queue
    else:
        raise Exception("Type is not supported")
            

def round_robin(ready_queue, algorithm):
  #not sure if we want this as an option in scheduler or take a second parameter sorting by fcfs or sjf
    if algorithm == "fcfs":
        first_come_first_serve(ready_queue)
    elif algorithm == "sjf":
        shortest_job_first(ready_queue)
    else:
        raise Exception("Algorithm type not supported")
    
    return None
