import kivy
from kivy.app import App
from kivy.uix.label import Label

class kunden_projekt_x1(App):
    def build(self):
        return Label(text="DatenbankSystem Goldener Colt")
    
if __name__ == "__main__":
    kunden_projekt_x1().run()