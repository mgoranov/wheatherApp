from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest


class WeatherApp(App):
    pass


class AddLocationForm(BoxLayout):
    tbSearchLocation = ObjectProperty()
    lstSearchResults = ObjectProperty()

    def on_search(self):
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like"
        search_url = search_template.format(self.tbSearchLocation.text)
        request = UrlRequest(search_url, on_success=self.found_location, on_error=self.notfound_location)

    def notfound_location(self, request, error):
        print(error)

    def found_location(self, request, data):
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        self.lstSearchResults.item_strings = cities
        # print("\n".join(cities))


if __name__ == '__main__':
    WeatherApp().run()