my_string = 'python'
x = 0

for i in my_string:
   x = x + 1
   print(my_string[0:x])


for i in my_string:
   x = x - 1
   print(my_string[0:x])




2.
my_string = 'python'
   ...: x = 0
   ...: 
   ...: for i in my_string:
   ...:    x = x + 1
   ...:    print(my_string[0:x])
   ...: 
   ...: 
   ...: for i in my_string:
   ...:    x -= 1
   ...:    print(my_string[0:x])
   ...: 

