#graphics part
import pygame
pygame.init()

screenHeight= 530
screenWidth= 940

win = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Missionaries and Cannibals")

widthC = 44
heightC = 40
widthM = 44
heightM = 40
widthB = 120
heightB = 39

#logic part
import math

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
	children = [];
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		## Two missionaries cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		## Two cannibals cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ( "(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) + \
					"," + state.boat + "," + str(state.cannibalRight) + "," + \
					str(state.missionaryRight) + ")")
			# here goes the render
			#mainloop
			bg = pygame.image.load('bg.png')
			bg2 = pygame.image.load('bg2.png')
			boat = pygame.image.load('boat.png')
			miss = pygame.image.load('missionary.png')
			can = pygame.image.load('cannibal.png')

			xC1 = 200
			yC1 = 250
			xC2 = 150
			yC2 = 250
			xC3 = 100
			yC3 = 250
			xM1 = 200
			yM1 = 180
			xM2 = 150
			yM2 = 180
			xM3 = 100
			yM3 = 180
			xB = 315
			yB = 250

			def redrawGameWindow2():
			    win.blit(bg2, (0,0))

			    win.blit(miss,(xM1, yM1))
			    win.blit(miss,(xM2, yM2))
			    win.blit(miss,(xM3, yM3))

			    win.blit(can,(xC1, yC1))
			    win.blit(can,(xC2, yC2))
			    win.blit(can,(xC3, yC3))

			    pygame.display.update()

			def redrawGameWindow():
			    win.blit(bg, (0,0))

			    win.blit(miss,(xM1, yM1))
			    win.blit(miss,(xM2, yM2))
			    win.blit(miss,(xM3, yM3))

			    win.blit(can,(xC1, yC1))
			    win.blit(can,(xC2, yC2))
			    win.blit(can,(xC3, yC3))

			    win.blit(boat,(xB, yB))

			    pygame.display.update()

			run = True
			while run:
				for event in pygame.event.get():

					if event.type == pygame.QUIT:
						pygame.quit()

					elif event.type == pygame.MOUSEBUTTONUP:
						if state.cannibalLeft==3 and state.missionaryLeft==3 and state.cannibalRight==0 and state.missionaryRight==0:
								xC1 = 200
								xC2 = 150
								xC3 = 100
								xM1 = 200
								xM2 = 150
								xM3 = 100
								xB = 315
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==1 and state.missionaryLeft==1 and state.cannibalRight==2 and state.missionaryRight==2:
							if state.boat=='left':
								xC1 = 200
								xC2 = 800
								xC3 = 750
								xM1 = 200
								xM2 = 800
								xM3 = 750
								xB = 315
								redrawGameWindow()
								run = False
							else:
								xC1 = 200
								xC2 = 800
								xC3 = 750
								xM1 = 200
								xM2 = 800
								xM3 = 750
								xB = 524
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==1 and state.missionaryLeft==3 and state.cannibalRight==2 and state.missionaryRight==0:
							if state.boat=='left':
								xC1 = 200
								xC2 = 800
								xC3 = 750
								xM1 = 200
								xM2 = 150
								xM3 = 100
								xB = 315
								redrawGameWindow()
								run = False
							else:
								xC1 = 200
								xC2 = 800
								xC3 = 750
								xM1 = 200
								xM2 = 150
								xM3 = 100
								xB = 524
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==2 and state.missionaryLeft==3 and state.cannibalRight==1 and state.missionaryRight==0:
								xC1 = 200
								xC2 = 150
								xC3 = 750
								xM1 = 200
								xM2 = 150
								xM3 = 100
								xB = 315
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==0 and state.missionaryLeft==3 and state.cannibalRight==3 and state.missionaryRight==0:
								xC1 = 700
								xC2 = 800
								xC3 = 750
								xM1 = 200
								xM2 = 150
								xM3 = 100
								xB = 524
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==2 and state.missionaryLeft==2 and state.cannibalRight==1 and state.missionaryRight==1:
								xC1 = 200
								xC2 = 150
								xC3 = 750
								xM1 = 200
								xM2 = 150
								xM3 = 750
								xB = 315
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==2 and state.missionaryLeft==0 and state.cannibalRight==1 and state.missionaryRight==3:
								xC1 = 200
								xC2 = 150
								xC3 = 750
								xM1 = 700
								xM2 = 800
								xM3 = 750
								xB = 524
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==3 and state.missionaryLeft==0 and state.cannibalRight==0 and state.missionaryRight==3:
								xC1 = 200
								xC2 = 150
								xC3 = 100
								xM1 = 700
								xM2 = 800
								xM3 = 750
								xB = 315
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==1 and state.missionaryLeft==0 and state.cannibalRight==2 and state.missionaryRight==3:
								xC1 = 200
								xC2 = 800
								xC3 = 750
								xM1 = 700
								xM2 = 800
								xM3 = 750
								xB = 524
								redrawGameWindow()
								run = False

						elif state.cannibalLeft==0 and state.missionaryLeft==0 and state.cannibalRight==3 and state.missionaryRight==3:
								xC1 = 700
								xC2 = 800
								xC3 = 750
								xM1 = 700
								xM2 = 800
								xM3 = 750
								xB = 524
								redrawGameWindow2()



def main():
	solution = breadth_first_search()
	print ("Missionaries and Cannibals solution:")
	print ("(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)")
	print_solution(solution)

# if called from the command line, call main()
if __name__ == "__main__":
    main()
