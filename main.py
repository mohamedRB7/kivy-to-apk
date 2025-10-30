from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ArabicApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)

        # نص الترحيب
        self.label = Label(
            text="hello Kivy 🎉",
            font_size="22sp",
            color=(0.2, 0.3, 0.6, 1),
            halign="center"
        )

        # الزر
        self.button = Button(
            text="push here 👇",
            font_size="20sp",
            background_color=(0.1, 0.5, 0.8, 1),
            on_press=self.change_text
        )

        self.add_widget(self.label)
        self.add_widget(self.button)

    def change_text(self, instance):
        self.label.text = "  pushed ✅"


class MyApp(App):
    def build(self):
        self.title = " Kivy app"
        return ArabicApp()


if __name__ == "__main__":
    MyApp().run()
