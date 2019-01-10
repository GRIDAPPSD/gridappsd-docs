
Request all GridLAB-D configuration files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates all configuration files necessary to run a sumulation using the GridLAB-D simulator.  Returns the diretory where all of the configuration files are stored.

- Required: configurationType, parameters[model_id,directory,simulationname,simulation_start_time,simulation_duration,simulation_id,simulation_broker_host,simulation_broker_port]
- Optional: parameters[i_fraction, p_fraction, z_fraction, load_scaling_factor, schedule_name,solver_method]

Request: goss.gridappsd.process.request.config
::

  {
    "configurationType": "GridLAB-D All",
    "parameters": {
      "load_scaling_factor": "1.0",
      "i_fraction": "1.0",
      "model_id": "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3",
      "p_fraction": "0.0",
      "simulation_id": "12345",
      "z_fraction": "0.0",
      "simulation_broker_host": "localhost",
      "simulation_name": "ieee8500",
      "simulation_duration": "60",
      "simulation_start_time": "2018-02-18 00:00:00",
      "solver_method": "NR",
      "schedule_name": "ieeezipload",
      "simulation_broker_port": "61616",
      "directory": "/tmp/gridlabdsimulation/"
    }
  }

Response:
<directory where files have been stored>
  
  
Request GridLAB-D Base File
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates the main GLM file required by the GridLAB-D simulator

- Required: configurationType, parameters[model_id]
- Optional: parameters[simulation_id, i_fraction, p_fraction, z_fraction, load_scaling_factor, schedule_name]

Request:  goss.gridappsd.process.request.config
::

  {
    "configurationType": "GridLAB-D Base GLM",
    "parameters": {
      "i_fraction": "1.0",
      "z_fraction": "0.0",
      "model_id": "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3",
      "load_scaling_factor": "1.0",
      "schedule_name": "ieeezipload",
      "p_fraction": "0.0"
    }
  }
  
