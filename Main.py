from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from GameController import *
from PokemonController import *
from random import randint


class ButtonPlay (Button):
	def __init__(self, **kwargs):
		super(ButtonPlay, self).\
			__init__(**kwargs)
		
		self.text="Jogar"
		self.italic=True
		self.bold=True
		self.color="000000"
		self.size_hint=(1,1)
		self.background_color="FFCB05"
		self.background_normal=""
		self.status = True


class MainLayout (BoxLayout):
	def __init__(self, **kwargs):
		# call constructor
		super(MainLayout, self).\
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
		f_size = "10 pt"
		f_infosize = "8 pt"
		f_color = "FFCB05"
		
		self.bx_get_name = BoxLayout(
			spacing=20,
			size_hint=(1, 0.08),
		)
		self.bx_show_info = BoxLayout(
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
		self.lbl_name = Label(
			text="Nome: ",
			font_size=f_size,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_type1 = Label(
			text="",
			font_size=f_infosize,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_type2 = Label(
			text="",
			font_size=f_infosize,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_height = Label(
			text="",
			font_size=f_infosize,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
		)
		self.lbl_weight = Label(
			text="",
			font_size=f_infosize,
			color=f_color,
			size_hint=(1, 1),
			bold=False,
			italic=False,
			font_name="DejaVuSans.ttf"
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
		
		self.img_pkm = Image()
		self.img_pkm.source = "img/000_empty.png"
		self.img_pkm.fit_mode = "scale-down"
		self.img_pkm.allow_stretch = True
		self.img_randpkm = Image(
							source="img/000_whoIs.png"
							)
		self.img_randpkm.fit_mode = "scale-down"
		self.img_randpkm.allow_stretch = True
		self.img_randpkm.size_hint = (1, 0.6)
		
		self.btn_play = ButtonPlay()

		widgets_bx_get_name = [
			self.lbl_name,
			self.ti_name,
			self.btn_play
		]
		for widget in widgets_bx_get_name:
			self.bx_get_name.add_widget(widget)

		widgets_bx_show_info = [
			self.img_pkm,
			self.lbl_type1,
			self.lbl_type2,
			self.lbl_height,
			self.lbl_weight
		]
		for widget in widgets_bx_show_info:
			self.bx_show_info.add_widget(widget)

		# add widgets
		widgets = [
			lbl_title, self.img_randpkm,
			self.bx_get_name, self.lbl_suggestion,
			self.bx_show_info
		]
		for widget in widgets:
			self.add_widget(widget)
	
	def setDefault (self):
		self.lbl_type1.text = ""
		self.lbl_type2.text = ""
		self.lbl_height.text = ""
		self.lbl_weight.text = ""
		self.lbl_suggestion.text = ""
		self.img_pkm.source = "img/000_empty.png"
		self.img_randpkm.source="img/000_whoIs.png"
		self.btn_play.text = "Jogar"


class Main(App):
	currentDir = os.getcwd()
	dataBaseFile = os.path.join(\
		currentDir, "Pokedex.csv")
	ctrl = Controller(dataBaseFile)
	pkmCtrl = PokemonController()
	allPkmNames = ctrl.getNames()
	hTable = ctrl.mountHashTable()
	attempts = 0
	randPkm = None
	
	def build(self):
		windowcolor = (0.102, 0.102, 0.141, 1)
		Window.clearcolor = windowcolor
		
		self.layout = MainLayout()
		
		self.layout.btn_play.bind(
			on_release=self.click
		)
		self.layout.ti_name.bind(
			on_text_validate=self.click
		)
		self.layout.ti_name.bind(
			text=self.tap
		)
		
		self.randPkm = self.randomPkm()
		return self.layout
	
	def tap(self, instance, value):
		show = ""
		
		if value != "":
			names = self.ctrl.getSimilarNames(
				value,
				self.allPkmNames
			)
			# TODO ARRUMAR LÓGICA
			lenNames = len(names)
			if lenNames > 0:
				for i in range(len(names)):
					if i < 3:
						show += names[i]
						if i < 2:
							show += ", "
		self.layout.lbl_suggestion.text = \
			show
	
	def click (self, instance):
		if self.layout.btn_play.status:
			self.play()
		else:
			self.replay()
	
	def replay(self):
		self.layout.bx_get_name.remove_widget(self.layout.btn_play)
		self.layout.bx_get_name.add_widget(
			self.layout.lbl_name
		)
		self.layout.bx_get_name.add_widget(
			self.layout.ti_name
		)
		self.layout.bx_get_name.add_widget(
			self.layout.btn_play
		)
		self.layout.setDefault()
		self.attempts = 0
		self.randPkm = self.randomPkm()
		self.layout.btn_play.status = True 
	
	def play(self):
		self.layout.lbl_suggestion.text = ""
		name = self.layout.ti_name.text
		usrPkm = self.hTable.getPkm(name)
		if usrPkm == False:
			return
		isEqual = self.pkmCtrl.equals(
			usrPkm,
			self.randPkm
		)
		self.compare(usrPkm)
		self.layout.ti_name.text = ""
		self.attempts += 1
		if isEqual:
			self.win(usrPkm)
			self.layout.btn_play.status = False
	
	def win(self,  pkm):
		id = self.getIdMsg(int(pkm.id))
		
		imgName = f"img/{id}.png"
		self.layout.img_randpkm.source = imgName
		self.layout.btn_play.text = "Jogar de Novo"
		self.layout.bx_get_name.remove_widget(self.layout.lbl_name)
		self.layout.bx_get_name.remove_widget(self.layout.ti_name)
		self.layout.lbl_suggestion.text = f'You win in {self.attempts} attempts!'
	
	def compare(self, pkm):
		id = self.getIdMsg(int(pkm.id))
		
		imgName = f"img/{id}.png"
		self.layout.img_pkm.source = imgName
		self.setLabelTypes(
			pkm.types[0],
			self.layout.lbl_type1,
			self.randPkm.types[0]
		)
		self.setLabelTypes(
			pkm.types[1],
			self.layout.lbl_type2,
			self.randPkm.types[1]
		)
		self.setLabelNumeric(
			pkm.weight,
			self.randPkm.weight,
			self.layout.lbl_weight
		)
		self.setLabelNumeric(
			pkm.height,
			self.randPkm.height,
			self.layout.lbl_height
		)

	def setLabelTypes(self, type_a, label, type_b):
		label.text = type_a
		label.color = (1, 0, 0, 1)
		if type_a == type_b:
			label.color = (0, 1, 0, 1)

	def setLabelNumeric(self, value_a, value_b, label):
		text = value_a
		value_a = float(value_a)
		value_b = float(value_b)
		label.color = (1, 0, 0, 1)
		if value_a > value_b:
			text += "↓"
		elif value_a < value_b:
			text += "↑"
		else:
			label.color = (0, 1, 0, 1)
		label.text = text

	def getIdMsg(self, id):
		strId = str(id)
		if id < 10:
			strId = "00" + strId
		elif id < 100:
			strId = "0" + strId
		return strId
	
	def randomPkm(self):
		id = randint(1, 152)
		pkm = self.pkmCtrl.getRandom(
			id, 
			self.allPkmNames, 
			self.hTable
		)
		return pkm
		


if __name__ == '__main__':
	Main().run()






















