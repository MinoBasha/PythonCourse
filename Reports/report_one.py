class First(object):
   def __init__(self):
       print ("first")

class Second(First):
   def __init__(self):
       print ("second")

class Third(First):
   def __init__(self):
       print ("third")

class Fourth(Second, Third):
	def __init__(self):
		Second.__init__(self)
		Third.__init__(self)
        #super(Fourth, super).__init__()
		print ("that's it")

fourth_obj= Fourth()

