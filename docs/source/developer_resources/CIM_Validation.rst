
This section presents an overview of CIM Validation techniques that
will be expanded upon in the future.  The purpose of CIM validation
is to assess the level of compliance GRIDAPPS-D is using in its 
use of CIM version 100.  

Introduction
^^^^^^^^^^^^

In electrical power distribution and transmission the Common 
Information Model (CIM) is a technology agnostic standard developed by
the International Electrotechnical Commission (IEC).  CIM provides
the blueprints for application software like GridAPPS-D to represent
data structures, message payloads, and information exchanges between
applications.  

To represent the model, CIM is written using the Unified Modeling 
Language (UML) using Sparx Enterprise Architect.  The model is stored
in a project file (*.eap extension file).  

UML Profiles are domain or technology  specific representations
of the original model.  UML profiles are generated in a variety of ways:
including: by hand, using a tool such as CIMContextor/CIMTool.

Extending CIM
^^^^^^^^^^^^^

CIM is built on universally understood power grid concepts which
means that the UML should be generally applicable, When the needs
go beyond the general purpose solution it is possible to extend CIM
for application specific purposes.  When extending CIM to be compliant, 
the extentions comply with the rules and organization of the existing 
model.  Otherwise an uncompliant application risks losing the advantage
of using the standard, particularly for information exchanges.

Techniques for extending the CIM will not be discussed here, however
the IEC TC 57 61970 part 301 document provides excellent guidance on 
best practices when extending the CIM.  The 61970 part 600 
series developed for use by ENTSO-E provides an excellent end-to-end
series of extension use cases for the European power grid.

Validation Techniques
^^^^^^^^^^^^^^^^^^^^^

Well-Formed UML Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^
In the IEC TC 57  13, 14, and 16 Working Groups the CIM Model Managers are 
relied upon for any updates to the UML.  Before a release occurs the
JCleanCim tool (http://tanjakostic.org/jcleancim/index.html) is used
to validate UML package, class, and associations against agreed upon
rules for well-formed UML.  The JCleanCim tool generates a log report
citing any non-compliance items along with other products.  It is 
basically like a software debug tool for CIM UML.   For extensions the
JCimClean tool can be used to review GridAPPS-D extensions and flag
any problematic areas.   In addition the JCimClean tool original log 
report for CIM100 can be compared against the GridAPPS-D CIMv100.


Well-Formed Profile 
^^^^^^^^^^^^^^^^^^^
Two external tools have been developed to create CIM profiles based on
the UML.  Both CIMTool and CIMContextor can create Resource Description 
Framework Schema (RDFS) profiles from CIM to validate how CIMv100 classes 
and associations are transposed into message payload objects.  In addition,
CIMTool does have a means to validate example payloads against payloads to 
flag any formatting or structural errors.


Final Thoughts
^^^^^^^^^^^^^^
This section is expected to evolve in the spring/summer of 2019 with the
advancement of CIM Model Manager tools that were previously only accessible
to the model managers or based on advancements of validation techniques 
in the profile development communities. 
 
