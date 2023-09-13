from pcb import PCB


def priority(ready_queue):
    # Sort the ready queue based on priority in ascending order
    if len(ready_queue) == 0:
        return None # Return None if the queue is empty
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getPriority())
    return sorted_queue

def first_come_first_serve(ready_queue):
    # Sort the ready queue based on arrival time in ascending order (First Come First Serve)
    if len(ready_queue) == 0:
        return None  # Return None if the queue is empty
    sorted_queue = sorted(ready_queue, key=lambda pcb: (pcb.getArrival_time(), -pcb.getLast_run()))
    return sorted_queue  # Return the sorted queue

def shortest_job_first(ready_queue):
    # Sort the ready queue based on CPU burst time in ascending order (Shortest Job First)
    sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getCPU_burst())
    if len(sorted_queue) == 0:
        return None  # Return None if the queue is empty
    else:
        return sorted_queue  # Return the sorted queue

def round_robin(ready_queue, algorithm):
    # Sort the ready queue for Round Robin scheduling with optional secondary sorting
    primary_sort = sorted(ready_queue, key=lambda pcb: pcb.getLast_run())
    secondary_sort = []

    # Identify processes that have not run yet (last_run == -1) and add them to secondary_sort
    for i in primary_sort:
        if i.getLast_run() == -1:
            secondary_sort.append(i)
        else:
            break

    # Depending on the selected algorithm, apply secondary sorting
    if algorithm == "fcfs":
         secondary_sort = first_come_first_serve(secondary_sort)
    elif algorithm == "sjf":
        secondary_sort = shortest_job_first(secondary_sort)
    elif algorithm == "priority":
        secondary_sort = priority(secondary_sort)
    else:
        raise Exception("Algorithm is not supported")

    # Combine the secondary-sorted and primary-sorted queues to get the final sorted queue
    if secondary_sort:
        final_sort = secondary_sort + primary_sort[len(secondary_sort):]
    else:
        final_sort = primary_sort

    return final_sort  # Return the final sorted queue
    
        
    
    
