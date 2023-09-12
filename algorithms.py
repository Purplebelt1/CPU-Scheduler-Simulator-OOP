from pcb import PCB


def priority(ready_queue):
    if len(ready_queue) == 0:
        return None
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getPriority_time())
    return sorted_queue


def first_come_first_serve(ready_queue):
    if len(ready_queue) == 0:
        return None
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getArrival_time())
    return sorted_queue

def shortest_job_first(ready_queue):
    # Please remove type. Scheduler handles that. All I need is the returned queue.
        sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst())
        if len(sorted_queue) == 0:
            return None
        else:
            return sorted_queue
            

def round_robin(ready_queue, algorithm):
  #not sure if we want this as an option in scheduler or take a second parameter sorting by fcfs or sjf
  # This is NOT round robin. Round robin sorts a queue in a two step process. There is Primary and secondary sort.
  # This means that anything that is equal in value by the primary sorting parameter is again sorted by the secondary sorting parameter
  # (For this case all we need to worry about is if there are multiple pcbs with a last_run of -1)
  # The primary sort is by last_run for the pcb. Your secodary sort is by fcfs or sjf. This should only be for if you have multiple -1
  # last_run pcbs

    primary_sort = sorted(ready_queue, key = lambda pcb: pcb.getLast_run())
    secondary_sort = []
    for i in primary_sort:
        if i.getLast_run() == -1:
            secondary_sort.append(i)
        else:
            break

    if algorithm == "FCFS":
         secondary_sort = first_come_first_serve(secondary_sort)
    elif algorithm == "SJF":
        secondary_sort = shortest_job_first(secondary_sort)
    else:
        raise Exception("Algorithm is not supported")
    final_sort = secondary_sort + primary_sort[len(secondary_sort):]

    return final_sort
    
        
    
    
