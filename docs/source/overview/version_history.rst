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

Version 2019.06.0
^^^^^^^^^^^^^^^^^
1. Bugs Fixed

	- Updated configuration, power grid model and simulation API for CIM100 and app evaluation features addition.
	- All logs are being published to topic instead of queue. 
	- Fixed TypError bug in gridappsd-sensor-service. 
	
2. New Features
		
	- Communication outages: Platform supports input and/or output outage request with simulation for all or some selected power grid components. Outages are initiated and removed at the requested start and end time. 
	- Fault injection: Platform can receive faults with simulation request and forwards them to co-simulator.
	- Viz UI updated: Input form added for communication outage and fault parameter selection. Input form moved from single page to separate tabs.
	- CIM version update: Updated CIM version to CIM100. Added support for Recloser and Breaker in model parsing.
	- New methods in Python wrapper: Capability added in gridappsd-python to start, stop and run a simulation directly from python using yaml or json.
	- Sample app container move to Python 3.6 as default. Updated gridappsd-sample-app to use updated container.
	- Debug scripts added: Added scripts in gridappsd-docker to run platform, co-simulator and simulator in separate terminals for debugging purposes.
	- Sensor service in available in gridappsd container by default. Sensor service is no longer required to be added in gridappsd container via docker-compose file.
	- Default log level is changed from DEBUG to ERROR for limiting the amount of log messages on terminal. 
	- **Breaking API change** - Simulation input and output topics changed in gridappsd-python from FNCS_INPUT_TOPIC to SIMULATION_INPUT_TOPIC and FNCS_OUTPUT_TOPIC to SIMULATION_OUTPUT_TOPIC.
	- **Breaking API change** - Simulation request return a json with simulation id and list of events with their uuids instead of just simulation id.


3. Documentation

	- Using GridAPPS-D documentation section updated for new UI input form with communication outages and faults selection.
	
4. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.06.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.06.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.06.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.06.0
	- proven-cluster - 1.3.4 https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.3
	- proven-client - 1.3.4 https://github.com/pnnl/proven-client/releases/tag/v1.3.4 
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.3 
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.06.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.06.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/feature/1146
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.06.0

Version 2019.07.0
^^^^^^^^^^^^^^^^^


1. Bugs Fixed

	- Time series query filter are updated in the API as well documentation.
	- Selecting houses is now working with the simulation.
	- Following bugs resolved for Viz
	
		- Line name is not based on previously selected values.
		- Removing a selected app-name closes input form
		- Change Event Id to Event tag
		- Change attribute to a multi-value select box
		- Help-text 'Add input item' does not go away on CommOutage tab
		- Object mrid is not correct for multiple phases selection.
	- Pos added for load break switches 

	
2. New Features
		
	- Platform now stores input and output from services and applications output/input in time series data store.
	- Simulation can run with new 9500 node model 
	- Support for synchronous machines added in CIM model in blazegraph.
	- End-to-end fault injecting and processing pipeline is now working.
	- Powergrid api added to query object id, object dictionary and object measurements. 
	- New keys added in glm file to support faults.
	- Viz can display plot for new 9500 model.
	- Added log api in gridappsd-python
	- Measurement for switch positions for all models
	- Explicit setting for manual mode in reg and capacitora in the RegulatingControl.mode attribute.
	- GridAPPS base constainer has folowwing changes
	
		- Switch to openjdk
		- New version of fncs 
		- CZMQ_VERSION changeed to 4.2.0
		- ZMQ_VERSION changes to 4.3.1
		- GridLAB-D switched from feature/1146 to develop
		

3. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.07.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.07.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.07.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.07.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.4
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.5
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.06.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.07.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.07.0
	
	
Version 2019.08.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Viz added capability to select power/voltage/tap measurments for custom plotting
	- Control attributes are back for Capacitors
	- Added Voltage Violation service that publishes list of measurement ids with per unit voltages that are out of range every 15 minutes
	- Viz added display for Voltage Violation service output
	- Viz can display Lot/Long coordinated for 9500 node model.
	- Breaking Change: JSON format for timeseries query response is flattend out
	- Resolved 500 Internal server error for storing simulation input.
	- Houses are created and uploaded to Blazegraph for 123 node model
	- Additonal column process_type added for logs to distinguish process id for simulation
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.08.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.08.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.08.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.08.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.5
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.5
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.08.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.08.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.08.0
	
Version 2019.08.1
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Viz: Change simulation pause button to start button when simulation completes.
	- Bug fix: Simulation id dropdown is not showing selected id in Browse-data-logs.
	- Bug fix: Timeseries queries returning same object multiple times. 
	- Bug fix: Weather file containes only 10 minute data even if simulation duration is longer.
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.08.1
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.08.1
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.08.1
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.08.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.5
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.5
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.08.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.08.1
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.08.1
	
Version 2019.09.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Fault Processing: Faults are working on radial feeders. 
	- Note: Faults are not working on meshed systems. If you have a meshed system then send switch open message to simulate the fault.
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.09.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.09.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.09.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.09.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.5
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.5
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.09.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.09.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.09.0

Version 2019.09.1
^^^^^^^^^^^^^^^^^

