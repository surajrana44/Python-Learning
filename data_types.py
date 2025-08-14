a=10       #int  type
b=10.23    #float type
c=a+4j     #complex type
print(type(a),type(b),type(c))


is_raining= True   #bool type
is_sunny= False
print(is_raining,is_sunny)

marks=None  #none type  
marks=100
print(marks)

string="thie is not me"  #string type
print(string)

my_list=['data1','data2','data3'] #list type
print(my_list)

my_tuple=('name1','name2','name3') #tuple type 
print(my_tuple)

unique_number={1,2,2,2,3,3,4,6,6,6} #set type ,data can be modified
print(unique_number)

unique_no= frozenset([1,2,2,2,3,3,4,6,6,6])    #set type ,data can not be modified
print(unique_number)

person={ 'name':'suraj','age':22,100:20}   #map type (key:value)
print(person)