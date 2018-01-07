 #!/usr/bin/python3 
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
import random
import time
from sim_components import *
class MLFQ(object):

    def __init__(self, num_levels=2):
        self.num_levels = num_levels
        self.queues = []

        for i in range(self.num_levels):
            self.queues.append(Fifo())
			

    def new(self,process):
        """This method admits a new process into the system.
        - **Args:**
            - None
        - **Returns:**
            - None
        """
        self.queues[0].add(process) 
    def runProcessL1(self,process):
        pass	 
        #self.cpu.run_process(self.readyQ.queues[0][0])
        #print "process is running"
        #try:
        #   print(single_cpu.run_process(processes[1]))
        #except:
         #   print("\tError: process already running on cpu")                   
        	

    def __str__(self):
        """Visual dump of class state.
        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return MyStr(self)

###################################################################################################

# === Class: Scheduler===

class Scheduler(object):
    """
    New:        In this status, the Process is just made or created.
    Running:    In the Running status, the Process is being executed.
    Waiting:    The process waits for an event to happen for example an input from the keyboard.
    Ready:      In this status the Process is waiting for execution in the CPU.
    Terminated: In this status the Process has finished its job and is ended.
    """
    def __init__(self, *args, **kwargs):
        self.clock = Clock()
        self.memory = Memory()                  
        self.cpu = Cpu()
        self.accounting = SystemAccounting()
        self.semaphore = SemaphorePool(num_sems=5, count=1)
        self.job_scheduling_queue = Fifo()
        self.scheduling=MLFQ()
        
    def new_process(self,job_info):
        """New process entering system gets placed on the 'job_scheduling_queue'.
        - **Args**:
            - job_info (dict): Contains new job information.
        - **Returns**:
            - None
        """
        self.job_scheduling_queue.add(Process(**job_info))
        #print (self.job_scheduling_queue)
    
		
    def perform_io(self,info):
        """Current process on cpu performs io
        """
        print(info)

    def sem_acquire(self,info):
        """Acquire one of the semaphores
        """
        print(info)

    def sem_release(self,info):
        """Release one of the semaphores
        """
        print(info)

###################################################################################################

# === Class: Simulator===

class Simulator(object):
    """
    Not quite sure yet
    """
    def __init__(self, **kwargs):

        # Must have input file to continue
        if 'input_file' in kwargs:
            self.input_file = kwargs['input_file']
        else:
            raise Exception("Input file needed for simulator")
        
        # Can pass a start time in to init the system clock.
        if 'start_clock' in kwargs:
            self.start_clock = kwargs['start_clock']
        else:
            self.start_clock = 0

        # Read jobs in apriori from input file.
        self.jobs_dict = load_process_file(self.input_file,return_type="Dict")

        # create system clock and do a hard reset it to make sure
        # its a fresh instance. 
        self.system_clock = Clock()
        self.system_clock.hard_reset(self.start_clock)
        
        # Initialize all the components of the system. 
        self.scheduler = Scheduler()    
        self.memory = Memory()
        self.cpu = Cpu()
        self.accounting = SystemAccounting()
        self.readyQ=MLFQ()

        self.event_dispatcher = {
            'A': self.scheduler.new_process,
            'D': self.display_status,
            'I': self.scheduler.perform_io,
            'W': self.scheduler.sem_acquire,
            'S': self.scheduler.sem_release
        }

     #   print(self.jobs_dict)
       # sys.exit()
        #self.display_status(self.jobs_dict)
        while len(self.jobs_dict) > 0:
            # Events are stored in dictionary with time as the key
            key = str(self.system_clock.current_time())
            # If current time is a key in dictionary, run that event.
            if key in self.jobs_dict.keys():
                event_data = self.jobs_dict[key]
                event_type = event_data['event']
                eventmem=event_data['mem_required']
                #print eventmem
                #print event_data
                # Call appropriate function based on event type
                if int(eventmem)<= int(512):
                    print "Event: "+ event_type +" Time: "+key
                    self.event_dispatcher[event_type](event_data)
                else:
				    print "This job exceeds the system's main memory capacity."
                
                if len(self.scheduler.job_scheduling_queue.Q) > 0:
                    req=self.scheduler.job_scheduling_queue.Q[0]['mem_required']
                    avail=self.memory.available()
                    print avail#just print to check
                    print req
                    if (req > avail):
                        print "time"+key
                        self.memory.allocate(self.scheduler.job_scheduling_queue.Q[0])
                        self.readyQ.new(self.scheduler.job_scheduling_queue.Q[0])
                        self.scheduler.job_scheduling_queue.remove()
                print "readyQ len is"
                print len(self.readyQ.queues[0].Q)
                #print self.readyQ.queues[0].Q[0]
                print len(self.readyQ.queues[1].Q)
                if self.readyQ.queues[0].Q:#if there are processes in L1 Q
                    self.readyQ.runProcessL1(self.readyQ.queues[0])#run first process
                elif self.readyQ.queues[1].Q:#l1 is empty then check L2
                    self.readyQ.runProcessL2(self.readyQ.queues[1].Q[0])	
                if len(self.readyQ.queues[0]) > 0:
                    pass
							
                                            
                # Remove job from dictionary
                del self.jobs_dict[key]
            self.system_clock += 1
        #print len(self.scheduler.job_scheduling_queue.Q)
        """
        if self.readyQ.queues[0].Q:
                    self.readyQ.runProcessL1(self.readyQ.queues[0])while len(self.scheduler.job_scheduling_queue.Q)> 0:
            for subp in self.scheduler.job_scheduling_queue.Q:
                time.sleep(.1)
                print("Registering process ....")
                avail = self.memory.available()
                print("  Available: %d" % avail)
                need = subp['mem_required']
                print("  Needed   : %s" % need)
				if 
                    res = self.memory.allocate(subp)
                    self.readyQ.new(self.scheduler.job_scheduling_queue.Q[0])
            #print self.scheduler.job_scheduling_queue
            self.scheduler.job_scheduling_queue.remove()
        """
        #print self.readyQ.queues[0]	
        print self.memory.process_table	
        print self.system_clock		
    def display_status(self,info):
        print(info)

    def __str__(self):
        """
        Visual dump of class state.
        """
        return my_str(self)



if __name__ == '__main__':

    file_name1 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_c.txt'
    file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/t.txt'
    S = Simulator(input_file=file_name2)
    s=Scheduler()
   # print self.s.job_scheduling_queue