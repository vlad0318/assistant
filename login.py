import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

	def __init__(self,**kwargs):
		super(LoginScreen,self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text='username'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True,multiline=False)
		self.add_widget(self.password)
