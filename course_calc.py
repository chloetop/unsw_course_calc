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

		if len(selected_course):
			print("Do you want to export your selections?")
			user_input = input(">")

			if user_input.lower() in ['y', 'yes', 'ye']:
				selected_course.export()
				quit()

		quit()

	elif user_input == "check":

		selected_course.check()

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


	elif user_input == "remove":

		selected_course.remove_course()

	elif user_input == "export":
		
		selected_course.export()

	else:
		selected_course.select_course(user_input)




















