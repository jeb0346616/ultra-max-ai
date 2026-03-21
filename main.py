from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from ai_model import predict

class MyApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical')

        self.input = TextInput(hint_text='Enter B/S sequence')
        self.box.add_widget(self.input)

        self.result = Label(text='Result')
        self.box.add_widget(self.result)

        btn = Label(text='(Type data, app will auto predict)')
        self.box.add_widget(btn)

        self.input.bind(text=self.on_text)

        return self.box

    def on_text(self, instance, value):
        pred = predict(value)
        self.result.text = f'Prediction: {pred}'

MyApp().run()