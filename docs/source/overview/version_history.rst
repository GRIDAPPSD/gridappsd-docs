.. _version_history:


Release History
---------------

Version: Release Cycle 1 (RC1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Release Date: May 2017

Version description: This is the first version for internal release of GridAPPS-D platform. 
This is not ready for public use yet.

Functional requirements covered in this release:

* 102/202 Command Interface

* 301 Real-time Simulation Data

* 310 Hosted Application, but short-cutting the registration process (partial)

* 401 Distribution Co-Simulator (partial)

* 402 Process Manager (partial)

* 404 Data Manager (partial)

* 405 Simulation Manager (partial)

* 406 Power System Model Manager (partial)

* 413 Platform Manager (encapsulating 401 and 403-406)


Version: 2019.01.0
^^^^^^^^^^^^^^^^^^

Release Date: January 2019

GridAPPS-D v2019.01.0 release contains following features/updates:

1. **Platform updates:**

    - Simulation can run as fast as possible as well as real-time (every 3 seconds)
    - Simulation can run with houses if present in the model.
    - Following components can be controlled while the simulation is running:
        + Open or close capacitors
        + Open or close switches
        + Change tap setting for regulators
        + Changing control modes for regulators
        + Change inverter P & Q output
        + Set control modes for regulators and capacitors
    - Simulation request creates the input weather file. 
    - gridappsd-python: 
        + (@Craig: list out updates here)
    - cim2glm:
        + Optional house cooling load components
    - Single-phase power electronics and fuse ratings
    - Inverter parameters changed from rotating machines to power electronics
    - Solar and storage
    - Measurements exported to the circuit metadata (JSON file); SimObject identifies the corresponding GridLAB-D object
    - Supplemental scripts to populate feeder with measurements and houses
    - Rotating machines, only parameters essential for the UAF lab microgrid
    - In GridLAB-D export of loads, each node or triplex_node will have separate submeters for houses, PV inverters, battery inverters and rotating machines, i.e., not patterned after net metering
    
    
2. **Data updates:**

       2.1 Power grid models:
       
         - Power grid models are stored in blazegraph database in its own docker container.
         - Following models are pre-loaded 
            + EPRI_DPV_J1
            + IEEE123
            + IEEE13
            + R2_12_47_2
            + IEEE8500
            + IEEE123_pv
         - User can upload customized model (@Tara: attach readthedocs link)
             
       2.2 Weather:
       
         - Weather data in stored in InfluxDB using Proven.
         - InfluxDB has its own docker container with pre-loaded weather data.
         - API added to query weather data. 
         - Feature added to create weather file for a simulation 
         - Details of pre-loaded weather data in current release: (@Eric: meta-data details please)
                           
       2.3 Simulation Input
       
         - Simulation input commands sent by applications/services are stored in InfluxDB using Proven.
         - API added to query input data.
             
       2.4 Simulation Output
       
         - Output from simulator is stored in InfluxDB using Proven.
         - API added to query output data.
             
       2.5 Logs 
       
         - API added for query based on pre-defined filters or custom SQL string. 
         - Changed logs to have epoch time format. 

                  
3. **Applications and Services:**

  3.1 Viz
    
    - User can select to run simulation at real-time or as fast as possible
    - User can select to add houses in the simulation
    - User can open or close switches and capacitors by clocking on them
    - Cleaner display of log messages while simulation is running
    - User can query simulation logs after simulation is done.
    - Toggle switches open/close 
    - Querying logs through Viz (still working on this)
    - Bug fixes
       + fixed the stomp client in Viz, 
       + added missing capacitor labels
       + redirect non-root urls to root (localhost:8080)
             
  3.2 Sample application: (@Craig/Andy: please review/add)
  
    - Source code at https://github.com/GRIDAPPSD/gridappsd-sample-app
    - Sample app runs in its own container
    - Register with gridapps-d platform when platform start.
    - Re-register automatically if platform restart.
    - Redundant log messages removed.
    - Works with user selected model instead of hard-coded ones. 
    
  3.3 State Estimator (TODO: @Andrew)
    
  3.4 RDRD(WSU) (TODO: @Anamika/Shiva)
  
  3.5 DER Dispatch (@TODO: @Jeff)
  
  3.6 VVO (@TODO: @Brandon)
  
5. **Source Code:**

  - goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.01.0
  - gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.01.0
  - gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.01.0
  - cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.01.0
  - proven-cluster - https://github.com/pnnl/proven-cluster (@Eric: link for release branches)
  - proven-docker - https://github.com/GRIDAPPSD/proven-docker
  - proven-client - https://github.com/pnnl/proven-client
  - proven-message - https://github.com/pnnl/proven-message
  - fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
  - gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.01.0
  - gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
  - sample-app https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.01.0

6. **Docker Container:**

GridAPPS-D creates and starts following docker containers: 

  - gridappsd/gridappsd:2019.01.0 - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.01.0
            + proven-client - https://github.com/pnnl/proven-client
            + cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.01.0
            + gridappsd/gridappsd-base:master - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.01.0
            + zeromq - http://download.zeromq.org/zeromq-4.0.2.tar.gz
            + zeromq_czmq - https://archive.org/download/zeromq_czmq_3.0.2/czmq-3.0.2.tar.gz
            + activemq - http://mirror.olnevhost.net/pub/apache/activemq/activemq-cpp/3.9.4/activemq-cpp-library-3.9.4-src.tar.gz 
            + fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
            + gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
  - gridappsd/influxdb:2019.01.0 - https://github.com/GRIDAPPSD/gridappsd-data/tree/releases/2019.01.0
            + influxdb:latest - https://hub.docker.com/_/influxdb
  - gridappsd/blazegraph - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.01.0
            + lyrasis/lbazegraph:2.1.4 - https://hub.docker.com/r/lyrasis/blazegraph
  - gridappsd/proven - https://github.com/GRIDAPPSD/proven-docker
            + proven-cluster - https://github.com/pnnl/proven-cluster/tree/v1.3.3
            + proven-message - https://github.com/pnnl/proven-message/tree/v1.3.1
  - gridappsd/sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.01.0
            + gridappsd/app-container-base - (TODO: @Craig can you provide the repository?)
  - gridappsd/viz:2019.01.0 - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.01.0
  - redis:3.2.11-alpine - https://hub.docker.com/_/redis
  - mysql/mysql-server:5.7 - https://hub.docker.com/_/mysql

  
Version: 2019.02.0
^^^^^^^^^^^^^^^^^^

Release Date: Feb 2019

1. Fixed Bugs:

  - PROVEN - It can now store simulation input and output which can scale for IEEE8500 model.
  - PROVEN - It can store data with real-time simulation run.
  - PROVEN - Increased max data limit to unlimited.
  - FNCS Goss Bridge - Corrected the timestamp format in simulation logs.
  
2. New Features:

  - Viz - User can query log data from MySQL using Viz menu.
  - Viz - Added menu to operate switches.
  - FNCS GOSS bridge can do execute pause, resume and stop operations for simulation. 
  - Update PROVEN docker container for automated builds.
  

3. Source Code:

  - goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.02.0
  - gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.02.0
  - gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.02.0
  - cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.02.0
  - proven-cluster - 1.3.4 https://github.com/pnnl/proven-cluster/releases/tag/v1.3.4
  - proven-client - 1.3.4 https://github.com/pnnl/proven-client/releases/tag/v1.3.4 
  - proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.1 
  - proven-docker - https://github.com/GRIDAPPSD/proven-docker
  - fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
  - gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.02.0
  - gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
  - sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.02.0

4. **Docker Container:**

GridAPPS-D creates and starts following docker containers: 

  - gridappsd/gridappsd:2019.01.0 - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.01.0
            + proven-client - https://github.com/pnnl/proven-client
            + cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.01.0
            + gridappsd/gridappsd-base:master - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.01.0
            + zeromq - http://download.zeromq.org/zeromq-4.0.2.tar.gz
            + zeromq_czmq - https://archive.org/download/zeromq_czmq_3.0.2/czmq-3.0.2.tar.gz
            + activemq - http://mirror.olnevhost.net/pub/apache/activemq/activemq-cpp/3.9.4/activemq-cpp-library-3.9.4-src.tar.gz 
            + fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
            + gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
  - gridappsd/influxdb:2019.01.0 - https://github.com/GRIDAPPSD/gridappsd-data/tree/releases/2019.01.0
            + influxdb:latest - https://hub.docker.com/_/influxdb
  - gridappsd/blazegraph - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.01.0
            + lyrasis/lbazegraph:2.1.4 - https://hub.docker.com/r/lyrasis/blazegraph
  - gridappsd/proven - https://github.com/GRIDAPPSD/proven-docker
            + proven-cluster - https://github.com/pnnl/proven-cluster/tree/v1.3.3
            + proven-message - https://github.com/pnnl/proven-message/tree/v1.3.1
  - gridappsd/sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.01.0
            + gridappsd/app-container-base - (TODO: @Craig can you provide the repository?)
  - gridappsd/viz:2019.01.0 - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.01.0
  - redis:3.2.11-alpine - https://hub.docker.com/_/redis
  - mysql/mysql-server:5.7 - https://hub.docker.com/_/mysql

Version 2019.03.0
^^^^^^^^^^^^^^^^^
1. Bugs Fixed

	- Sending a command to change set point to the PV inverter has no effect.
	- Time series query return no data after simulation run.
	- Viz: Switch operations not working on Firefox browser. Time on x-axis on plots is not displayed correctly.

2. New Features
		
	- GridAPPS-D – VOLTTRON initial interface created. https://github.com/VOLTTRON/volttron/tree/rabbitmq-volttron/examples/GridAPPS-DAgent
	- Fault injection: Simulator can receive faults. Fault schema created in Test Manager. Workflow for fault processing documented on readthedocs.
	- Viz: Created menu for capacitors, regulators.
	- Proven: Facilitates direct disclosure of JSON messages to Proven via Hazelcast or REST; eliminating need for the proven-message library. Improved throughput and scalability for Proven's data disclosure component.  Disclosed data is now distributed or staged across the cluster to be used by future JET processing pipelines. 

3. Documentation

	- CIM100 documented
	- Steps added for creating and testing an application
	- Updated documentation on Simulation API

4. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.03.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.03.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.03.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.03.0
	- proven-cluster - 1.3.4 https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.3
	- proven-client - 1.3.4 https://github.com/pnnl/proven-client/releases/tag/v1.3.4 
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.3 
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.03.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.03.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.03.0
