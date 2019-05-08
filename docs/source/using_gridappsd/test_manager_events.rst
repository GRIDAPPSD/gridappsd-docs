Test Manager Events
~~~~~~~~~~~~~~~~~~~

There are 3 types events supported by the TestManager and the platform along with a command to add them:
    1. CIM defined fault events, used when a line is down or for taking a piece of equipment out of service.  
    2. Communication outage events which simulates measurements or control message outages.
    3. Command at specific time which sends commands to a piece of equipment to simulate reclosers.

There are 2 commands to the TestManager:
    1. Update
    2. QueryStatus
    

|event_classes_image0|

Fault Events
^^^^^^^^^^^^

Fault Events are defined in a Test Script and define the CIM Fault events that will be intialized and cleared at scheduled times.

The phases can be more the just "A". For example it could be AN" A to ground and "AB" would be line to line.
There can be secondary codes:
"S12N" both hot wires to ground
"S12" both hot wires together.
 
PhaseConnectedFaultKind is an enumeration:

1.	lineToGround
2.	lineToLine
3.	lineToLineToGround
4.	lineOpen

.. code-block:: none
    :caption: Fault Events in Test Script JSON schema
    :emphasize-lines: 3,5

    {
        "faultMRID" : string,
        "equipmentMRID" : string, 
        "phases": string, 
        "PhaseConnectedFaultKind" : string,
        "rGround":double,
        "xGround": double,
        "rLineToLine": double,
        "xLineToLine": double,
        "timeInitiated":long,
        "timeCleared":long
    }
..


.. code-block:: JSON
   :caption: Fault Event Example in test script

    {
        "events" : [
            {"faultMRID" : "1233",
            "equipmentMRID" : "12344",
            "phases": "AN",
            "PhaseConnectedFaultKind" : "lineToGround",
            "rGround":0.001,
            "xGround":0.001,
            "rLineToLine":0.0,
            "xLineToLine":0.0,
            "timeInitiated":1248156005,
            "timeCleared":1248156008
            },
            {"faultMRID" : "1234",
            "equipmentMRID" : "12345",
            "phases": "AB",
            "PhaseConnectedFaultKind" : "lineToLine",
            "rGround":0.0,
            "xGround":0.0,
            "rLineToLine":0.001,
            "xLineToLine":0.001,
            "timeInitiated":1248156017,
            "timeCleared":1248156020
            }
        ]
    }
..


Fault Commands sent from the Test Manager to the simulation

.. code-block:: JSON
   :caption: Initialize a Fault Command example

    {
        "command": "update", 
        "input": {
            "timestamp": 1553201000414, 
            "reverse_differences": [], 
            "difference_mrid": "_ee4e4055-222f-4ccf-bed1-93063bd4392c", 
            "forward_differences": [
            {
                "ObjectMRID": "12344", 
                "FaultImpedance": {
                "xLineToLine": 0.0, 
                "rGround": 0.001, 
                "rLineToLine": 0.0, 
                "xGround": 0.001
                }, 
                "FaultMRID": "1233", 
                "PhaseCode": "AN", 
                "PhaseConnectedFaultKind": "lineToGround"
            }
            ]
        }
    }
..

.. code-block:: JSON
   :caption: Clear a Fault Command example

    {
        "command": "update", 
        "input": {
            "timestamp": 1553201003561, 
            "reverse_differences": [
            {
                "ObjectMRID": "12344", 
                "FaultImpedance": {
                "xLineToLine": 0.0, 
                "rGround": 0.001, 
                "rLineToLine": 0.0, 
                "xGround": 0.001
                }, 
                "FaultMRID": "1233", 
                "PhaseCode": "AN", 
                "PhaseConnectedFaultKind": "lineToGround"
            }
            ], 
            "difference_mrid": "_00b4668d-8454-4f1c-aed9-42d1424af149", 
            "forward_differences": []
        }
    }
..

Communication Event
^^^^^^^^^^^^^^^^^^^

Communication Events are separate from the CIM events but we tried to keep pattern of the CIM events and as much commonality as possible. 

For reference this is the complete JSON schema of the internal Communication Event for the platform and goes between the Test Manager and the fncs_goss_bridge.py.

.. code-block::  none
   :caption: JSON Communication Event command for the TestManager

    {  
        "command":"CommEvent",
        "simulation_id":int,
        "message":{
            "inputList":[ {"ObjectMRID":String,
                        "attribute":String },...
                    ],
            "outputList":[MeasurementMRID,...],
            "filterAllInputs":boolean,
            "filterAllOutputs":boolean,
            "timeInitiated":long,
            "timeCleared":long
        }
    }