1. New Features
		
	- BREAKING CHANGE: Measurements in simulation output message changed from array to dictionary.
	- Simulation are now working for 9500 model with houses.
	- Added missing measurement in blazegraph for houses.
	- Voltage violation service and Viz app updated to work with new simulation output format.
	- Faults are working with 9500 model.
	- Viz app: User can select services and their input parameters in simulation request form.
	- Viz app: Y-axis label corrected if plot value is same during the simulation run.
	- Simulation request API updated to take user input parameters for services. 
	- Timezone corrected for pre-loaded weather data. 
	- Operational limit set on the power grid models in blazegraph. 
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.09.1
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.09.1
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.09.1
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.09.1
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.7
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.6
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.09.1
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.09.1
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.09.1
	
Version 2019.10.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Alarms service created. It publishes alarm whenver a switch or capacitor is opened or closed. It is added as a pre-requisite for sample app.
	- Load profile data pre-loaded in timeseries data store InfluxDB. 
	- Load profile file ieeezipload.player is created dynamically based on simulation start time and duration.
	- API updated in platform and Proven to query load profile data.
	- Timeseries API updated to accept timestamps in seconds instead of micro or nanosecond.
	- Timeseries API updated to accept query filters in an array instead of single value. 
	- Viz app: User can search and highlight objects on network by name and mrid.
	- Viz app: User can re-center network graph.
	- Viz app: Displays alarms in a saperate tab when simulation is running. Notifies when a new alarm is received in alarm tab. 
	- Viz app: User can upload scheduled commands json file with communication outage and faults.
	- Viz app: Switches are displayed as closed/opened based on simulation output value.
	- Viz app: Display image for switches are changes to green/red squares and moved between nodes.
	- Bug fixes in DSS configuration.
	- GridLAB-D updated to latest develop version.
	- OpenDSSCmd updated to 1.2.3.
	- Powergrid models - Updated Generator.dss to include kVA for generators. 
	- Added kva base to glm file, so setting kw=0 does not make the kva base also 0.
	- Internal house loads added. Schedule file is created for simulation when useHouses=true. 
	- Sensor service bugs fixed.
	- API added to export Vnom opendss file. 
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.10.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.10.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.10.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.10.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.7
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.6
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.10.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.10.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.10.0

Version 2019.12.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Updated and documented MRID UUID generator to ensure compliance with UUID 4
	- Integrate DNP3 service with GridAPPS-D container
	- Created API to get user role based on login
	- Added a user for testmanager to distinguish between simulation commands and alarms
	- Removed hardcoded corrdinate identifcation from Viz
	- Added capability to change model state before starting a simulation.
	- Added feature on UI to upload a file with faults and comunication output
	- Created user login page on UI 
	- Added light/dark toggle themeon UI 
	- Wrote a SWING_PQ node for each potential island in power grid model.
	- Fixed issues for app eveluations as reported by app developers or evluation team
	- Updated ci/cd scripts for repositories to support travis.ci updates
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2019.12.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2019.12.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2019.12.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2019.12.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.7
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.6
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2019.12.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2019.12.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2019.12.0
	
Version 2020.01.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Alarms are varified before publishing.
	- Fixed floating switches issue on Viz app. 
	- Release process documeted at gridappsd-docker-build repository readme
	- Created an automated, repeatable way to upload data in blazegraph
	- Documented model state update for starting a simulation 
		
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2020.01.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2020.01.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2020.01.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2020.01.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.7
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.6
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2020.01.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2020.01.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2020.01.0
	
Version 2020.02.0
^^^^^^^^^^^^^^^^^

1. New Features
		
	- Alarms status is published as Open/Close instead of 0/1.
	- Added resume/pause-at API for simulation.
	- Added the EnergyConsumer.p attribute as a writable property in the FNCS GOSS Bridge
	- Fixed floating switches issue on Viz app. 
	- Added units on the plots.
	- Viz allow user to go to nodes by clicking on plots.
	- Labels added for overlapping line on Viz plots.
	- Operator login issue resolved.
	- First integration test added in gridappsd-testing repo.
	
2. Source Code

	- goss-gridapps-d - https://github.com/GRIDAPPSD/GOSS-GridAPPS-D/tree/releases/2020.02.0
	- gridappsd-viz - https://github.com/GRIDAPPSD/gridappsd-viz/tree/releases/2020.02.0
	- gridappsd-python - https://github.com/GRIDAPPSD/gridappsd-python/tree/releases/2020.02.0
	- cim2glm - https://github.com/GRIDAPPSD/Powergrid-Models/tree/releases/2020.02.0
	- proven-cluster - https://github.com/pnnl/proven-cluster/releases/tag/v1.3.5.7
	- proven-client - https://github.com/pnnl/proven-client/releases/tag/v1.3.6
	- proven-message - https://github.com/pnnl/proven-message/releases/tag/v1.3.5.4
	- proven-docker - https://github.com/GRIDAPPSD/proven-docker/tree/releases/2020.02.0
	- fncs - https://github.com/GRIDAPPSD/fncs/tree/develop
	- gridappsd-docker-build - https://github.com/GRIDAPPSD/gridappsd-docker-build/tree/releases/2020.02.0
	- gridlab-d - https://github.com/GRIDAPPSD/gridlab-d/tree/develop
	- sample-app - https://github.com/GRIDAPPSD/gridappsd-sample-app/tree/releases/2020.02.0


