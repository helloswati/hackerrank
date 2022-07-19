#class Numbers:
#  def __init__(self, x):
    #
#    a = [1, 2, 3, 4, 5]
#    for i in a:
#        if i % 2 == 1:
#            print(i)

def odd_even(number):
  '''
  Function to figure out odd or even numbers
  '''
  if (number % 2 == 0):
    print ("%d is even" %number)
  else:
    print ("%d is odd" %number)


if __name__ == "__main__":
  while True:
    user_input = input("Enter the number: ")
    if user_input == "quit":
        break
    else:
      pass
    try:
      odd_even(int(user_input))
    except ValueError as ve:
      print ("Entered value is not correct, please enter a numberic value ", ve)
    except Exception as ex:
      print ("Exception Occurred ", ex)
  print(user_input)


