from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

	def __init__(self,**kwargs):
		super(LoginScreen,self).__init__(**kwargs)
		# This sets the amount of columns
		self.cols = 2

		# This sets the username field
		self.add_widget(Label(text='username'))
		self.username = TextInput(multiline=False,hint_text="username")
		self.add_widget(self.username)

		# This sets the username field
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True,multiline=False, hint_text="password")
		self.add_widget(self.password)
