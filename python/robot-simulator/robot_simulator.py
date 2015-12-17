(NORTH , EAST , SOUTH, WEST) =("NORTH","EAST","SOUTH","WEST")

class Robot:
		
	def __init__(self,bearing=NORTH,x=0,y=0):		
		self.x,self.y = x,y		
		self.bearing = bearing
		
	def __str__(self):
		return " Current position \n Direction:%s \n Coordinates:%s\n"%(self.bearing,self.coordinates)
		
	@property
	def coordinates(self):
		return (self.x,self.y)
	
	def advance(self):				
		if self.bearing ==NORTH:self.y+=1
		if self.bearing ==SOUTH:self.y-=1
		if self.bearing ==WEST:self.x-=1
		if self.bearing ==EAST:self.x+=1
		
	def turn_left(self):
		if self.bearing==NORTH:self.bearing=WEST			
		elif self.bearing==SOUTH:self.bearing=EAST
		elif self.bearing==WEST:self.bearing=SOUTH
		elif self.bearing==EAST:self.bearing=NORTH
		
	def turn_right(self):
		if self.bearing==NORTH:self.bearing=EAST			
		elif self.bearing==SOUTH:self.bearing=WEST
		elif self.bearing==WEST:self.bearing=NORTH
		elif self.bearing==EAST:self.bearing=SOUTH
	
	def simulate(self,commands):
		for cmd in commands:
			if cmd.upper()=="R":self.turn_right()
			elif cmd.upper()=="L":self.turn_left()
			elif cmd.upper()=="A":self.advance()
			else: print("**INVALID MOVEMENT**")

if __name__=="__main__":
	robot = Robot(NORTH,7,3)
	robot.simulate("RAALAL")
	print robot