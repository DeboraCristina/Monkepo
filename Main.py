from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from GameController import *
from PokemonController import *


class MainLayout (BoxLayout):
	def __init__(self, **kwargs):
		# call constructor
		super(MainLayout, self).\
							__init__(**kwargs)
		
		# set properties
		self.orientation = "vertical"
		self.spacing = 100
		
		wide = 0.9
		height = 0.6
		self.size_hint = (wide, height)
		x = 0.5
		y = 0.63
		self.pos_hint = {
			"center_x": x,
			"center_y": y
		}
		
		# set widgets to add
		f_size = "10 pt"
		f_color = "FFCB05"
		
		bx_get_name = BoxLayout(
			spacing=20,
			size_hint=(1, 0.2),
		)
		bx_show_info = BoxLayout(
			spacing=25,
			size_hint=(1, 0.2)
		)
		self.ti_name = TextInput(
			multiline=False,
			size_hint=(1, 1)
		)
		lbl_title = Label(
			text="Monkepo",
			font_size="16 pt",
			color=f_color,
			size_hint=(1, 0.2),
			bold=False,
			italic=False
		)
		lbl_name = Label(
			text="Nome: ",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False
		)
		self.lbl_type1 = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False
		)
		self.lbl_type2 = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False
		)
		self.lbl_height = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False
		)
		self.lbl_weight = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False
		)
		self.lbl_suggestion = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 0.1),
			bold=False,
			italic=False
		)
		
		self.img_pkm = Image()
		self.img_pkm.source = "img/000_empty.png"
		self.img_pkm.fit_mode = "scale-down"
		self.img_pkm.allow_stretch = True
		self.img_randpkm = Image(
							source="img/000_whoIs.png"
							)
		self.img_randpkm.fit_mode = "scale-down"
		self.img_randpkm.allow_stretch = True
		
		self.btn_play = Button(
			text="Jogar",
			italic=True,
			bold=True,
			color="000000",
			background_color="FFCB05",
			background_normal=""
		)

		widgets_bx_get_name = [
			lbl_name,
			self.ti_name,
			self.btn_play
		]
		for widget in widgets_bx_get_name:
			bx_get_name.add_widget(widget)

		widgets_bx_show_info = [
			self.img_pkm,
			self.lbl_type1,
			self.lbl_type2,
			self.lbl_height,
			self.lbl_weight
		]
		for widget in widgets_bx_show_info:
			bx_show_info.add_widget(widget)

		# add widgets
		widgets = [
			lbl_title, self.img_randpkm,
			bx_get_name, self.lbl_sugestion,
			bx_show_info
		]
		for widget in widgets:
			self.add_widget(widget)


class Main(App):
	def build(self):
		windowcolor = (0.102, 0.102, 0.141, 1)
		Window.clearcolor = windowcolor
		
		return MainLayout()
		pass


if __name__ == '__main__':
	Main().run()
