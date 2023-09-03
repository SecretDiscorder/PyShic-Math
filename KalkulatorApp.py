from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.result)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
            ["^", "sqrt", "log", "sin"],
            ["cos", "tan", "Sin to degree", "Tan to degree", "SPLDV"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        equals_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)
        return layout

    def spldv(self):
        try:
            a = float(self.result.text)
            b = float(self.result2.text)
            hasil1 = float(self.result3.text)
            c = float(self.result4.text)
            d = float(self.result5.text)
            hasil2 = float(self.result6.text)
            determinan = (a * d) - (b * c)
            determinan_x = (d * hasil1) - (b * hasil2)
            determinan_y = (a * hasil2) - (c * hasil1)
            x = determinan_x / determinan
            y = determinan_y / determinan
            self.result.text = f"x: {x}\ny: {y}\nDeterminan: {determinan}"
        except Exception:
            self.result.text = "Error"

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        elif button_text == "=":
            try:
                answer = str(eval(self.result.text))
                self.result.text = answer
            except Exception:
                self.result.text = "Error"
        elif button_text == "sqrt":
            try:
                number = float(current)
                self.result.text = str(math.sqrt(number))
            except Exception:
                self.result.text = "Error"
        elif button_text == "log":
            try:
                number = float(current)
                self.result.text = str(math.log(number))
            except Exception:
                self.result.text = "Error"
        elif button_text == "^":
            self.result.text += "**"
        elif button_text == "sin":
            try:
                number = float(current)
                self.result.text = str(math.sin(math.radians(number)))
            except Exception:
                self.result.text = "Error"
        elif button_text == "cos":
            try:
                number = float(current)
                self.result.text = str(math.cos(math.radians(number)))
            except Exception:
                self.result.text = "Error"
        elif button_text == "tan":
            try:
                number = float(current)
                self.result.text = str(math.tan(math.radians(number)))
            except Exception:
                self.result.text = "Error"
        elif button_text == "Sin to degree":
            try:
                number = float(current)
                self.result.text = str(math.degrees(math.asin(number)))
            except Exception:
                self.result.text = "Error"
        elif button_text == "Tan to degree":
            try:
                number = float(current)
                self.result.text = str(math.degrees(math.atan(number)))
            except Exception:
                self.result.text = "Error"
        elif button_text == "SPLDV":
            # Aktifkan mode SPLDV
            self.result.text = ""
            self.result.hint_text = "Masukan nilai a"
            self.result2 = TextInput(font_size=32, readonly=False, halign="right", multiline=False)
            self.result2.bind(on_text_validate=self.on_spldv_a_entered)
            self.root.add_widget(self.result2)
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_spldv_a_entered(self, instance):
        self.result.text = "Masukan nilai b"
        self.result.hint_text = ""
        instance.readonly = True

    def on_spldv_b_entered(self, instance):
        self.result3.text = "Masukan nilai c"
        self.result.hint_text = ""
        instance.readonly = True

    def on_spldv_c_entered(self, instance):
        self.result2.text = "Masukan hasil 1"
        self.result.hint_text = ""
        instance.readonly = True

    def on_spldv_d_entered(self, instance):
        self.result4.text = "Masukan nilai d"
        self.result.hint_text = ""
        instance.readonly = True

    def on_spldv_e_entered(self, instance):
        self.result5.text = "Masukan hasil 2"
        self.result.hint_text = ""
        instance.readonly = True
        self.spldv()

    def on_solution(self, instance):
        if self.result.text == "SPLDV":
            self.spldv()
        else:
            text = self.result.text
            try:
                answer = str(eval(self.result.text))
                self.result.text = answer
            except Exception:
                self.result.text = "Error"

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
