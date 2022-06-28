import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class tampilan(GridLayout):
    def __init__(self, **kwargs):
        super(tampilan, self).__init__(**kwargs)
        
        self.cols=1
        self.row_force_default=True
        self.row_default_height= 210
        self.col_force_default=True
        self.col_default_width=700
        
        self.ax= GridLayout(
           row_force_default=True,
           row_default_height= 60,
           col_force_default=True,
           col_default_width=400)

        self.ax.cols=2
        
        self.ax.add_widget(Label(text="nama:"))        
        self.teinn = TextInput(multiline=True)
        self.ax.add_widget(self.teinn)
        
        self.ax.add_widget(Label(text="kelas:"))
        self.teink=TextInput(multiline=True)
        self.ax.add_widget(self.teink)
        
        self.ax.add_widget(Label(text="tanggal lahir:"))
        self.teinl= TextInput(multiline=True)
        self.ax.add_widget(self.teinl)
        
        self.ax.add_widget(Label(text="anak ke:"))
        self.teinak= TextInput(multiline=True)
        self.ax.add_widget(self.teinak)
        
        self.ax.add_widget(Label(text="Alamat:"))        
        self.teina = TextInput(multiline=True)
        self.ax.add_widget(self.teina)
        
        self.add_widget(self.ax)
                                
        self.bu = Button(text="sumbit",
           font_size=32,
           size_hint_y= None,
           height=60,
           size_hint_x= None,
           width=200)
        self.bu.bind(on_press=self.outputan)
        self.add_widget(self.bu)
                
    def outputan(self,instance):
        nama= self.teinn.text
        alamat= self.teina.text
        kelas= self.teink.text
        anakke= self.teinak.text
        lahir= self.teinl.text
                
        self.add_widget(Label(text=f"profil\nnama             : {nama}\nkelas              : {kelas}\ntanggal lahir : {lahir}\nanak ke          : {anakke}\nalamat            : {alamat}"))
              
        self.teinn.text=""
        self.teina.text=""
        self.teink.text=""
        self.teinl.text=""
        self.teinak.text=""
        
class Ap(App):
    def build(self):
        return tampilan()
        
if __name__ == '__main__':
    Ap().run()