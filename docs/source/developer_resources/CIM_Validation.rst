
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
Language (UML) using Sparx Enterprise Architect. The model is stored 
in a project file (\*.eap extension file).  GridAPPS-D extends the CIM 
to meet its application specific needs. UML (Object Management Group 
UML 2.5 Specification) profiles are secondary models, derived from 
the primary information model.  Profiles represent a portion of the 
model to support GridAPPS-D application-specific structures and 
exchanges.  A profile operates within the scope of the information 
model and is formed by extracting selected elements of the information 
model.  These extracted elements are filtered or constrained by 
providing value ranges, reducing cardinality, and filtering structures.  

UML profiles use stereotype notation <<>> to annotate information model 
elements such as classes, associations, and attributes in a target domain 
or technology.   Stereotypes are either used to impose domain-specific 
criteria (for example, <<CIM:Datatype>>) or technical criteria (for example, 
<<table>>, <<primarykey>>) on UML elements. UML profiles are generated in a 
variety of ways including use of tools such as Enterprise Architect (EA) 
Schema Composer, CIMContextor, or CIMTool to define structural requirements.  
The W3C Shape Constraint Language (SHACL) will be used as extensions to 
further specify value constraints.

Currently GridAPPS-D is using UML diagrams as a human-readable intuitive profile 
description of application-specific uses of the extended CIM.  Future profiles 
will be produced by CIMTool and SHACL to provide a more comprehensive blueprint 
for application development that is machine readable to compliment the diagrams.


Extending CIM
^^^^^^^^^^^^^

CIM is built on universally understood power grid concepts which
means that the UML should be generally applicable, When the needs
go beyond the general purpose solution it is possible to extend CIM
for application specific purposes.  When extending CIM to be compliant, 
the extentions comply with the rules and organization of the existing 
model.  Otherwise an uncompliant application risks losing the advantage
of using the standard, particularly for information exchanges.

Techniques for extending the CIM will not be discussed here, however the 
IEC TC 57 61970 part 301 document and the CIM Model Manager Guide (being 
released Spring 2020 by the TC57 CIM Model Managers) provides excellent 
guidance on best practices when extending the CIM. 


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


Well-Formed and Valid Profile 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CIMTool can not only create Resource Description Framework Schema (RDFS) 
profiles from the CIM100 UML, it can also validate the generated profiles 
or created RDF datasets against CIM100 schema.  GridAPPS-D has plans to 
extend the CIMTool Validation using SHACL to specify and constrain 
value ranges or check regular expression patterns

Final Thoughts
^^^^^^^^^^^^^^
This section is expected to evolve in 2020  with the
advancement of CIM Model Manager tools that were previously only accessible
to the model managers or based on advancements of validation techniques 
in the profile development communities. 
 
