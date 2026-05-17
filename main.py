"""
Минимальное Kivy-приложение для проверки сборки APK.
Если это запустится на телефоне — путь рабочий.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class KozelTest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.label = Label(text='Privet, Kozel!', font_size=40)
        self.add_widget(self.label)

        self.button = Button(text='Tap me', font_size=30)
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

        self.counter = 0

    def on_button_press(self, instance):
        self.counter += 1
        self.label.text = f'Taps: {self.counter}'


class KozelApp(App):
    def build(self):
        return KozelTest()


if __name__ == '__main__':
    KozelApp().run()
