
Design section desribes the conceptual design of GridAPPS-D's managers. Each manager is resposible for executing specific groupd of functions.  

Process Manager
^^^^^^^^^^^^^^^

Process Manager is responsible for starting, managing and stopping processes. 
All the requests to start a process like starting a simulation or querying a data store is received by Process Mananger. 
After receiving a request to start a process it forwards the request to corresponding manager for execution. 
Process Manager keeps track of all the processes and reports their status when requested.

This implements Internal Function Definition- 402 Process Manager
 
Log Manager
^^^^^^^^^^^
TBD

Simulation Manager
^^^^^^^^^^^^^^^^^^
TBD

Configuration Manager
^^^^^^^^^^^^^^^^^^^^^
TBD






