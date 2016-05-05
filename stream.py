from sc import Selected_Course

class Stream:

	def __init__(self, name, spec):
		
		self.name = name
		self.spec = spec

	def req(self,course_list):

		temp_list = course_list.copy()

		course_list.convert_list_to_id(temp_list)

		if "GSOE9820" not in temp_list:
			print("GSOE9820: Engineering Project Management missing \n")

		# if course_list.course_stat()[1] < 9:
		# 	print("Not enough Level 0,1,2,3 courses")
		# 	print("%d courses are missing \n" % (9 - course_list.course_stat()[2]))

		if course_list.course_stat()[0] < 16:
			print("Not enough courses. Overall 16 courses needed.")
			print("%d courses selected, %d courses missing" %(course_list.course_stat()[0], 16 - course_list.course_stat()[0]) )

		if course_list.course_stat()[2] < 6:
			print("Not enough Advanced Disciplinary Knowledge Courses")
			print("%d courses are missing \n" % (6 - course_list.course_stat()[1]))


		self.spec(temp_list)

def dse_spec(course_list):

	print("Checking specliasation for Data Science and Engineering\n")

	cat1 = ["COMP9313", "COMP9315", "COMP9318", "COMP9319"]
	cat2 = ["COMP4418", "COMP6714", "COMP9417", "COMP9444"]
	cat3 = ["COMP4141", "COMP6741", "MATH5845", "MATH5855", "MATH5905", "MATH5960"]


	inter1 = set.intersection(set(cat1), set(course_list))
	inter2 = set.intersection(set(cat2), set(course_list))
	inter3 = set.intersection(set(cat3), set(course_list))

	if (len(inter1) >= 2 and len(inter2) >= 2 and len(inter3) >= 1) or \
	   (len(inter1) >= 1 and len(inter2) >= 2 and len(inter3) >= 2) or \
	   (len(inter1) >= 2 and len(inter2) >= 1 and len(inter3) >= 2):
		print("Stream specialisations courses satisfied")
		return True
	else:
		print("Stream specialisations courses unsatisfied")
		return False

def ai_spec(course_list):

	print("Checking specliasation for Artificial Intelligence\n")

	cat = ["COMP4411", "COMP9431", "COMP4418", "COMP9318", "COMP9417", "COMP9444", "COMP9517"]

	inter = set.intersection(set(cat), set(course_list))

	if len(inter) < 3:
		print("AI Stream specialisations courses unsatisfied")
	else:
		print("AI Stream specialisations courses satisfied")

def bio_spec(course_list):

	print("Checking specliasation for Bioinformatics\n")

	cat1 = ["BINF9010"]
	cat2 = ["BINf9020", "MATH5846", "MATH5856", "COMP9318", "COMP9417"]

	inter = set.intersection(set(cat2), set(course_list))

	if cat1[0] not in course_list:
		print("Missing %s for BIO" % "BINF9010")

	if len(inter) < 3:
		print("BIO Stream specialisations courses unsatisfied")
	else:
		print("BIO Stream specialisations courses satisfied")

def ds_spec(course_list):

	print("Checking specliasation for Database Systems\n")

	cat = ["COMP9315", "COMP9318", "COMP9319", "COMP9321"]

	inter = set.intersection(set(cat), set(course_list))

	if len(inter) < 3:
		print("DS Stream specialisations courses unsatisfied")
	else:
		print("DS Stream specialisations courses satisfied")

def ecs_spec(course_list):

	print("Checking specliasation for E-Commerce Systems\n")

	cat = ["COMP9321", "COMP9322", "COMP9323", "GBAT9117", "TABL5521"]

	inter = set.intersection(set(cat), set(course_list))

	if len(inter) < 3:
		print("ECS Stream specialisations courses unsatisfied")
	else:
		print("ECS Stream specialisations courses satisfied")

def geo_spec(course_list):

	print("Checking specliasation for Geospatial\n")

	cat = ["GEO9016", "GMAT9200", "GMAT9210", "GMAT9300", "GMAT9600", "COMP9318"]

	inter = set.intersection(set(cat), set(course_list))

	if len(inter) < 3:
		print("GEO Stream specialisations courses unsatisfied")
	else:
		print("GEO Stream specialisations courses satisfied")

def ntw_spec(course_list):

	print("Checking specliasation for Internetworking\n")

	cat = ["COMP6733", "COMP9332", "COMP9333", "COMP9334", "COMP9336", "COMP9337", "COMP9441"]

	inter = set.intersection(set(cat), set(course_list))

	if len(inter) < 3:
		print("NTW Stream specialisations courses unsatisfied")
	else:
		print("NTW Stream specialisations courses satisfied")

		

dse = Stream("Data Science and Engineering", dse_spec)
ai = Stream("Artificial Intelligence", ai_spec)
bio = Stream("Bioinformatics", bio_spec)
ds = Stream("Database Systems", ds_spec)
ecs = Stream("E-Commerce Systems", ecs_spec)
geo = Stream("Geospatial", geo_spec)
ntw = Stream("Internetworking", ntw_spec)