Response:
::

  object regulator_configuration {
    name "rcon_VREG4";
    connect_type WYE_WYE;
    Control MANUAL; // OUTPUT_VOLTAGE;
  .......

Request GridLAB-D Symbols File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates the symbols file with XY coordinates used by the GridLAB-D simulator

- Required: configurationType, parameters[model_id]
- Optional: parameters[simulation_id]

Request:  goss.gridappsd.process.request.config
::

  {
    "configurationType": "GridLAB-D Symbols",
    "parameters": {
      "model_id": "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"
    }
  }
  
Response:
::

  {"feeder":[
  {"swing_nodes":[
  {"name":"source","bus":"sourcebus","phases":"ABC",
    "nominal_voltage":66395.3,"x1":1693780.0,"y1":1.22775777570982E7}
  ]},
  {"capacitors":[
  .......


Request CIM Dictionary file
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates a dictionary file which maps between the mrid identifiers used by the CIM model and the other names of model objects used by simulators.

- Required: configurationType, parameters[model_id]
- Optional: parameters[simulation_id]

Request: goss.gridappsd.process.request.config
::

  {
    "configurationType":"CIM Dictionary",
    "parameters":{"model_id":"_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"}
   }

Response:
::

  {"feeders":[
  {"name":"ieee8500",
  "mRID":"_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3",
  "substation":"ieee8500_Substation",
  "substationID":"_F1E8E479-5FA0-4BFF-8173-B375D25B0AA2",
  "subregion":"large",
  "subregionID":"_A1170111-942A-6ABD-D325-C64886DC4D7D",
  "region":"ieee",
  "regionID":"_6F10E278-12DC-9CBB-D2D9-D09582538F8A",
  "capacitors":[
  {"name":"capbank0a","mRID":"_A5866105-A527-F682-C982-69807C0E088B","CN1":"r42246","phases":"A","kvar_A":400.0,"kvar_B":0.0,"kvar_C":0.0,"nominalVoltage":12470.0,"nomU":7200.0,"phaseConnection":"Y","grounded":true,"enabled":true,"mode":"reactivePower","targetValue":-50000.0,"targetDeadband":-500000.0,"aVRDelay":100.0,"monitoredName":"cap_3a","monitoredClass":"ACLineSegment","monitoredBus":"q16642","monitoredPhase":"A"},
  .......
  ],
  "regulators":[
  {"bankName":"FEEDER_REG","size":"3","bankPhases":"ABC","tankName":["feeder_rega","feeder_regb","feeder_regc"],"endNumber":[2,2,2],"endPhase":["A","B","C"],"rtcName":["feeder_rega","feeder_regb","feeder_regc"],"mRID":["_330E7EDE-2C70-8F72-B183-AA4BA3C5E221","_0EBF840D-7BE9-0D81-03A0-315D617ECA27","_BBB3984D-2A67-7E15-0763-635C5B06A348"],"monitoredPhase":["A","B","C"],"TapChanger.tculControlMode":["volt","volt","volt"],"highStep":[32,32,32],"lowStep":[0,0,0],"neutralStep":[16,16,16],"normalStep":[16,16,16],"TapChanger.controlEnabled":[true,true,true],"lineDropCompensation":[false,false,false],"ltcFlag":[true,true,true],"RegulatingControl.enabled":[true,true,true],"RegulatingControl.discrete":[true,true,true],"RegulatingControl.mode":["voltage","voltage","voltage"],"step":[1.0125,1.0125,1.0063],"targetValue":[126.5000,126.5000,126.5000],"targetDeadband":[2.0000,2.0000,2.0000],"limitVoltage":[0.0000,0.0000,0.0000],"stepVoltageIncrement":[0.6250,0.6250,0.6250],"neutralU":[7200.0000,7200.0000,7200.0000],"initialDelay":[15.0000,15.0000,15.0000],"subsequentDelay":[2.0000,2.0000,2.0000],"lineDropR":[0.0000,0.0000,0.0000],"lineDropX":[0.0000,0.0000,0.0000],"reverseLineDropR":[0.0000,0.0000,0.0000],"reverseLineDropX":[0.0000,0.0000,0.0000],"ctRating":[300.0000,300.0000,300.0000],"ctRatio":[1500.0000,1500.0000,1500.0000],"ptRatio":[60.0000,60.0000,60.0000]},
  .......
  ],
  "solarpanels":[
  ],
  "batteries":[
  ],
  "switches":[
  {"name":"2002200004641085_sw","mRID":"_F5E6D212-C700-C94A-ED54-E00E8230C19C","CN1":"q14734","CN2":"d5587291-3_int","phases":"ABC","nominalVoltage":12470.0,"normalOpen":false},
  .......
  ],
  "measurements":[  
    {"name":"RatioTapChanger_VREG2","mRID":"02b818b7-fab3-4529-b3b3-fa7cb026eab9","ConductingEquipment_mRID":"_39BD981D-C57D-49E9-1209-9DF79B93A9EA","Terminal_mRID":"_4082AE8B-FAF3-34A9-26A6-6769C16CF78D","measurementType":"Pos","phases":"A","MeasurementClass":"Discrete","ConductingEquipment_type":"PowerTransformer","ConductingEquipment_name":"VREG2","ConnectivityNode":"190-8593"},
  {"name":"PowerTransformer_hvmv_sub_Power","mRID":"034241b0-c4f9-4f83-9b65-5dcbeab6b029","ConductingEquipment_mRID":"_B32F64E3-AAD3-FA3F-254B-CF74D12DA290","Terminal_mRID":"_ECDEEB50-1B94-9B13-A797-DED1326D80A5","measurementType":"VA","phases":"B","MeasurementClass":"Analog","ConductingEquipment_type":"PowerTransformer","ConductingEquipment_name":"hvmv_sub","ConnectivityNode":"hvmv_sub_hsb"},

  .......
  ]
  }]}

Request CIM Feeder Index file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates a list of the feeders available powergrid model data store

- Required: configurationType, parameters[model_id]
- Optional: parameters[simulation_id]

Request: goss.gridappsd.process.request.config
::

  {
    "configurationType":"CIM Feeder Index",
    "parameters":{"model_id":"_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"}
   }

Response:
::

  {"feeders":[
  {"name":"ieee123","mRID":"_C1C3E687-6FFD-C753-582B-632A27E28507","substationName":"ieee123_Substation","substationID":"_FE44B314-385E-C2BF-3983-3A10C6060022","subregionName":"large","subregionID":"_1CD7D2EE-3C91-3248-5662-A43EFEFAC224","regionName":"ieee","regionID":"_24809814-4EC6-29D2-B509-7F8BFB646437"},
  {"name":"ieee13nodecktassets","mRID":"_5B816B93-7A5F-B64C-8460-47C17D6E4B0F","substationName":"ieee13nodecktassets_Substation","substationID":"_D5B23536-54A7-984E-78F2-B136E9B6380E","subregionName":"test","subregionID":"_C43D4535-5786-01CD-C3C4-69AAC7945AD2","regionName":"ieee","regionID":"_85D8A951-64F2-4787-C922-4AE0AA99A874"},
  .......
  ]}

Request Simulation Output Configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates file containing objects and properties with measurements avilable in the selected model

- Required: configurationType, parameters[model_id]
- Optional: parameters[simulation_id]

Request: goss.gridappsd.process.request.config
::

  {
    "configurationType":"CIM Feeder Index",
    "parameters":{"model_id":"_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"}
   }

Response:
::

  {
    "cap_capbank0a": [
      "switchA",
      "shunt_A",
      "voltage_A"
    ],

    "cap_capbank1b": [
      "switchB",
      "voltage_B",
      "shunt_B"
    ],
    "cap_capbank2c": [
      "voltage_C",
      "switchC",
      "shunt_C"
    ],
    "cap_capbank0b": [
      "voltage_B",
      "switchB",
      "shunt_B"
    ],.......


Request YBus Export Configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Generates file containing ybus configuration for the selected simulation.  Simulation must be running.

- Required: configurationType, parameters[simulation_id]

Request: goss.gridappsd.process.request.config
::

  {
    "configurationType":"YBus Export",
    "parameters":{"simulation_id":"12345"}
    }

Response:
::

  {
    yParseFilePath":"/tmp/gridappsd_tmp/1129698954/base_ysparse.csv",
    "nodeListFilePath":"/tmp/gridappsd_tmp/1129698954/base_nodelist.csv",
    "summaryFilePath":"/tmp/gridappsd_tmp/1129698954/base_summary.csv"
  }


