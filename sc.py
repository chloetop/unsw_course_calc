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