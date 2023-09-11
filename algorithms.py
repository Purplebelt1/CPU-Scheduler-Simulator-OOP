import PCB from pcb.py

def first_come_first_serve(ready_queue):
    sorted_queue = sorted(ready_queue, key=lambda pcb: pcb.getArrival_time)
    if len(sorted_queue) == 0:
        return None
    else:
        return sorted_queue

def shortest_job_first(ready_queue):
    sorted_queue = sorted(ready_queue,  key=lambda pcb: pcb.getBurst_time)
    if len(sorted_queue) == 0:
        return None
    else:
        return sorted_queue

def round_robin(ready_queue):
  #not sure if we want this as an option in scheduler or take a second parameter sorting by fcfs or sjf
    return None
