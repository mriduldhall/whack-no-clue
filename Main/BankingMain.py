from Main.DatabaseConnector import Connection
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect

class Scroll(ScrollView):
    pass

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
        return RootUI()
    
    def on_start(self):
        database = Connection(host='165.232.37.228',database='whacknoclue',user='whacknoclueuser',password='P@ssword123')
        transactions_db = database.get_transactions()
        transactions_db.sort(key=lambda x: x[3])
        transactions_db = list(reversed(transactions_db))
        len_transactions = len(transactions_db)

        
        for i in range(len(transactions_db)):
            print(transactions_db[i][1])
            self.root.ids.categories.add_widget(ObtainCategories(text = transactions_db[i][1], color = self.set_color(transactions_db[i][5])))
            self.root.ids.categories.add_widget(ObtainCategories(text = str(transactions_db[i][2]), color = self.set_color(transactions_db[i][5])))
        # for i in range(len(self.root.ids.categories.children)):
        #    self.root.ids.categories.children[i].rgba = self.set_color(transactions_db[i][5])

    def set_color(self,color_id):
        match color_id:
            case 1:
                return (0,0,1,1)
            case 2:
                return (1,0,0,1)
            case 3:
                return (0,1,0,1)
            case 4:
                return (1,1,0,1)
            case 5:
                return (1,0,1,1)
            case 6:
                return (0.5,0.5,0.5,1)

#   database = Connection(host='165.232.37.228',database='whacknoclue',user='whacknoclueuser',password='P@ssword123')
#        db_categories = database.get_categories()
#        for i in range(len(db_categories)):
#            customCategories = ObtainCategories()
#           self.ids.categories.add_widget(customCategories)
#            print(db_categories[i])