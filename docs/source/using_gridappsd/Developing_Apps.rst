Supported Application or Service Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Python
- EXE

Hosting Application
^^^^^^^^^^^^^^^^^^^

Developers can create application using GridAPPS-D API and use following instruction to host it with the platform.
Applications run in their own Docker contianer. 
For example of an application working with GridAPPS-D, please see: https://github.com/GRIDAPPSD/gridappsd-sample-app.

**1. Create proper folder structure for the application**

Following is the recommended structure for applications working with GridAPPS-D using gridappsd-sample-app as an example:

::
		
	.
	└── gridappsd-sample_app
	    ├── sample-app
	    │   ├── [application exe or pythod code]
	    ├── requirements.txt
	    ├── sample_app.config
	    ├── Dockerfile
	    └── setup.py
		

Where,
		
 - **gridappsd-sample-app** is a folder and name of the application.
 - **sample-app** is a folder that contains the application's source/build code.
 - **requirements.txt** is required for Python based application and lists all the pre-requisite packages. 
 - **sample_app.config** is a file used by GridAPPS-D to launch the application from inside application container. More details are provided in Step 2. 
 - **Dockerfile** contains all the commands to assemble a Docker image for the application. More details are provided in Step 3. 
 - **setup.py** is build script file for python based applications. 
 
**2. Create config file for application**

Config file is used by GridAPPS-D platform to register and launch the application. 
Here is the config file example using gridappsd-sample-app:

::

	{
	    "id":"sample-app",
	    "description":"GridAPPS-D Sample Application app",
	    "creator":"PNNL",
	    "inputs":[],
	    "outputs":[],
	    "options": ["(simulationId)"],
	    "type":"PYTHON",
	    "execution_path": "sample_app/runsample.py",
	    "launch_on_startup":false,
	    "prereqs":["gridappsd-state-estimator"],
	    "multiple_instances":false
	}

Where,

 - **id** is the name of the application and should match the name of the config file. 
 - **description** is a string that describes the application.
 - **creator** is the organization/developer name
 - **inputs** is the list of input topics application is listening to. *For future use. Leave it as in the example for now*.
 - **outputs** is the list of input topics application is publishing to. *For future use. Leave it as in the example for now*.
 - **options** are the run time arguments required by the application. Available options are: (i) simulationId: Unique identifier for the simulation, (ii) request: Simulation request sent by the user.
 - **type** defines the type fo the application which can be PYTHON or EXE.
 - **execution_path** is the path of the main file that starts the application relative to the top-most folder. In this example it would be the path relative to gridappsd-sample-app folder.
 - **launch_on_startup** is true if application needs to be started as the platform starts and false if application needs to be started with a simulation. 
 - **prereqs** is list of GridAPPS-D services that need to be started before starting the application. Leave it as empty list [] if no such services are required. 
   Services such as FNCS and FNCS-GOSS-BRIDGE are started by default with a simuolation so not needed to be specified here. 
 - **multiple_instances** is true if multiple instances of this application can be started for a single simulation otherwise false.
 

**3. Create Dockerfile for application**

Copy Dockerfile from https://github.com/GRIDAPPSD/gridappsd-sample-app/blob/master/Dockerfile. 
In the file replace gridappsd-sample with your applcation name and sample_app.config with the name of the config file of your application. 
You can add more commands in the file if needed for your application. 

**4. Build the Docker container for application**

::

    docker build --network=host -t sample-app .
	
Where,

 - **sample-app** is the image name. Change it to your application name.
	
**5. Clone gridappsd-docker repository**

Clone this repository outside any application folder.

::

    git clone https://github.com/GRIDAPPSD/gridappsd-docker.git
	
**6. Add application to platform**

In order to add your application to the GridAPPS-D platform you will need to modify the docker-compose.yml file included in the gridappsd-docker repository.
Add the following to the file:

