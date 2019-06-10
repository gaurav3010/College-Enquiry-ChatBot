from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import aiml
import os
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	 
	@app.route("/", methods=['GET', 'POST'])
	def hello():
		form = ReusableForm(request.form)
		 
		print(form.errors)
		if request.method == 'POST':
			name=request.form['name']
			print(name)
		 
		if form.validate():
		# Save the comment here.

			print(os.getcwd())
			# Create the kernel and learn AIML files
			kernel = aiml.Kernel()
			kernel.learn("std-startup.xml")
			kernel.respond("load aiml b")

			# Press CTRL-C to break this loop
			#while True:
			#print(kernel.respond(input("Enter your message >> ")))
			#ans_form_dataset = kernel.respond(input("Enter your message >> "))

			user_message = request.form['name']
			sem = {'sem-1':'sem1', 'sem-2':'sem2', 'sem-3':'sem3', 'sem-4':'sem4'}
			department = ['Computer', 'IT', 'Electronics', 'Electrical', 'Mechanical', 'Civil', 'Production', 'EC']

			user_message_list = user_message.split(" ")
			#print(user_message_list)

			for msg in user_message_list:
				if msg in department:
					dept_response = msg
				if msg in sem:
					sem_response = sem[msg]

			#print(find_response)
			print(dept_response)
			print(sem_response)
			find_response = dept_response + " " + sem_response
			kernel_response = kernel.respond(find_response)


			flash(kernel_response)
		else:
			flash('All the form fields are required. ')
		 
		return render_template('hello.html', form=form)
 
if __name__ == "__main__":
	app.run()