import time
import stream

class Selected_Course(list):

	def __init__(self,database):
		self.database = database

	def course_stat(self):

		total_num = len(self)
		adv_course_num = 0
		level0123_course_num = 0

		for i in self:
			if i.id == "GSOE9820":
				pass
			elif i.is_adv == 1:
				adv_course_num += 1
			else:
				level0123_course_num += 1

		return [total_num, adv_course_num, level0123_course_num]

	def select_course(self, course_id):

		course_id = course_id.upper()

		for s in self:
			if s.id == course_id:
				print("%s already added! \n" %self.find_course_from_id(course_id).name)
				return 0

		for c in self.database:
			if course_id == c.id:
				self.append(c)
				print("%s added \n" %c.name)
				self.load_req(c)
				return 1

		print("No such course called %s" %course_id)
		return 0


	def load_req(self, c):

		if not c.pre_req:
			return 1
		elif type(c.pre_req[0]) == type([]):
			print("which one do you want? enter an id." \
			      "Availbale courses are %s" \
			      % (c.pre_req[0][0] + " and " +c.pre_req[0][1]))
			user_input = input(">")
			self.select_course(user_input)
		else:
			for sub_c in c.pre_req:
				print("Adding pre_required course %s" %sub_c)
				self.select_course(sub_c)

	def review(self):

		if len(self):
			print("Total number of course selected: %d \n" %self.course_stat()[0])
			print("In which %d general courses are selected" %self.course_stat()[2])
			print("And %d advanced courses are selected\n" %self.course_stat()[1])
			print("The selected courses are:")

			for i in self:
				if i.is_adv:
					print("*" + i.name)
				else:
					print(" " + i.name)
		else:
			print("No course selected")

	def convert_list_to_id(self, a_list):

		for i in range(len(a_list)):
			a_list[i] = a_list[i].id

	def find_course_from_id(self, course_id):
		
		for s in self.database:
			if course_id == s.id:
				return s
		print("no such course called %s!"%course_id)
		return 0

	def remove_course(self):

		if not len(self):
			print("No course to remove")
			return 1

		print("Which course do you want to remove. Indicate Course_ID")
		user_input = input(">")

		course_id = user_input.upper()
		
		for i in range(len(self)):
			if self[i].id == course_id:
				self.pop(i)
				print("%s removed!" %course_id)
				break

	def export(self):

		if len(self):

			file = open('courseSelection.txt', 'a')

			s = "Course selected on "  + time.ctime() + ':\n\n'
			file.write(s)

			for i in self:
				singleEntry = i.name + '\n'
				file.write(singleEntry)

			file.write('-' * 50 + '\n\n')

			file.close()

			print("Selection saved in courseSelection.txt")

		else:

			print("No course to export")
		
	def startover(self):

		self = Selected_Course(self.database)


	def check(self):
		print("Which stream do you want to check upon?")
		print("Choose among these options:")
		print("ai", "bio",'dse', 'ds', 'ecs', 'geo', 'ntw')
		user_input = input(">")
		if "dse" == user_input:
			stream.dse.req(self)
		if "ai"  == user_input:
			stream.ai.req(self)
		if "bio" == user_input:
			stream.bio.req(self)	
		if "ds"  == user_input:
			stream.ds.req(self)
		if "ecs" == user_input:
			stream.ecs.req(self)
		if "geo" == user_input:
			stream.geo.req(self)
		if "ntw" == user_input:
			stream.ntw.req(self)



