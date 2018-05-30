
1. Test Configuration
The test configuration contains information to define the simulation run,
initial conditions and default values.

Example:

::

  {
      "power_system_configuration":"ieee8500",
      "simulation_configuration":"ieee8500",
      "duration":60,
      "run_start":"2017-07-21 12:00:00",
      "run_end":"2017-07-22 12:00:00",
      "region_name":"ieee8500_Region",
      "subregion_name":"ieee8500_SubRegion",
      "line_name":"ieee8500",
      "logging":"true",
      "logging_options":{ "log":"true"

      },
      "initial_conditions":{

      },
      "default_values":{

      }
  }

2. Test Script
The test script contains the name of the test script and the name of the
application, it needs to match the name of application on platform.
It also contains the test configuration path, the outputs to to listen for,
events, and the rules application script.

Example:

::

  {
   "name": "sample_app",
   "test_configuration": "./SampleTestConfig.json",
   "application": "sample_app",
   "outputs":
        {"substation_link": ["xf_hvmv_sub"],
         "regulator_list": ["reg_FEEDER_REG", "reg_VREG2", "reg_VREG3", "reg_VREG4"],
         "regulator_configuration_list": ["rcon_FEEDER_REG", "rcon_VREG2", "rcon_VREG3", "rcon_VREG4"],
         "capacitor_list": ["cap_capbank0a","cap_capbank0b", "cap_capbank0c", "cap_capbank1a", "cap_capbank1b", "cap_capbank1c", "cap_capbank2a", "cap_capbank2b", "cap_capbank2c", "cap_capbank3"],
         "voltage_measurements": ["nd_l2955047", "nd_l3160107", "nd_l2673313", "nd_l2876814", "nd_m1047574", "nd_l3254238"]
       },
   "log" : {
         "name":"string",
         "location":"ref_location1234"
     },
     "events" : [

     ],
     "rules":[
        {"name": "app_rules.py",
         "port": 5000,
         "topic":"input"
      }  ]
  }


3. Expected results series:
Time series json structure with expected results.

::

  {
      "expected_outputs": {
          "1": {
              "simulation_id": "2034749692",
              "message": {
                  "timestamp": "2018-05-03 18:24:20.464399",
                  "measurements": [
                      {
                          "measurement_mrid": "21558b56-380b-4969-9ce1-9b1c91824a76",
                          "value": 1
                      }, ...]
                      }
                }
      }
  }


4. Rules

The rules used for testing are using a package called durable_rules https://github.com/jruizgit/rules

The rules application allow developers to describe the event to match (antecedent) and the action to take (consequent).
The implementation run by the test manager is expected to be in python, but durable_rules can be written in javascript and ruby.


The rules application is started by the test manager and messages sent to
simulation.input.[simulationId] and simulation.output.[simulationId] will be
forwarded to http://localhost:5000/input/events


::


5. Request Test message API

The request test message is sent to the "goss.gridappsd.test" topic and will cause put the test manager into test mode.

The test message contains the following:

* testConfigPath - Full path to the test config.
* testScriptPath - Full path to the test config.
* rulePort - Port to use for the rules app, the default is 5000.
* topic - topic to use for the rule app, the default is input.
* expectedResult - Full path to the expected result test series data.

.. code-block:: python

  loc ='/gridappsd/applications/sample_app/tests'
  testCfg = {"testConfigPath":loc+"/SampleTestConfig.json",
          "testScriptPath":loc+"/SampleTestScript.json",
          "simulationID": 1234,
          "rulePort": 5000,
          "topic":"input",
          "expectedResult":loc + "/expected_result_series_filtered_8500.json"
          }



Run request_test.py provided for the sample app

.. code-block:: bash

  user@foo>python request_test.py
