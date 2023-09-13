from scheduler import Scheduler
class Simulator(Scheduler):
    def __init__(self, algorithm, traces, timeslot=None):
        super().__init__(algorithm, traces, timeslot)
    def runSimulation(self):
        continue_running = True
        i = 0
        while continue_running:
            continue_running = super().run()