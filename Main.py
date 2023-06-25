from kivy.app import App
from kivy.core.window import Window

from Layout import MainLayout
from GameController import *
from PokemonController import *
from random import randint
import os


class Main(App):
	currentDir = os.getcwd()
	dataBaseFile = os.path.join(
		currentDir, "Pokedex.csv"
	)
	ctrl = Controller(dataBaseFile)
	pkmCtrl = PokemonController()
	allPkmNames = ctrl.getNames()
	hTable = ctrl.mountHashTable()
	attempts = 0
	randPkm = None
	layout = MainLayout()

	def build(self):
		windowcolor = (0.102, 0.102, 0.141, 1)
		Window.clearcolor = windowcolor
		Window.size = (313, 700)

		self.layout.bx_input.btn_play.bind(
			on_release=self.click
		)
		self.layout.bx_input.ti_name.bind(
			on_text_validate=self.click
		)
		self.layout.bx_input.ti_name.bind(
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
			lenNames = len(names)
			if lenNames >= 3:
				for i in range(3):
					show += names[i]
					if i < 2:
						show += ", "
			else:
				for i in range(lenNames):
					show += names[i]
					if i == 0 and lenNames == 2:
						show += ", "
		self.layout.lbl_suggestion.text = \
			show

	def click(self, instance):
		if self.layout.bx_input.btn_play.status:
			self.play()
		else:
			self.replay()

	def replay(self):
		self.layout.bx_input.remove_widget(self.layout.bx_input.btn_play)
		self.layout.bx_input.add_widget(
			self.layout.bx_input.lbl_name
		)
		self.layout.bx_input.add_widget(
			self.layout.bx_input.ti_name
		)
		self.layout.bx_input.add_widget(
			self.layout.bx_input.btn_play
		)
		self.layout.setDefault()
		self.attempts = 0
		self.randPkm = self.randomPkm()
		self.layout.bx_input.btn_play.status = True

	def play(self):
		self.layout.lbl_suggestion.text = ""
		name = self.layout.bx_input.ti_name.text
		usrPkm = self.hTable.getPkm(name)
		if not usrPkm:
			return
		isEqual = self.pkmCtrl.equals(
			usrPkm,
			self.randPkm
		)
		self.compare(usrPkm)
		self.layout.bx_input.ti_name.text = ""
		self.attempts += 1
		if isEqual:
			self.win(usrPkm)
			self.layout.bx_input.btn_play.status = False

	def win(self, pkm):
		pkmId = self.getIdMsg(int(pkm.id))

		imgName = f"img/{pkmId}.png"
		self.layout.img_randpkm.source = imgName
		self.layout.bx_input.btn_play.text = "Jogar de Novo"
		self.layout.bx_input.remove_widget(self.layout.bx_input.lbl_name)
		self.layout.bx_input.remove_widget(self.layout.bx_input.ti_name)
		self.layout.lbl_suggestion.text = f'You win in {self.attempts} attempts!'

	def compare(self, pkm):
		pkmId = self.getIdMsg(int(pkm.id))

		imgName = f"img/{pkmId}.png"
		self.layout.bx_info.img_pkm.source = imgName
		self.setLabelTypes(
			pkm.types[0],
			self.layout.bx_info.lbl_type1,
			self.randPkm.types[0]
		)
		self.setLabelTypes(
			pkm.types[1],
			self.layout.bx_info.lbl_type2,
			self.randPkm.types[1]
		)
		self.setLabelNumeric(
			pkm.weight,
			self.randPkm.weight,
			self.layout.bx_info.lbl_weight
		)
		self.setLabelNumeric(
			pkm.height,
			self.randPkm.height,
			self.layout.bx_info.lbl_height
		)

	@staticmethod
	def setLabelTypes(type_a, label, type_b):
		label.text = type_a
		label.color = (1, 0, 0, 1)
		if type_a == type_b:
			label.color = (0, 1, 0, 1)

	@staticmethod
	def setLabelNumeric(value_a, value_b, label):
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

	@staticmethod
	def getIdMsg(pkm_id):
		strId = str(pkm_id)
		if pkm_id < 10:
			strId = "00" + strId
		elif pkm_id < 100:
			strId = "0" + strId
		return strId

	def randomPkm(self):
		pkmId = randint(1, 152)
		pkm = self.pkmCtrl.getRandom(
			pkmId,
			self.allPkmNames,
			self.hTable
		)
		return pkm


if __name__ == '__main__':
	Main().run()
