import kivy
from kivy.app import App
kivy.require('1.11.0')
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Config.set('graphics', 'resizable', 1)


class Tampilan(GridLayout):
    def senin(self):
        self.add_widget(Label(text="SENIN:\nPkn\nSenbud\nSk",font_size=70))
        
         
    def selasa(self):
        self.add_widget(Label(text= "SELASA:\nDDG\nKJD\nB.INGGRIS",font_size=70))
        
        
    def rabu(self):
        self.add_widget(Label(text ="RABU:\nBADAR  \nMATEMATIKA\nSIMDIG\nFISIKA",font_size=70))
        
        
    def kamis(self):
        self.add_widget(Label(text="KAMIS:\n   SEJARAH INDONESIA\nKIMIA\nPAI",font_size=70))
      
        
    def jumat(self):
      self.add_widget(Label(text="JUM'AT:\nPD\nB.INDONESIA\nBP\nPJOK",font_size=70))
      

class App(App):
    def build(self):
        return Tampilan()
        
if __name__=="__main__":
    App().run()   
