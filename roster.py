

class Wrestler():
	def __init__(self,n,l,w,s,y):
		self.name_first = n
		self.name_last = l
		self.weight = w
		self.scholarship = s
		self.years_of_eligiblity = y
		self.redshirted = False

		

	def __repr__(self):
		return f"{self.name_first} {self.name_last}"

	def redshirt(self):
		if self.redshirted == False:
			self.redshirted = True
			self.years_of_eligiblity += 1
		else:
			print("ERROR. Already redshirted.")
		

class Roster():
	# on deck roster
	# For each WR in Roster --> if WR.yr > 0 & wr.RS == Flase .append ODroster 
	# in the hole roster
	def __init__(self):
		self.roster = []

	def add_to_roster(self, obj):
		self.roster.append(obj)

	def delete_from_roster(self, obj):
		self.roster.remove(obj)

	def money_spent(self):
		spent = 0

		for wrestler in self.roster:
			spent += wrestler.scholarship

		print(f"${spent}")

	def next_yr_roster(self):
		next_yr_roster = []

		for wrestler in self.roster:
			if wrestler.years_of_eligiblity > 1:
				next_yr_roster.append(wrestler)
			elif wrestler.redshirted == False and wrestler.years_of_eligiblity == 0:
				next_yr_roster.append(wrestler)


		return next_yr_roster









roster = Roster()
brock = Wrestler("Brock","Zacherl", 149, 25000, 1)
roster.add_to_roster(brock)
seth = Wrestler("Seth","koleno", 141, 20000, 0)
roster.add_to_roster(seth)
joey = Wrestler("Joey","Fischer", 125, 25000, 4)
roster.add_to_roster(joey)
ty = Wrestler("Ty","Bagoly", 197, 2000, 0)
roster.add_to_roster(ty)
next_yr_roster = roster.next_yr_roster()


print(roster.roster)
print(brock.years_of_eligiblity)
print(ty.redshirted)
print(next_yr_roster)








