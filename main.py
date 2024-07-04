import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.textinput import TextInput
import add_event


class MyApp(App):

	def build(self):
		return add_event.Add_Event()


if __name__ == '__main__':
	MyApp().run()