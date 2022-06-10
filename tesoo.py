
import types

#WHen saving from protege use OWL/XML Syntax and .owl extension!
from owlready2 import *

onto = get_ontology("file://C:/Users/silve/OneDrive/Documenti/Git/tesoo/tesoo_owl.owl").load()

print(onto.Auridon)

print(list(onto.classes()))

"""
Search search() does not perform any kind of reasoning, it just searches in asserted facts. In addition, it cannot find Classes through SOME or ONLY restrictions.

iri, for searching entities by its full IRI
type, for searching Individuals of a given Class
subclass_of, for searching subclasses of a given Class
is_a, for searching both Individuals and subclasses of a given Class
subproperty_of, for searching subproperty of a given Property
any object, data or annotation property name

"""
print( onto.search(subclass_of=  onto.npc))


#Annidate search
print( onto.search(is_a=  onto.Quest , quest_located_in = onto.The_Harborage))


#Add a class
class Drug(Thing):
    namespace = onto


#Multiple inheritance classes
class DrugAssociation(Drug): # A drug associating several active principles
    pass


#is_a method that returns superclass, opposite of .subclasses()
print(DrugAssociation.is_a)

#descendant and ancestor methods

print(DrugAssociation.ancestors())




with onto:
    DynamicClass = types.new_class("DynamicClass", (Drug,))


#In the descendants of Drug we'll find DynamicClass
print(Drug.descendants())



"""
---------INDIVIDUALS------------------------
"""

my_drug = Drug("my_drug")
print(my_drug.name)

#auto named individual

unamed_drug = Drug()
print(unamed_drug.name)


#Iterate over instances of the class
for i in Drug.instances(): print(i)


#Same as relation
assert Drug("my_drug3") is Drug("my_drug3")     


#Saving, OWL/XML is not yet supported for writing, only refxml is supported
onto.save(file = "C:/Users/silve/OneDrive/Documenti/Git/tesoo/tesoo_py_save", format = "rdfxml")