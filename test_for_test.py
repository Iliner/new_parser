from tkinter import *
import random
 
# class Block:
#     def __init__(self, master):
#         self.e = Entry(master, width=20)
#         self.b = Button(master, text="Преобразовать")
#         self.l = Label(master, bg='black', fg='white', width=20)
#         self.e.pack()
#         self.b.pack()
#         self.l.pack()
#     def setFunc(self, func):
#         self.b['command'] = eval('self.' + func)	
#     def strToSortlist(self):
#         s = self.e.get()
#         s = s.split()
#         s.sort()
#         self.l['text'] = ' '.join(s)
#     def strReverse(self):
#         s = self.e.get()
#         s = s.split()
#         s.reverse()
#         self.l['text'] = ' '.join(s)
 
# root = Tk()
 
# first_block = Block(root)
# first_block.setFunc('strToSortlist')
 
# second_block = Block(root)
# second_block.setFunc('strReverse')
 
# root.mainloop()

# class Table:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height

# 	def square(self):
# 		return self.width + self.height


# class MyTable(Table):
# 	def __init__(self, width, height, places):
# 		super(MyTable, self).__init__(width, height)
# 		self.places = places

# 	def square(self, e):
# 		return Table.square(self) - e




# first = Table(20, 40)
# second = MyTable(20, 30, 1)
# print(second.square(1))



# class Solder:
# 	def __init__(self, number, team):
# 		self.team = team
# 		self.number = number

# 	def to_hero(self, hero):
# 		return hero.number, self.number

# class Hero:
# 	def __init__(self, number, team):
# 		self.team = team
# 		self.number = number
# 		self.lvl = 0

# 	def up_lvl(self):
# 		self.lvl += 1


# hero_team_first = Hero(1, 1)
# hero_team_second = Hero(2, 2)

# list_team_first = []
# list_team_second = []
# count = 0
# while count < 10:
# 	team_for_solder = random.randrange(1, 3)
# 	number_for_solder = random.random()
# 	if team_for_solder == 1:
# 		list_team_first.append(Solder(number_for_solder, team_for_solder))
# 	else:
# 		list_team_second.append(Solder(number_for_solder, team_for_solder))
# 	count += 1	

# if len(list_team_first) > len(list_team_second):
# 	hero_team_first.up_lvl()
# 	#print(hero_team_first.number)
# else:
# 	hero_team_second.up_lvl()
# 	#print(hero_team_second.number)

# print(list_team_first[0].to_hero(hero_team_first))





class Character:
	uniq_number = 0	
	def __init__(self, team_number):
		self.team_number = team_number
		Character.uniq_number += 1
		self.number = Character.uniq_number





class Solder(Character):

	def to_hero(self, hero):
		return hero.number, self.number



class Hero(Character):
	
	def __init__(self, team_number): # Если сдесь обьявить team=[] то почему то у нас список не сбрасывается для каждого отдельного экземпляра.
		super(Hero, self).__init__(team_number)
		self.lvl = 0
		self.team = []

	def up_lvl(self):
		self.lvl += 1

	def add_solder(self, solder):
		return self.team.append(solder)

	def look_count_team(self):
		return len(self.team)


a = Hero(1)


# hero_team_first = Hero(1, 1, [])
# hero_team_second = Hero(2, 2, [])
# count = 0
# while count < 10:
# 	team_for_solder = random.randrange(1, 3)
# 	number_for_solder = random.random()
# 	if team_for_solder == 1:
# 		hero_team_first.add_solder(Solder(number_for_solder, team_for_solder))
# 	else:
# 		hero_team_second.add_solder(Solder(number_for_solder, team_for_solder))
# 	count += 1	



# if hero_team_first.look_count_team() > hero_team_second.look_count_team():
# 	hero_team_first.up_lvl()
# else:
# 	hero_team_second.up_lvl()

# print(hero_team_first.team[0].to_hero(hero_team_first))






# class A:
# 	def __init__(self, n):
# 		self.number  = n


# 	def __add__(self, obj):
# 		self.number = self.number + obj.number
# 		return self.number 

# class B:

# 	def __init__(self, n):
# 		self.number  = n

# 	def __add__(self, obj):
# 		self.number = self.number + obj.number
# 		return self.number 

# first = A(2)
# second = B(3)

# print(first + second









# class Solder:
# 	def __init__(self, number, team):
# 		self.team = team
# 		self.number = number

# 	def to_hero(self, hero):
# 		return hero.number, self.number

# class Hero:
# 	def __init__(self, number, team_number, team): # Если сдесь обьявить team=[] то почему то у нас список не сбрасывается для каждого отдельного экземпляра.
# 		self.team_number = team_number
# 		self.number = number
# 		self.lvl = 0
# 		self.team = team

# 	def up_lvl(self):
# 		self.lvl += 1

# 	def add_solder(self, solder):
# 		return self.team.append(solder)

# 	def look_count_team(self):
# 		return len(self.team)

# hero_team_first = Hero(1, 1, [])
# hero_team_second = Hero(2, 2, [])
# count = 0
# while count < 10:
# 	team_for_solder = random.randrange(1, 3)
# 	number_for_solder = random.random()
# 	if team_for_solder == 1:
# 		hero_team_first.add_solder(Solder(number_for_solder, team_for_solder))
# 	else:
# 		hero_team_second.add_solder(Solder(number_for_solder, team_for_solder))
# 	count += 1	



# if hero_team_first.look_count_team() > hero_team_second.look_count_team():
# 	hero_team_first.up_lvl()
# else:
# 	hero_team_second.up_lvl()

# print(hero_team_first.team[0].to_hero(hero_team_first))

