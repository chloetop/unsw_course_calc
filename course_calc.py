import copy
import stream
from sc import Selected_Course
import courses
from courses import course_base


selected_course = Selected_Course(course_base)

# main loop
while True:

	user_input = input(">")

	if user_input == "quit":
		quit()

	elif user_input == "check":
		print("Which stream do you want to check upon?")
		print("Choose among these options:")
		print("ai", "bio",'dse', 'ds', 'ecs', 'geo', 'ntw')
		user_input = input(">")
		if "dse" in user_input:
			stream.dse.req(selected_course)
		if "ai" in user_input:
			stream.ai.req(selected_course)
		if "bio" in user_input:
			stream.bio.req(selected_course)	
		if "ds" in user_input:
			stream.ds.req(selected_course)
		if "ecs" in user_input:
			stream.ecs.req(selected_course)
		if "geo" in user_input:
			stream.geo.req(selected_course)
		if "ntw" in user_input:
			stream.ntw.req(selected_course)

	elif user_input == "review":
		selected_course.review()

	elif user_input == "startover":
		print("Are you sure?")
		user_input = input(">")
		if user_input.lower() in ['y', 'yes', 'ye']:
			selected_course = Selected_Course(course_base)
			print("All course deleted!")
		else:
			print("Nothing altered.")
			pass

	else:
		selected_course.select_course(user_input)




















