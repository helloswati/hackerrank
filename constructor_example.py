# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name, surname='Singh'):
		self.name = name
		self.surname = surname

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name, self.surname)
		print (__name__)


p = Person('Nikhil', 'Gupta')
p.say_hi()


s = Person('Siddhi','Devrukhar')
p.say_hi()
s.say_hi()

d = Person('dk','Gupta')
d.say_hi()

k = Person('kisan')
k.say_hi()


