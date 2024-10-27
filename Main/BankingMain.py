from Main.DatabaseConnector import Connection
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

class HorizBox(Widget):
    pass

class RootUI(FloatLayout):
    pass

class LabelFormat(Label):
    pass

class BalanceFormat(Label):
    pass

class ObtainCategories(Label):
    pass

class rootuiApp(App):
    def build(self):
        database = Connection(host='165.232.37.228',database='whacknoclue',user='whacknoclueuser',password='P@ssword123')
        self.balance = str(database.get_balance())
        print(RootUI().children)
        return RootUI()
    
    def on_start(self):
        database = Connection(host='165.232.37.228',database='whacknoclue',user='whacknoclueuser',password='P@ssword123')
        categories_db = database.get_categories()
        for i in range(len(categories_db)):
            print(categories_db[i][1])
            self.root.ids.categories.add_widget(ObtainCategories(text = categories_db[i][1]))
        print(self.root.ids.categories.children)

#   database = Connection(host='165.232.37.228',database='whacknoclue',user='whacknoclueuser',password='P@ssword123')
#        db_categories = database.get_categories()
#        for i in range(len(db_categories)):
#            customCategories = ObtainCategories()
#           self.ids.categories.add_widget(customCategories)
#            print(db_categories[i])