..

The inputList is the list of objects that are the ObjectMRID of anything that can be controllable and specific control attribute i.e. "RegulatingControl.mode". 

The outputList is the list of measurements mrids for the simulations. 

If filterAllInputs is True the inputList is not needed.
If filterAllOutputs is True the outputList is not needed.

.. code-block::  none
   :caption: Communication Event to the Simulation Bridge

    {
        "command":"CommEvent",
        "input":{
            "simulation_id":int,
            "message":{
                "timestamp":long,
                "difference_mrid":String,
                "reverse_differences":[],
                "forward_differences":[{
                    "object":String,
                    "attribute":"FilterObject",
                    "value":{
                    "inputList":[ {"ObjectMRID":String,
                                    "attribute":String },...
                                ],
                    "outputList":[MeasurementMRID,...],
                    "filterAllInputs":boolean,
                "filterAllOutputs":boolean,
                    "timeInitiated":long,
                    "timeCleared":long
                    }
                },...],
            }
        }
    }
..

The object will be the EventID generated by TestManager

Updating Events
^^^^^^^^^^^^^^^

Events time initialized and time cleared can be updated to happen at a differant times or to happen immediately.
A value of -1 will cause the event to be scheduled immediately.

.. code-block::  none
    :caption: JSON update command to Test Manager
    :emphasize-lines: 6

    {  
        "command": "update",
        "simulation_id",int,
        “message”:{
            "object":String, "FaultMRID"
            "attribute":"timeInitiated",
            "value": 1357048740, or -1 for now
        }
    }
..

Query
^^^^^
The Test Manager can be queried the for list of faults and statuses.
The status can be "scheduled", "inprogress", and "cleared".

.. code-block:: none
    :caption: Query the for list of faults and status

    {"queryMeasurement":"faults", “simulation_id”:int}
..

.. code-block:: none
    :caption: Result JSON Schema
    :emphasize-lines: 10

    { 
        "data": [
            {“faultMRID" : String,
            "simulation_id": int,
            “faultType:”: String,
            "fault": <Fault Object>,    
            "timeInitiated":long,
            "timeCleared":long,
            "status": "scheduled"},  # "scheduled", "inprogress", "cleared"
        }
    }
..


.. code-block:: JSON
    :caption: Result CIM Fault Events example

    { 
        "data":  [       
            {"faultMRID" : "1233",
            "simulation_id": 12399999,
            “faultType:”: "CommEvent",
            "fault":{
                "equipmentMRID" : "12344",
                "phases": "AN",
                "PhaseConnectedFaultKind" : "lineToGround",
                "rGround":0.001,
                "xGround":0.001,
                "rLineToLine":0.0,
                "xLineToLine":0.0,
            }
            "timeInitiated":1248156005,
            "timeCleared":1248156008,
            "status": "scheduled"}, 
        ]
    }
..

Scheduled Commands
^^^^^^^^^^^^^^^^^^

WIP. Commands can be scheduled a point in time in the simulation.

.. code-block:: none
    :caption: JSON scheduled command schema

    {
        "command": "update",
        "input":{
            "simulation_id":int,
                "message":{
                "timestamp":long,
                "difference_mrid":String,
                "reverse_differences":[<Object>],
                "forward_differences":[<Object>]
            }
        },
        "timeInitiated":long,
        "timeCleared":long,
    }
..


.. code-block:: JSON
    :caption: Scheduled command example

    { 
        "commandToBeScheduled":
        {
            "simulation_id" : 12399999,
            "message" : {
                "timestamp" : "2018-01-08T13:27:00.000Z",
                "difference_mrid" : "123a456b-789c-012d-345e-678f901a235c",
                "reverse_differences" : [
                        {
                                "object" : "61A547FB-9F68-5635-BB4C-F7F537FD824E",
                                "attribute" : "ShuntCompensator.sections",
                                "value" : "1"
                        }],
                "forward_differences" : [
                        {
                                "object" : "61A547FB-9F68-5635-BB4C-F7F537FD824E",
                                "attribute" : "ShuntCompensator.sections",
                                "value" : "0"
                        }]
            }
        },
        "timeInitiated":1248156005,
        "timeCleared":1248156008,
    }
..


.. |event_classes_image0| image:: EventClassDiagram.png
