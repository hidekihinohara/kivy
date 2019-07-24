#coding: utf-8
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from org.hinohara.Generator.ChordScaleGenerator import ChordScaleGenerator
from org.hinohara.Generator.MajorScaleGenerator import MajorScaleGenerator
from org.hinohara.Generator.MinorScaleGenerator import MinorScaleGenerator
from org.hinohara.Generator.ModeScaleGenerator import ModeScaleGenerator


class CustomSpinner(Spinner):
    pass

#文字化け対策
from kivy.core.text import LabelBase, DEFAULT_FONT #追加
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf") #追加

class KeyValidationApp(BoxLayout):
    key = ObjectProperty(None)

    def on_spinner_change(self, text):
        major_scale = MajorScaleGenerator()
        major_scale.set(text)
        self.major_scale.text = major_scale.get()
        minor_scale = MinorScaleGenerator()
        minor_scale.set(text)
        self.minor_scale.text = minor_scale.get()
        chord_scale = ChordScaleGenerator()
        chord_scale.set(text)
        self.chords.text = chord_scale.get()
        mode_scale = ModeScaleGenerator()
        mode_scale.set(text)
        self.modes.text = mode_scale.get()

class KeyValidation(App):
    def build(self):
        return KeyValidationApp()

if __name__ == '__main__':
    KeyValidation().run()