from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

class MainApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x = 'center', anchor_y = "top", padding = [0,10,0,0] )
        balance = 2400.00 #Stores the balance of the user.
  
        label = Label(text="Balance: " + str(balance),
                      size_hint=(.2, .2))
        
        layout.add_widget(label)

        return layout
