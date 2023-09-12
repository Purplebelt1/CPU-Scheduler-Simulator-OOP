from pcb import PCB

def priority(ready_queue):
    if len(ready_queue) == 0:
        return None
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getPriority_time)
    return sorted_queue


def first_come_first_serve(ready_queue):
    if len(ready_queue) == 0:
        return None
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getArrival_time)
    return sorted_queue

def shortest_job_first(ready_queue, type = "NPR"):
    # Please remove type. Scheduler handles that. All I need is the returned queue.
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
  # This is NOT round robin. Round robin sorts a queue in a two step process. There is Primary and secondary sort.
  # This means that anything that is equal in value by the primary sorting parameter is again sorted by the secondary sorting parameter
  # (For this case all we need to worry about is if there are multiple pcbs with a last_run of -1)
  # The primary sort is by last_run for the pcb. Your secodary sort is by fcfs or sjf. This should only be for if you have multiple -1
  # last_run pcbs
    if algorithm == "fcfs":
        first_come_first_serve(ready_queue)
    elif algorithm == "sjf":
        shortest_job_first(ready_queue)
    else:
        raise Exception("Algorithm type not supported")
    
    return None

