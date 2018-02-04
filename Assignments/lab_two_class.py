class Person:
	moods=('happy','tired','lazy')
	def __init__(self,name):
		self.name=name
		self.money=0
		self.mood=Person.moods[0]
		self.healthRate=100
	@property
	def healthRate(self):
                return self.__healthRate
	@healthRate.setter
	def healthRate(self,healthRate):
                if(healthRate>=0 and healthRate<=100):
                        self.__healthRate=healthRate
                else:
                        self.__healthRate=100

	def sleep(self,hours):
		if(hours == 7):
			self.mood=moods[0]
		elif(hours < 7):
			self.mood=moods[1]
		else:
			self.mood=moods[2]
	def eat(self,meals):
		if(meals >= 3):
                        self.healthRate=100
		elif(meals == 2):
                        self.healthRate=75
		else:
                        self.healthRate=50
	def buy(self,items):
		self.money-=(items*10)
class Employee(Person):
	def __init__(self,name,distanceToWork,salary,car):
		super().__init__(name)
		self.id=id(self)
		self.distanceToWork=distanceToWork
		self.salary=salary
		self.car=car
	@property
	def salary(self):
		return self.__salary
	@salary.setter
	def salary(self,salary):
		if(salary>=1000):
			self.__salary=salary
		else:
			self.__salary=1000
	def work(self,hours):
		if(hours == 8):
                        self.mood=moods[0]
		elif(hours < 8):
                        self.mood=moods[2]
		else:
                        self.mood=moods[1]

	def drive(self,velocity):
		self.car.run(velocity,self.distanceToWork)
	def refuel(self,gasAmount=100):
		self.car.fuelRate+=gasAmount
class Car:
	def __init__(self,name):
		self.name=name
		self.fuelRate=50
		self.velocity=0
	@property
	def velocity(self):
                return self.__velocity
	@velocity.setter
	def velocity(self,velocity):
		if(velocity>=0 and velocity <=200):
			self.__velocity=velocity
		elif(velocity<0):
			self.__velocity=0
		elif(velocity>200):
			self.__velocity=200
	@property
	def fuelRate(self):
                return self.__fuelRate
	@fuelRate.setter
	def fuelRate(self,fuelRate):
                if(fuelRate>=0 and fuelRate <=100):
                        self.__fuelRate=fuelRate
                elif(fuelRate<0):
                        self.__fuelRate=0
                elif(fuelRate>100):
                        self.__fuelRate=100


	def run(self,velocity,distance ):
		if(fuelRate>=distance):
			self.fuelRate-=distance
			self.velocity=velocity
			distance=0
			self.stop(distance)
		else:
			self.velocity=velocity
			distance-=self.fuelRate
			self.fuelRate=0
			self.stop(distance)


	def stop(self,remaining):
		self.velocity=0
		if(remaining==0):
			print("7amdella")
		else:
			print("Ya mosahhel.. fadel",remaining,"KM")
class Office:
	def __init__(self,name):
		self.name=name
		self.employees={}
	def getAllEmployees(self):
		pass
	def getEmployee(self):
		pass
	def hire(self):
		pass
	def fire(self):
		pass
	def calculateLateness(self):
		pass
	def deduct(self):
		pass
	def reward(self):
                pass
