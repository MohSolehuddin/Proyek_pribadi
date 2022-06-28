import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class jadwal(GridLayout):
    def __init__ (self , **kwargs):
        super(jadwal , self).__init__(**kwargs)
        self.cols=1
        self.ac= GridLayout(
            row_force_default=True,
            row_default_height=400,
            col_force_default=True,
            col_default_width=710)
        self.ac.cols=1
        self.row_force_default=True
        self.row_default_height=350
        self.col_force_default=True
        self.col_default_width=710
        self.ax= GridLayout(row_force_default=True,
            row_default_height=60,
            col_force_default=True,
            col_default_width=145)
        self.ax.cols=5
        
        self.ac.add_widget(Label(text="JADWAL PELAJARAN",font_size=65))
        self.add_widget(self.ac)
    
        self.bu1= Button(text="senin",font_size=45)
        self.bu1.bind(on_press=self.senin)
        self.ax.add_widget(self.bu1)
    
        self.bu2= Button(text="selasa",font_size=45)
        self.bu2.bind(on_press=self.selasa)
        self.ax.add_widget(self.bu2)
    
        self.bu3= Button(text="rabu",font_size=45)
        self.bu3.bind(on_press=self.rabu)
        self.ax.add_widget(self.bu3)
    
        self.bu4= Button(text="kamis",font_size=45)
        self.bu4.bind(on_press=self.kamis)
        self.ax.add_widget(self.bu4)
    
        self.bu5= Button(text="Jum'at",font_size=45)
        self.bu5.bind(on_press=self.jumat)
        self.ax.add_widget(self.bu5)
        
        self.add_widget(self.ax)
    
    def senin(self,instance):
        self.add_widget(Label(text="SENIN:\nPkn\nSenbud\nSk", font_size=72))
        
    def selasa(self,instance):
        self.add_widget(Label(text="SELASA:\nDDG\nKJD\nB.INGGRIS", font_size=72))
        
    def rabu(self,instance):
        self.add_widget(Label(text="RABU:\nBADAR  \nMATEMATIKA\nSIMDIG\nFISIKA", font_size=72))
        
    def kamis(self,instance):
        self.add_widget(Label(text="KAMIS:\n   SEJARAH INDONESIA\nKIMIA\nPAI", font_size=72))
        
    def jumat(self,instance):
        self.add_widget(Label(text="JUM'AT:\nPD\nB.INDONESIA\nBP\nPJOK", font_size=72))
    
class Apk(App):
    def build(self):
        return jadwal()
        
if __name__=='__main__':
    Apk().run()