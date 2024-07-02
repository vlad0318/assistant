import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.textinput import TextInput
import login


class MyApp(App):

	def build(self):
		return login.LoginScreen()


if __name__ == '__main__':
	MyApp().run()