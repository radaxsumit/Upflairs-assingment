# ----------------------------------------------Dictionary{ 'key' : value}------------------
#dduplication nnot allowed 

# Marks = {'Sumit':9.41 , 'Ronak': 8.00 , 'saurabh': 9.7}
# print(Marks)
# print(type(Marks))
# print(Marks['Ronak'])
# Marks['Sumit'] = 10
# Marks['RAda'] = 100  #a key is not define but added 
# print(Marks)
# print(Marks.values())

student = {"Name":['Sumit','ronak','sorab'],
           "marks" : [10,20,30],
           "subj" : ['physic' , 'maths']}

# print(student['Name'])
# print(student['marks'])
# print(student['subj'])
# student['Name'].remove('Sumit')
# student['marks'].update(10,20000)

student['marks'].update(10)
print(student) 