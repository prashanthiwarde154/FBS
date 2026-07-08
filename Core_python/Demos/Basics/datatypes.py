#Data types in python

#-----Numeric------

#1.Integer
var=10
print(type(var))

#2.Float
var=10.33
print(type(var))

#3.complex
var=10+7j
print(type(var))
print(var)

#---------Text-------

#1.String
var='Hello world'
var="Hello world"
var='''Hello world i am coming
to destroy you 2026 me duniya khatam haii'''
var="""jhjhdhff ghgghjfgdhgfhgh hgf
 jdjhjhsjhdfhjhfjhjv   vfvhfgskjfjhjhvhh"""

print(type(var))


#----Sequencial-----

#1.List
var=[1,2,3,4,5]

#2.Tuple 
var=(1,2,3,4,5)
var=1,2,3,4,5

#3.Range
var=range(1,20)

#--------Set Type-----
#1.Set
var={1,2,3,4,5}

#2.frozenset
var=frozenset({1,10})

#-------Mapping-----

#1.dict
var={"Id":101,"Name":"Prashant","Salary":20000}

#------Other-----
#1.boolean
var=True



#2.nonetype
var=None



print(type(var))