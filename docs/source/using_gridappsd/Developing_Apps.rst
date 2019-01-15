Supported Application or Service Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Python
- EXE

Hosting Application or Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Developers can create application and services using GridAPPS-D API and use following instruction to host it with the platform.
For example of application and service working with GridAPPS-D, please see: https://github.com/GRIDAPPSD/gridappsd-sample-app and
https://github.com/GRIDAPPSD/gridappsd-state-estimator

1. Create proper folder structure for the application or service.

Following is the recommended structure for applications or services working with gridappsd using sample-app as an example:

For application:
::

	.
	├── README.md
	└── my_app
	    ├── app
	    │   ├── [application exe or python code]
	    ├── requirements.txt
	    ├── my_app.config
	    └── setup.py

For service:
::

	.
	├── README.md
	└── my_service
	    ├── service
	    │   ├── [service exe or pythod code]
	    ├── requirements.txt
	    ├── my_service.config
	    └── setup.py

Where config file is used by GridAPPS-D to launch the application or service from inside the gridappsd container.

Example config for application:

::

	{
	    "id":"sample_app",
	    "description":"GridAPPS-D Sample Application app",
	    "creator":"PNNL",
	    "inputs":[],
	    "outputs":[],
	    "options": ["(simulationId)"],
	    "type":"PYTHON",
	    "execution_path": "sample_app/runsample.py",
	    "launch_on_startup":false,
	    "prereqs":["fncs","fncsgossbridge"],
	    "multiple_instances":true
	}

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


3. Add application or service to platform

In order to add your application/service to the container you will need to modify the docker-compose.yml file included in the gridappsd-docker repository.
Under the gridappsd service there is an example volumes leaf that is commented out. Uncomment and modify these lines to add the path for your application and config file.
Adding these lines will mount the application/service on the container's filesystem when the container is started.

For application:

::

	#    volumes:
	#      - ~/git/gridappsd-sample-app/sample_app:/gridappsd/applications/sample_app
	#      - ~/git/gridappsd-sample-app/sample_app/sample_app.config:/gridappsd/applications/sample_app.config

	    volumes:
	      - ~/git/[my_app_directory]/[my_app]:/gridappsd/applications/[my_app]
	      - ~/git/[my_app_directory]/[my_app]/[my_app.config]:/gridappsd/applications/[my_app.config]

For service:

::

	#    volumes:
	#      - ~/git/gridappsd-sample-app/sample_app:/gridappsd/applications/sample_app
	#      - ~/git/gridappsd-sample-app/sample_app/sample_app.config:/gridappsd/applications/sample_app.config

	    volumes:
	      - ~/git/[my_service_directory]/[my_service]:/gridappsd/services/[my_service]
	      - ~/git/[my_service_directory]/[my_service]/[my_service.config]:/gridappsd/services/[my_service.config]
