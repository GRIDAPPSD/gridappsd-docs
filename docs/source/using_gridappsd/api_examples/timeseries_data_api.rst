The Timeseries Data API allows you to query the timeseries data such as weather, simulation output and input. 

Query Request Queue
^^^^^^^^^^^^^^^^^^^
Query request should be sent on following queue: goss.gridappsd.process.request.data.timeseries

Query Weather data
^^^^^^^^^^^^^^^^^^

.. include:: api_examples/weather.rst

Example Request:
::

	{"queryMeasurement":"weather", 
	"queryFilter":{"startTime":"1357048800000000",
				"endTime":"1357048860000000"},
	"responseFormat":"JSON"}

Example Response for result format JSON:
::

	{ "data": { "measurements": [ { "name": "weather",
	  "points": [ { "row": { "entry": [ 
		 			{ "key": "Diffuse","value": "-0.006386875" }, 
		 			{ "key": "AvgWindSpeed","value": "0.0" }, 
		 			{ "key": "TowerRH", "value": "86.8" },
		    		{ "key": "long", "value": "\"105.18 W\"" },
		    		{ "key": "MST","value": "00:00" },
		    		{ "key": "TowerDryBulbTemp","value": "13.316" },
		    		{ "key": "DATE", "value": "1/1/2013" },
		    		{ "key": "DirectCH1", "value": "-0.0402521765" },
		        	{ "key": "GlobalCM22", "value": "-0.037676152399999996" },
		         	{ "key": "AvgWindDirection", "value": "0.0" },
		          	{ "key": "time", "value": "1357048800" },
		           	{ "key": "place", "value": "\"Solar Radiation Research Laboratory\"" },
		            { "key": "lat", "value": "\"39.74 N\"" } ] } },
	           	  { "row": { "entry": [ 
	           	 	{ "key": "Diffuse","value": "-0.005538233499999999" },
	              	{ "key": "AvgWindSpeed", "value": "0.0" },
	               	{ "key": "TowerRH", "value": "86.9" },
	               	{ "key": "long", "value": "\"105.18 W\"" },
	                { "key": "MST", "value": "00:01" },
	                { "key": "TowerDryBulbTemp", "value": "13.406" },
	                { "key": "DATE", "value": "1/1/2013" },
	                { "key": "DirectCH1", "value": "-0.0395396335" },
	                { "key": "GlobalCM22", "value": "-0.0369521827" },
	                { "key": "AvgWindDirection", "value": "0.0" },
	                { "key": "time", "value": "1357048860" },
	                { "key": "place", "value": "\"Solar Radiation Research Laboratory\"" },
	                { "key": "lat", "value": "\"39.74 N\"" } ] } } ] } ] },
	  "responseComplete": true, "id": "1111869534" }

Allowed values for queryFilter are:
::

	startTime[epoch number]
	endTime[epoch number]
	AvgWindDirection[number]
	AvgWindSpeed[number]
	Diffuse[number]
	DirectCH1[number]
	GlobalCM22[number]
	MST[number]
	TowerDryBulbTemp[number]
	TowerRH[number]
	lat[string]
	long[string]
	place[string]

Query Simulation Data
^^^^^^^^^^^^^^^^^^^^^

Returns simulation input or output data based on query filters

Example Request:
::

	{"queryMeasurement": "simulation",
 	"queryFilter": {"simulation_id": "582881157"},
	"responseFormat": "JSON"}


Example Response for result format JSON:
::

	{
	"data": { "measurements": [{ "name": "simulation",
			"points": [{ "row": { "entry": [
				{ "key": "hasMeasurementDifference", "value": "FORWARD" },
				{ "key": "hasSimulationMessageType", "value": "INPUT" },
				{ "key": "difference_mrid", "value": "c65d4ba9-8689-4838-970c-2983b54ed2e6" },
				{ "key": "simulation_id", "value": "582881157" },
				{ "key": "time", "value": "1562614884" },
				{ "key": "attribute", "value": "ShuntCompensator.sections" },
				{ "key": "value", "value": "0.0" },
				{ "key": "object","value": "_5405BE1A-BC86-5452-CBF2-BD1BA8984093" }]}},
			{ "row": { "entry": [
				{ "key": "hasMeasurementDifference", "value": "FORWARD" },
				{ "key": "hasSimulationMessageType", "value": "INPUT" },
				{ "key": "difference_mrid", "value": "c65d4ba9-8689-4838-970c-2983b54ed2e6" },
				{ "key": "simulation_id", "value": "582881157" },
				{ "key": "time", "value": "1562614884" },
				{ "key": "attribute", "value": "ShuntCompensator.sections" },
				{ "key": "value", "value": "0.0" },
				{ "key": "object", "value": "_8D0EAC3F-AD56-C5A6-ED03-863DBB4A8C5F"}]}}
	"responseComplete": true,
	"id": "1927836780" }

	
Allowed values for queryFilter are:
::

	Both input and output message type:
	starttime [number] 
	endtime [number]
	measurement_mrid [string]
	simulation_id [string]
	hasSimulationMessageType ["OUTPUT" | "INPUT"]
	
	Ouput message type:
	angle [number]
	magnitude [number]
	
	Input Message type:
	hasMeasurementDifference  ["FORWARD"  | "REVERSE"]
	attribute [string]
	difference_mrid [string]
	object [string]
	value [number]

Please find some sample requests with various query filters
::
	{"queryMeasurement": "simulation",
 	"queryFilter": {"simulation_id": "582881157", "hasSimulationMessageType": "INPUT"},
	"responseFormat": "JSON"}

	{"queryMeasurement": "simulation",
 	"queryFilter": {"simulation_id": "582881157", "angle": 23.706919634782313},
	"responseFormat": "JSON"}
	
Query Sensor Service  Data
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns output of sensor sensor service.

Example Request:
::

	{"queryMeasurement": "gridappsd-sensor-simulator",
 	"queryFilter": {"simulation_id": "582881157"},
	"responseFormat": "JSON"}
	
Example Response for result format JSON:
::	
		{
			"data": {
			"measurements": [
				{
				"name": "gridappsd-sensor-simulator",
				"points": [
					{
						"row": {
						"entry": [
							{
								"key": "instance_id",
								"value": "gridappsd-sensor-simulator-1564186315783"
							},
							{
								"key": "hasSimulationMessageType",
								"value": "OUTPUT"
							},
							{
								"key": "measurement_mrid",
								"value": "_0009caa4-23ef-41b9-9db7-624f3f47460c"
							},
							{
								"key": "angle",
								"value": "-152.44531328865978"
							},
							{
								"key": "magnitude",
								"value": "2470.4939175057075"
							},
							{
								"key": "simulation_id",
								"value": "1512566584"
							},
							{
								"key": "time",
								"value": "1564186297"
							}
							]
							}
					},.........]}]
			},
			"responseComplete": true,
			"id": "597021681"
		}


Allowed values for queryFilter are:
::

	starttime [number] 
	endtime [number]
	measurement_mrid [string]
	simulation_id [string]
	instance_id
	angle [number]
	magnitude [number]
	value [number]
