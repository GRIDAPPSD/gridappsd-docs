The Timeseries Data API allows you to query the timeseries data such as weather, simulation output and input. 

Query Request Queue
^^^^^^^^^^^^^^^^^^^
Query request should be sent on following queue: goss.gridappsd.process.request.data.timeseries

Query Weather data
^^^^^^^^^^^^^^^^^^

By default GridAPPS-D comes with weather data for the year 2013. 

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

Returns simulation input or output data based on query filters/

Example Request:
::

	{"queryMeasurement": "PROVEN_MEASUREMENT",
 	 "queryFilter": {"hasSimulationId": "751004304"},
  	"responseFormat": "JSON"}


Example Response for result format JSON:
::

	{ "data": { "measurements": [ { "name": "PROVEN_MEASUREMENT", 
	"points": [ { "row": { "entry": [ 
				{ "key": "hasAngle", "value": "118.82725524902344" },
				{ "key": "hasProvenMessage", "value": "http://proven.pnnl.gov/proven-message#2d8ce725-dc82-4ea7-a739-d6fe11d810e4" },
				{ "key": "hasSimulationMessageType", "value": "OUTPUT" },
				{ "key": "time", "value": "1541708366" },
				{ "key": "hasMagnitude", "value": "2333.984130859375" },
				{ "key": "hasMeasurement", "value": "http://proven.pnnl.gov/proven-message#fb18f671-5b2b-4a07-a21b-c39c2cc5a21b" },
				{ "key": "hasMrid", "value": "_a8132cc6-52f7-4bae-be9e-8f28d9effcd3" },
				{ "key": "hasSimulationId", "value": "290653535" } ] } },
		{ "row": { "entry": [ 
				{ "key": "hasAngle", "value": "25.29271125793457" }, 
				{ "key": "hasProvenMessage", "value": "http://proven.pnnl.gov/proven-message#2d8ce725-dc82-4ea7-a739-d6fe11d810e4" }, 
				{ "key": "hasSimulationMessageType", "value": "OUTPUT" }, 
				{ "key": "time", "value": "1541708366" }, 
				{ "key": "hasMagnitude", "value": "44411.1796875" }, 
				{ "key": "hasMeasurement", "value": "http://proven.pnnl.gov/proven-message#fb41d8c5-7581-4282-aa29-c2b043d61b42" }, 
				{ "key": "hasMrid", "value": "_c3728546-d175-489a-934f-54d662454e24" },
				{ "key": "hasSimulationId", "value": "290653535" } ] } },
	"responseComplete":true,
	"id":"131754834"
	}
	
Allowed values for qwueryFilter are:
::

	Both input and output message type:
	startTime [number] 
	endTime [number]
	hasMrid [string]
	hasSimulationId [string]
	hasSimulationMessageType ["OUTPUT" | "INPUT"]
	
	Ouput message type:
	hasAngle [number]
	hasMagnitude [number]
	
	Input Message type:
	hasMeasurementDifference  ["FORWARD"  | "REVERSE"]
	hasDifferenceAttribute [string]
	hasObject [string]
	hasValue [number]
