The Test Manager is responsible for testing an application or service against different events or scenarios.
When the test manager receives a request test message with a specified simulation ID it will forward the simulation
input and output to the specified port for the rules application and compare the simulation output with the expected results

1. Test Configuration

The test configuration contains information to define the simulation run,
initial conditions and default values.

Example:

::

  {
      "power_system_configuration":"ieee8500",
      "simulation_configuration":"ieee8500",
      "duration":60,
      "run_start":"2018-05-03 12:00:00",
      "run_end":"2018-05-03 12:00:00",
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

`Supported Application or Service Types`_

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

The rules application is started by the test manager and messages sent to
simulation.input.[simulationId] and simulation.output.[simulationId] will be
forwarded to http://localhost:5000/input/events

Snippet to listen for changes to ShuntCompensators, i.e. CIM capacitors.

.. code-block:: python

  shunt_dict = defaultdict(lambda: {'count':0})
  shunt_threshold = 4
  
  # A Reverse and a Forward difference is a state change.
  @when_all((m.message.reverse_differences.allItems(item.attribute == 'ShuntCompensator.sections')) & (
  m.message.forward_differences.allItems(item.attribute == 'ShuntCompensator.sections')))
  def shunt_change(c):
      # consequent
      for i,f in enumerate(c.m.message.reverse_differences):
          c.post({'shunt_object': f['object'],
                  'action': f['attribute'],
                  'timestamp': c.m.message.timestamp})

  @when_all(+m.shunt_object)
  def count_shunt_object(c):
      shunt_dict[c.m.shunt_object]['count']+=1
      if shunt_dict[c.m.shunt_object]['count'] == shunt_threshold:
          print ('Shunt change threshold '+str(shunt_threshold)+' exceeded for shunt object ' + c.m.shunt_object)
          send_log_msg('Shunt change threshold '+str(shunt_threshold)+' exceeded for shunt object ' + c.m.shunt_object)


5. Request Test message API

There is a request_test.py python script provided for the sample app in gridappsd-sample-app/sample_app/tests/request_test.py
The request_test script will work outside the docker container and submits a request to run a simulation.
It will wait to capture the returned simulation ID. The simulation ID is set in the
test configuration message and that message is sent to the "goss.gridappsd.test" topic.
This will cause put the test manager into test mode. The test manager will now forward simulation
input and output to the specified port for the rules application.

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


The script works from outside of the docker container from either an IDE like PyCharm or from the command line.

.. code-block:: bash

  user@usermachine>python sample_app/tests/request_test.py
