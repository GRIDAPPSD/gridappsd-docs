.. _using:


Using GridAPPS-D
================

.. include:: rc1_overview.rst

Uploading Model into Blazegraph
-------------------------------

.. include:: Uploading_model_using_blazegraph_workbench.rst

Inserting Measurements into Blazegraph
--------------------------------------

.. include:: Inserting_measurements_blazegraph.rst

Using Platform API
------------------

Applications and services can use either publish/subscribe mechanism or Python API to interact with GridAPPS-D platform.

Publish/Subscribe mechanism can be implemented using any of the language bindings for ActiveMQ messaging framework.

Python API wraps the publish/subscribe messaging and makes the interaction easier for Python apps/services. 
For more information on Python API and how to use it, look at  https://github.com/GRIDAPPSD/gridappsd-python and 
https://github.com/GRIDAPPSD/gridappsd-sample-app. 

Following sections describe the messaging APIs and the corresponding Python API function to interact with platform. 
Where no Python API function is mentioned, following generic functions can be used.

::


	send(self, topic, message)
	get_response(self, topic, message, timeout=5)
	subscribe(self, topic, callback, id=None)


Powergrid Model API
-------------------
.. include:: api_examples/pg_data_manager.rst

Configuration File API
-----------------------------
.. include:: api_examples/config_data_manager.rst


Logging API
-----------

.. include:: logging_status.rst

Simulation API
--------------

.. include:: api_examples/simulation_request.rst

Timeseries API
--------------

.. include:: api_examples/timeseries_data_api.rst

Services
--------

`Sensor Simulator Service <https://gridappsd-sensor-simulator.readthedocs.io>`_
The `GridAPPSD's Sensor Simulator` simulates real devices based upon the magnitude of "prestine" simulated values.
Currently the sensor service supports angle and magnitude measurements.

'_GridAPPS-D DNP3 Service <https://gridappsd-dnp3.readthedocs.io/en/develop/>'__ 
The `GridAPPS-D DNP3 Service` integrates GridAPPS-D with DNP3 based commercial tools to enable the CIM and DNP3 data exchange of the devices.

Hosting Application
-------------------

.. include:: Developing_Apps.rst
