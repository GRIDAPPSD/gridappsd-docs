There are 3 types events supported by the TestManager and the platform along with a command to add them:
    1. CIM defined fault events, used when a line is down or for taking a piece of equipment out of service.  
    2. Communication outage events which simulates measurements or control message outages.
    3. Command at specific time which sends commands to a piece of equipment to simulate reclosers. WIP

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

    {
        "PhaseConnectedFaultKind": string,
        "FaultImpedance": {
                        "rGround": float,
                        "xGround": float
        },
        "ObjectMRID": [string],
        "phases": string,
        "event_type": string,
        "occuredDateTime": long,
        "stopDateTime": long
    }
..


.. code-block:: JSON
   :caption: Fault Event Example in test script

    {   
        "command": "new_events",
        "events" : [{
                "PhaseConnectedFaultKind": "lineToGround",
                "FaultImpedance": {
                                "rGround": 0.001,
                                "xGround": 0.001
                },
                "ObjectMRID": ["_9EF94B67-7279-21F4-5CEE-B2724E3C3FE6"],
                "phases": "ABC",
                "event_type": "Fault",
                "occuredDateTime": 1248130809,
                "stopDateTime": 1248130816
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

Communication Outage events are separate from the CIM events but we tried to keep pattern of the CIM events and as much commonality as possible. 

For reference this is the complete JSON schema of the internal Communication Event for the platform and goes between the Test Manager and the fncs_goss_bridge.py.

.. code-block::  none
   :caption: JSON Communication Outage schema command for the TestManager

    {  
        "allOutputOutage": boolean,
        "allInputOutage": boolean,
        "inputOutageList": [{"objectMRID":string, "attribute":string}],
        "outputOutageList": [string],
        "event_type": string,
        "occuredDateTime": long,
        "stopDateTime": long
    }
..

.. code-block::  JSON
   :caption: JSON Communication Outage command for the TestManager

   {"command": "new_events",
    "events": [
        {
            "allOutputOutage": false,
            "allInputOutage": false,
            "inputOutageList": [{"objectMRID":"_EF2FF8C1-A6A6-4771-ADDD-A371AD929D5B", "attribute":"ShuntCompensator.sections"}, {"objectMRID":"_C0F73227-012B-B70B-0142-55C7C991A343", "attribute":"ShuntCompensator.sections"}],
            "outputOutageList": ["_5405BE1A-BC86-5452-CBF2-BD1BA8984093"],
            "event_type": "CommOutage",
            "occuredDateTime": 1248130819,
            "stopDateTime": 1248130824
        }
    ]
    }
..

The inputList is the list of objects that are the ObjectMRID of anything that can be controllable and specific control attribute i.e. "RegulatingControl.mode". 

The outputList is the list of measurements mrids for the simulations. 

If allInputOutage is True the inputList is not needed.
If allOutputOutage is True the outputList is not needed.

.. code-block:: JSON
   :caption: Communication Event to the Simulation Bridge

    {
    "command": "CommOutage",
    "input": {
        "timestamp": 1248130819,
        "forward_differences": [
        {
            "allOutputOutage": false,
            "allInputOutage": false,
            "inputOutageList": [
            {
                "objectMRID": "_EF2FF8C1-A6A6-4771-ADDD-A371AD929D5B",
                "attribute": "ShuntCompensator.sections"
            },
            {
                "objectMRID": "_C0F73227-012B-B70B-0142-55C7C991A343",
                "attribute": "ShuntCompensator.sections"
            }
            ],
            "outputOutageList": [
            "_5405BE1A-BC86-5452-CBF2-BD1BA8984093"
            ],
            "faultMRID": "_ce5ee4c9-9c41-4f5e-8c5c-f19990f9cfba",
            "event_type": "CommOutage",
            "occuredDateTime": 1248130819,
            "stopDateTime": 1248130824
        }
        ],
        "reverse_differences": []
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
        "command": "update_events",
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

    {"command":"query_events", "simulationID":int}
..

.. code-block:: none
    :caption: Result JSON Schema

    { 
        "data": [
            {
                <fault>,
                "status": <status>  # SCHEDULED, INITIATED, CLEARED, CANCELLED
            },...
        }
    }
..


.. code-block:: JSON
    :caption: Result CIM Fault Events example

    { 
        "data": [
            {
            "allOutputOutage": false,
            "allInputOutage": false,
            "inputOutageList": [
                {
                "objectMRID": "_EF2FF8C1-A6A6-4771-ADDD-A371AD929D5B",
                "attribute": "ShuntCompensator.sections"
                },
                {
                "objectMRID": "_C0F73227-012B-B70B-0142-55C7C991A343",
                "attribute": "ShuntCompensator.sections"
                }
            ],
            "outputOutageList": [
                "_5405BE1A-BC86-5452-CBF2-BD1BA8984093"
            ],
            "faultMRID": "_ce5ee4c9-9c41-4f5e-8c5c-f19990f9cfba",
            "event_type": "CommOutage",
            "occuredDateTime": 1248130819,
            "stopDateTime": 1248130824,
            "status": "CLEARED"
            }
        ]
    }
..

Scheduled Commands
^^^^^^^^^^^^^^^^^^

Commands can be scheduled a point in time in the simulation.

.. code-block:: none
    :caption: JSON scheduled command schema

    {   
        "command": "new_events",
        "events":[{
                "message":{
                    "forward_differences":[<Object>],
                    "reverse_differences":[<Object>]
                },
                "timeInitiated":long,
                "timeCleared":long,
        }]
    }
..


.. code-block:: JSON
    :caption: Scheduled command example

    {
        "command": "new_events",
        "events":[{
            "message": {
                "forward_differences": [
                    {
                    "object": "_8D0EAC3F-AD56-C5A6-ED03-863DBB4A8C5F",
                    "attribute": "ShuntCompensator.sections",
                    "value": "0"
                    }
                ],
                "reverse_differences": [
                    {
                    "object": "_8D0EAC3F-AD56-C5A6-ED03-863DBB4A8C5F",
                    "attribute": "ShuntCompensator.sections",
                    "value": "1"
                    }
                ]
            },
            "event_type": "ScheduledCommandEvent",
            "occuredDateTime": 1248130812,
            "stopDateTime": 1248130842
            }]
    }
..


.. |event_classes_image0| image:: EventClassDiagram.png