:: 
		
    sample_app:
    image: sample_app
    environment:
      GRIDAPPSD_URI: tcp://gridappsd:61613
    depends_on:
      - gridappsd  

Use image name from step 4 instead of sample_app in line 1 and 2.
		
**7. Start platform and application container**

::
  
  cd gridappsd-docker
  ./run.sh 
  
This script starts application container along with platform. 
Application container has built-in code that allows application to register with GridAPPS-D platform when it starts.
  
**8. Verify that application container is running**

Use following command to list all Docker container which should include application container with *running* status.

::
 
  docker ps -a 

Optional - You can go inside the application container to check its content.

:: 

    docker exec -it sample_app bash
	

Where, 

 - **sample_app** is the name of the container. Replace it with your application container name.
 
Execute *exit* to get out of the application container.

  
**9. Varify that application is hosted correctly**

 - Go to http://localhost:8080
 - Login with default user credetials already provided in login screen.
 - Press Menu on the top-left corner
 - Press *Configure New Simulation* menu item
 - Go to *Application Configuration* tab
 - Look for the application name in the drop down box.
 

If your application is available in that drop down box then application is hosted correctly with the platform. 

For next step see documentation under *Using GridAPPS-D* --> *Start a Simulation*


Hosting Service
^^^^^^^^^^^^^^^

Developers can create a platform service using GridAPPS-D API and use following instruction to host it with the platform.
For example of an service working with GridAPPS-D, please see: https://github.com/GRIDAPPSD/gridappsd-state-estimator.		

**1. Create proper folder structure for the service.**

Following is the recommended structure for services working with gridappsd using gridappsd-state-estimator as an example:

::
		
	.
	└── gridappsd-state-estimator
	    ├── state-estimator
	    │   ├── [service exe or pythod code]
	    ├── requirements.txt
	    ├── state-estimator.config
	    └── setup.py
	    
 - **gridappsd-state-estimator** is a folder and name of the service.
 - **state-estimator** is a folder that contains the service's source/build code.
 - **requirements.txt** is required for Python based service and lists all the pre-requisite packages. 
 - **state-estimator.config** is a file used by GridAPPS-D to launch the service from inside GridAPPS-D container. More details are provided in Step 2. 
 - **setup.py** is build script file for python based applications. 

**2. Create config file for service**

Config file is used by GridAPPS-D platform to register and launch the service. 
Here is the config file example using gridappsd-state-estimator:

::
 
	{
		"id":"state-estimator",
		"description":"State Estimator",
		"creator":"PNNL",
		"inputs":["/topic/goss.gridappsd.fncs.output","/topic/goss.gridappsd.se.input"],
		"outputs":["/topic/goss.gridappsd.se.requests","/topic/goss.gridappsd.se.system_state"],
		"static_args":["(simulationId)","(request)"],
		"execution_path":"services/gridappsd-state-estimator/state-estimator/bin/state-estimator",
		"type":"EXE",
		"launch_on_startup":false,
		"prereqs":[],
		"multiple_instances":true,
		"environmentVariables":[],
		"user_input": {
			"use-sensors-for-estimates": {
				"help": "Use measurements from the sensor-simulator service, if the sensor-simulator is configured, to generate state estimates rather than using simulation measurements",
				"help_example": false,
				"default_value": true,
				"type": "bool"
			}
		}
	}

Where,

 - **id** is the name of the service and should match the name of the config file. 
 - **description** is a string that describes the service.
 - **creator** is the organization/developer name
 - **inputs** is the list of input topics service is listening to. *For future use. Leave it as in the example for now*.
 - **outputs** is the list of input topics service is publishing to. *For future use. Leave it as in the example for now*.
 - **options** are the run time arguments required by the service. Available options are: (i) simulationId: Unique identifier for the simulation, (ii) request: Simulation request sent by the user.
 - **type** defines the type fo the service which can be PYTHON or EXE.
 - **execution_path is the path of the main file that starts the service relative to the top-most folder. In this example it would be the path relative to gridappsd-sample-app folder.**
 - **launch_on_startup** is true if service needs to be started as the platform starts and false if service needs to be started with a simulation. 
 - **prereqs** is list of GridAPPS-D services that need to be started before starting the service. Leave it as empty list [] if no such services are required. 
   Services such as FNCS and FNCS-GOSS-BRIDGE are started by default with a simuolation so not needed to be specified here. 
 - **multiple_instances** is true if multiple instances of this service can be started for a single simulation otherwise false.



