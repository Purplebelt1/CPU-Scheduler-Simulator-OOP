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
        sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst())
        if len(sorted_queue) == 0:
            return None
        else:
            return sorted_queue
            

def round_robin(ready_queue, algorithm):
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
    
        
    
    
