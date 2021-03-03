#################################################################
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.textinput import TextInput
import math
from kivy.core.window import Window

#################################################################
Config.set('graphics', 'fullscreen', 0)


#################################################################
class CalculatorApp(App):
    def update_label(self):
        self.ti.text = self.formula
    def add_number(self, instance):
        if (self.formula == ''):
            self.formula = ''
        
        self.formula += str(instance.text)
        self.update_label()

#################################################################
    def add_operation(self, instance):
        if(str(instance.text) == '×'):
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()
        
    def add_operation1(self, instance):
        if(str(instance.text) == '÷'):
            self.formula += '/'
        else:
            self.formula += str(instance.text)
        self.update_label()
        
    def add_operation2(self, instance):
        if(str(instance.text) == 'xⁿ'):
            self.formula += '**'
        else:
            self.formula += str(instance.text)
        self.update_label()
        
    def add_operation3(self, instance):
        if(str(instance.text) == '√'):
            self.formula += '**0.5'
        else:
            self.formula += str(instance.text)
        self.update_label()
        
    def add_operation4(self, instance):
        if(str(instance.text) == 'π'):
            self.formula += str(float(math.pi))
        else:
            self.formula += str(instance.text)
        self.update_label()

################################################################# 
    def result(self, instance):
        self.ti.text = str(eval(self.ti.text))
        self.formula = self.ti.text
 
    def menu(self, instance):
        self.formula = ''
        self.update_label()
 
    def clear_one(self, instance):
        self.formula = self.formula[:-1] or ''
        self.update_label()



#################################################################
    def build(self):
        self.formula = ''
        bl = BoxLayout(orientation = 'vertical')
        
        
        
        self.ti = TextInput(text = '', font_size = 40, halign = 'right', size_hint = (1, .4), readonly=True)
        gl = GridLayout(cols = 4, rows = 6, padding = [0], spacing = 0, row_force_default = True, row_default_height = 170)
        
#################################################################
        gl.add_widget(Button(text = 'C', on_press = self.menu, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 35))
        gl.add_widget(Button(text = '(', on_press = self.add_operation, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = ')', on_press = self.add_operation, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 23))
        gl.add_widget(Button(text = 'DEL', on_press = self.clear_one, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 25))

        gl.add_widget(Button(text = 'π', on_press = self.add_operation4, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 35))
        gl.add_widget(Button(text = '√', on_press = self.add_operation3, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = 'xⁿ', on_press = self.add_operation2, background_color = [.65, .65, .65, 1], background_normal = '', font_size = 23))
        gl.add_widget(Button(text = '÷', on_press = self.add_operation1, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 25))
                
        gl.add_widget(Button(text = '7', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '8', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '9', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '×', on_press = self.add_operation, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 21))
        
        gl.add_widget(Button(text = '4', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '5', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '6', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '-', on_press = self.add_operation, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 30))
        
        gl.add_widget(Button(text = '1', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '2', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '3', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '+', on_press = self.add_operation, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 21))
 
        gl.add_widget(Button(text = '.', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '0', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '', on_press = self.add_number, background_color = [.2, .2, .2, 1], background_normal = '', font_size = 21))
        gl.add_widget(Button(text = '=', on_press = self.result, background_color = [0, 255, 255, 0.5], background_normal = '', font_size = 21))
        
#################################################################
        bl.add_widget(self.ti)
        bl.add_widget(gl)
        return bl

#################################################################
if __name__ == "__main__":
    CalculatorApp().run()