Example config for service:

::

	{
		"id":"state-estimator",
		"description":"State Estimator",
		"creator":"PNNL",
		"inputs":["/topic/goss.gridappsd.fncs.output","/topic/goss.gridappsd.se.input"],
		"outputs":["/topic/goss.gridappsd.se.requests","/topic/goss.gridappsd.se.system_state"],
		"static_args":["(simulationId)"],
		"execution_path":"service/bin/state-estimator.out",
		"type":"EXE",
		"launch_on_startup":false,
	        "prereqs":[],
		"multiple_instances":true,
		"environmentVariables":[]
	}


2. Clone the repository https://github.com/GRIDAPPSD/gridappsd-docker (refered to as gridappsd-docker repository) next to this repository (they should both have the same parent folder)

::
	
	.
	├── gridappsd-docker
	└── gridappsd-sample-app
	

3. Add service or service to platform

In order to add your service/service to the container you will need to modify the docker-compose.yml file included in the gridappsd-docker repository. 
Under the gridappsd service there is an example volumes leaf that is commented out. Uncomment and modify these lines to add the path for your service and config file. 
Adding these lines will mount the service/service on the container's filesystem when the container is started.

For service:

::
	
	#    volumes:
	#      - ~/git/gridappsd-sample-app/sample_app:/gridappsd/services/sample_app
	#      - ~/git/gridappsd-sample-app/sample_app/sample_app.config:/gridappsd/services/sample_app.config
	
	    volumes:
	      - ~/git/[my_app_directory]/[my_app]:/gridappsd/services/[my_app]
	      - ~/git/[my_app_directory]/[my_app]/[my_app.config]:/gridappsd/services/[my_app.config]

For service:

::
	
	#    volumes:
	#      - ~/git/gridappsd-sample-app/sample_app:/gridappsd/services/sample_app
	#      - ~/git/gridappsd-sample-app/sample_app/sample_app.config:/gridappsd/services/sample_app.config
	
	    volumes:
	      - ~/git/[my_service_directory]/[my_service]:/gridappsd/services/[my_service]
	      - ~/git/[my_service_directory]/[my_service]/[my_service.config]:/gridappsd/services/[my_service.config]			  
		  
How to start a service
^^^^^^^^^^^^^^^^^^^^^^
*Note: This process will be simplified in future releases so user could start a service through API and UI for a simulation with or without an service.*

Currently a service will be started by the platform only if it is a requirement for an service as described in the service config file under prereqs key.
By default gridappsd-sensor-service and gridappsd-voltage-violation  services are available in GridAPPS-D docker container. 

In order to start a service with an service (sample app in this example) follow these steps:

1. Go into sample app container by executing
::
	
	docker exec -it gridappsddocker_sample_app_1 bash

2. Inside sample app container execute following commands 
::
	
	apt-get update

	apt-get install vim

4. Edit sample_app.config and add service id to the prereqs as shown below:
::
	
	"prereqs":["gridappsd-sensor-simulator"]

*Note: Service id should match the value of "id" in service config file.* 

5. Exit sample app container

6. Restart sample app docker container by executing
::
	
	docker restart gridappsddocker_sample_app_1

7. Go into GridAPPS-D docker container by executing
::
	
	docker exec -it gridappsddocker_gridappsd_1 bash

8. Start platform by executing
:

	./run-gridappsd.sh
	
Now when you start a simulation with sample app the service defined in prereqs will start as well. 



