from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class WeatherApp(App):
    pass


class AddLocationForm(BoxLayout):

    tbSearchLocation = ObjectProperty()

    def on_search(self):
        print(self.tbSearchLocation.text)

if __name__ == '__main__':
    WeatherApp().run()
    #AddLocationFormApp().run()