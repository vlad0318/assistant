from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Add_Event(GridLayout):
	def __init__(self,**kwargs):
		super(Add_Event,self).__init__(**kwargs)

		# This sets the amount of columns

		self.cols=3

		# Sets the event name fild
		self.add_widget(Label(text='Event Name'))
		self.event_name = TextInput(multiline=False, hint_text="Enter Event Name")
		self.add_widget(self.event_name)


		#Create a dropdown menu

		self.dropdown = DropDown()

		#This part sets the text of the buttons

		self.low_pri = Button(text='This task is low proiorty', size_hint_y = None, height=44)
		self.med_pri = Button(text='This task is medium proiorty', size_hint_y = None, height=44)
		self.high_pri = Button(text='This task is high proiorty', size_hint_y = None, height=44)

		self.options = [self.low_pri,self.med_pri,self.high_pri]

		#This makes the buttons a list for the dropdown menu

		for button in self.options:

			#This is the thing that sets the text equal to the same text as in the buttons

			button.bind(on_release=lambda button: self.dropdown.select(button.text))

			self.dropdown.add_widget(button)


		#Defines the main button

		self.mainbutton = Button(text='Select The Proiorty', size_hint=(1,None))

		#Opens the dropdown menu when clicked

		self.mainbutton.bind(on_release=self.dropdown.open)

		#This sets the input that we selcted as the main button

		self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

		self.add_widget(self.mainbutton)