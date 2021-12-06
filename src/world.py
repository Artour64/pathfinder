import random

#default size
worldX=196
worldY=64

wallcoef=0.2

mindist=16

class Tile:
	def __init__(self):
		self.x=0
		self.y=0
		self.wall=False
		self.visited=False
		self.aDist=0
		
class World:
	def __init__(self,x=worldX,y=worldY):
		self.makeGrid()
		self.a=[0,0]
		self.b=[0,0]
	
	def makeGrid(self,x=worldX,y=worldY):
		self.worldX=x
		self.worldY=y
		self.grid=list()
		for x in range(self.worldX):
			self.grid.append(list())
			for y in range(self.worldY):
				t=Tile()
				self.grid[x].append(t)
				t.x=x
				t.y=y
				#print((id(t),id(t.entity)))
				
	def clearGrid(self):
		for x in self.grid:
			for y in x:
				y.wall=False
				y.visited=False

	def worldGen(self):
		self.clearGrid()
		randX = random.randrange(self.worldX)
		randY = random.randrange(self.worldY)
		for i in range(int(self.worldX*self.worldY*wallcoef)):#generate walls
			attemps=0
			while(self.grid[randX][randY].wall):
				randX = random.randrange(self.worldX)
				randY = random.randrange(self.worldY)
				attemps+=1
				if(attemps>100):
					break
			if(attemps>100):
					break
			self.grid[randX][randY].wall=True
		
		while(self.worldsimplify()):pass;
		self.removeopencorners()
		while(self.worldsimplify()):pass;
	
	def worldsimplify(self):
		q=False
		for x in range(self.worldX):
			for y in range(self.worldY):
				if (not self.grid[x][y].wall):
					xy=[x,y]
					mpsides=self.psides(xy)
					mpsidewalls=self.psidewalls(xy)
					if(mpsides-mpsidewalls<2):
						self.grid[x][y].wall=True
						q=True
					elif(mpsidewalls==0):
						if(self.nocornerwalls(xy,mpsides)):#change to 1 or 0 corner method
							self.grid[x][y].wall=True
							q=True
					elif(mpsidewalls==1):
						if(self.nocornerwalls(xy,mpsides)):
							self.grid[x][y].wall=True
							q=True
						elif(mpsides==4):
							if(self.oneside(xy)):
								self.grid[x][y].wall=True
								q=True
					elif(mpsidewalls==3):
						self.grid[x][y].wall=True
						q=True
		return q
		
	def removeopencorners(self):
		#q=False
		for x in range(self.worldX):
			for y in range(self.worldY):
				if (not self.grid[x][y].wall):
					xy=[x,y]
					mpsides=self.psides(xy)
					mpsidewalls=self.psidewalls(xy)
					if(mpsidewalls==2):
						if(mpsides==4):
							if(not self.closedcorner(xy)):
								self.grid[x][y].wall=True
								#self.grid[x][y].visited=True
								#q=True
		
	def oneside(self,p):
		if(self.grid[p[0]+1][p[1]].wall):
			if(self.grid[p[0]-1][p[1]+1].wall):
				return False
			if(self.grid[p[0]-1][p[1]-1].wall):
				return False
		elif(self.grid[p[0]-1][p[1]].wall):
			if(self.grid[p[0]+1][p[1]+1].wall):
				return False
			if(self.grid[p[0]+1][p[1]-1].wall):
				return False
		elif(self.grid[p[0]][p[1]+1].wall):
			if(self.grid[p[0]+1][p[1]-1].wall):
				return False
			if(self.grid[p[0]-1][p[1]-1].wall):
				return False
		elif(self.grid[p[0]][p[1]-1].wall):
			if(self.grid[p[0]+1][p[1]+1].wall):
				return False
			if(self.grid[p[0]-1][p[1]+1].wall):
				return False
		return True
	
	#'''doesn't produce desired world, fills whole world	
	def closedcorner(self,p):
		#return True
		if(self.grid[p[0]+1][p[1]].wall):
			if(self.grid[p[0]-1][p[1]].wall):
				return True
			if(self.grid[p[0]][p[1]+1].wall):
				return self.grid[p[0]-1][p[1]-1].wall
			elif(self.grid[p[0]][p[1]-1].wall):
				return self.grid[p[0]-1][p[1]+1].wall
		elif(self.grid[p[0]-1][p[1]].wall):
			if(self.grid[p[0]][p[1]+1].wall):
				return self.grid[p[0]+1][p[1]-1].wall
			elif(self.grid[p[0]][p[1]-1].wall):
				return self.grid[p[0]+1][p[1]+1].wall
		return True
	#'''
									
	def nocornerwalls(self,p,mpsides=4):
		#return False
		if(mpsides==4):
			if(self.grid[p[0]+1][p[1]+1].wall):
				return False
			if(self.grid[p[0]-1][p[1]+1].wall):
				return False
			if(self.grid[p[0]+1][p[1]-1].wall):
				return False
			if(self.grid[p[0]-1][p[1]-1].wall):
				return False
		elif(mpsides==3):
			pass
		else:#2
			pass
		return True
	
	def psides(self,p):
		c=4
		if(p[0]==0):
			c-=1
		elif(p[0]==self.worldX-1):
			c-=1
		if(p[1]==0):
			c-=1
		elif(p[1]==self.worldY-1):
			c-=1	
		return c
		
	def psidewalls(self,p):
		c=0
		if(p[0]>0):
			if(self.grid[p[0]-1][p[1]].wall):
				c+=1
			if(p[0]<self.worldX-1):
				if(self.grid[p[0]+1][p[1]].wall):
					c+=1
		elif(self.grid[p[0]+1][p[1]].wall):
			c+=1
			
		if(p[1]>0):
			if(self.grid[p[0]][p[1]-1].wall):
				c+=1
			if(p[1]<self.worldY-1):
				if(self.grid[p[0]][p[1]+1].wall):
					c+=1
		elif(self.grid[p[0]][p[1]+1].wall):
				c+=1
		return c
			
	def pointdist(self):
		return abs(self.a[0]-self.b[0])+abs(self.a[1]-self.b[1])
		
	def randpoints(self):
		attemps=0
		while(attemps<100):
			self.a[0]=random.randrange(self.worldX)
			self.a[1]=random.randrange(self.worldY)
			while(self.grid[self.a[0]][self.a[1]].wall):
				self.a[0]=random.randrange(self.worldX)
				self.a[1]=random.randrange(self.worldY)
			self.b[0]=random.randrange(self.worldX)
			self.b[1]=random.randrange(self.worldY)
			while((self.pointdist()<mindist or self.grid[self.b[0]][self.b[1]].wall) and attemps<100):
				attemps+=1
				self.b[0]=random.randrange(self.worldX)
				self.b[1]=random.randrange(self.worldY)
			if(attemps>=100):
				self.worldGen()
				attemps=0
			else:
				break

