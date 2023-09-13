#from typing import Text
from pcb import PCB
from simulator import Simulator
import xml.etree.ElementTree as ET

if __name__ == "__main__":

    tree = ET.parse('./input/conf.xml')
    root = tree.getroot()
    
    trace_filepath = root.find('trace_file_path').text.lower()
    time_slice_input = root.find('time_slice').text.lower()
    algorithm = root.find('algorithm').text.lower()

    if time_slice_input == "null":
        time_slice = None
        if algorithm[:2] == "rr":
            raise ValueError("Time Slice must not be set to a positive integer if a round robin algorithm is used.")
    elif time_slice_input.isdigit() & int(time_slice_input) > 0:
        time_slice = int(time_slice_input)
    else:
        raise ValueError("time_slice in conf.xml must either be \"None\" or a positive integer.")
    
    traces = []
    with open(trace_filepath, "r") as traces_file:
        next(traces_file)  # Skip the header line
        for line in traces_file:
            fields = line.strip().split(",")  # Split the line into fields
            if (algorithm == "priority" or algorithm == "rr-priority") and len(fields) != 4:
                raise ValueError("trace.txt must contain 4 values per line if priority is enabled.")
            if len(fields) == 3 or len(fields) == 4:
                traces.append(PCB(*fields))

    sorted_traces = sorted(traces, key=lambda pcb: pcb.getArrival_time())
    
    sim = Simulator(algorithm, sorted_traces, time_slice)
    sim.runSimulation()