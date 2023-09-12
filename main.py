from typing import Text
from pcb.py import PCB
from scheduler.py import Scheduler
import xml.etree.ElementTree as ET

if __name__ == "__main__":

    tree = ET.parse('./input/conf.xml')
    root = tree.getroot()
    
    trace_filepath = root.find('trace_file_path').text

    traces = []
    with open(trace_filepath, "r") as traces_file:
        next(traces_file)
        traces_txt = Text.reader(traces_file, delimiter=",")
        for row in traces_txt:
            traces.append(PCB(*row))
    
    