from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput


class ButtonPlay(Button):
	def __init__(self, **kwargs):
		super(ButtonPlay, self). \
			__init__(**kwargs)

		self.text = "Jogar"
		self.italic = True
		self.bold = True
		self.color = "000000"
		self.size_hint = (1, 1)
		self.background_color = "FFCB05"
		self.background_normal = ""
		self.status = True


class BxInput(BoxLayout):
	def __init__(self, **kwargs):
		super(BxInput, self). \
			__init__(**kwargs)

		self.spacing = 20
		self.size_hint = (1, 0.08)

		f_size = "10 pt"
		f_color = "FFCB05"

		self.img_pkm = Image(
			source="img/000_empty.png"
		)
		self.img_pkm.fit_mode = "scale-down"
		self.img_pkm.allow_stretch = True
		self.ti_name = TextInput(
			multiline=False,
			size_hint=(1, 1)
		)
		self.lbl_name = Label(
			text="Nome: ",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.btn_play = ButtonPlay()

		widgets_bx_get_name = [
			self.lbl_name,
			self.ti_name,
			self.btn_play
		]
		for widget in widgets_bx_get_name:
			self.add_widget(widget)


class BxInfo(BoxLayout):
	def __init__(self, **kwargs):
		super(BxInfo, self). \
			__init__(**kwargs)

		self.spacing = 25
		self.size_hint = (1, 0.2)

		f_size = "8 pt"
		f_color = "FFCB05"

		self.img_pkm = Image(
			source="img/000_empty.png"
		)
		self.img_pkm.fit_mode = "scale-down"
		self.img_pkm.allow_stretch = True
		self.lbl_type1 = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_type2 = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_height = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_weight = Label(
			text="",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)

		widgets_bx_show_info = [
			self.img_pkm,
			self.lbl_type1,
			self.lbl_type2,
			self.lbl_height,
			self.lbl_weight
		]
		for widget in widgets_bx_show_info:
			self.add_widget(widget)


class BxSuggestion(BoxLayout):
	def __init__(self, **kwargs):
		super(BxSuggestion, self). \
			__init__(**kwargs)


class MainLayout(BoxLayout):
	def __init__(self, **kwargs):
		# call constructor
		super(MainLayout, self). \
			__init__(**kwargs)

		# set properties
		self.orientation = "vertical"
		self.spacing = 60

		wide = 0.9
		height = 0.6
		self.size_hint = (wide, height)
		x = 0.5
		y = 0.67
		self.pos_hint = {
			"center_x": x,
			"center_y": y
		}

		# set widgets to add
		f_color = "FFCB05"

		self.bx_input = BxInput()
		self.bx_info = BxInfo()

		lbl_title = Label(
			text="Monkepo",
			font_size="16 pt",
			color=f_color,
			size_hint=(1, 0.2),
			bold=False,
			italic=False
		)
		self.lbl_suggestion = Label(
			text="",
			font_size="8 pt",
			color=f_color,
			size_hint=(1, 0.1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)

		self.img_randpkm = Image(
			source="img/000_whoIs.png"
		)
		self.img_randpkm.fit_mode = "scale-down"
		self.img_randpkm.allow_stretch = True
		self.img_randpkm.size_hint = (1, 0.6)

		# add widgets
		widgets = [
			lbl_title, self.img_randpkm,
			self.bx_input, self.lbl_suggestion,
			self.bx_info
		]
		for widget in widgets:
			self.add_widget(widget)

	def setDefault(self):
		self.bx_info.lbl_type1.text = ""
		self.bx_info.lbl_type2.text = ""
		self.bx_info.lbl_height.text = ""
		self.bx_info.lbl_weight.text = ""
		self.lbl_suggestion.text = ""
		self.img_pkm.source = "img/000_empty.png"
		self.img_randpkm.source = "img/000_whoIs.png"
		self.bx_input.btn_play.text = "Jogar"
