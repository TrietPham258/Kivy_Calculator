from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Designate .kv file
Builder.load_file("calc_design.kv")

# Set window size75
Window.size = (500, 600)

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'    

    # Button pressing functions
    def button_press(self, button):
        # Existing element in TextInput
        prior = self.ids.calc_input.text

        # Check for error - Remove error text and convert back to buttons
        if "Invalid Input" in prior:
            prior = ''
        #  Checking
        if prior == '0': 
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}" 

    # Remove last digit Funtion
    def remove(self):
        prior = self.ids.calc_input.text
        # Removing last item
        self.ids.calc_input.text = prior[:-1]
        # Check for emtpy and reset to 0
        exist = self.ids.calc_input.text
        self.ids.calc_input.text = "0" if len(exist)==0 else exist
      
    # Positve and negative numbers
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Check for subtraction sign
        self.ids.calc_input.text = f"{prior.replace('-', '')}" if "-" in prior else f"-{prior}" 

    # Decimal Function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split text box by + 
        num_lst = prior.split("+")
        # Add the decimal 
        if "+" in prior and "." not in num_lst[-1]:
            self.ids.calc_input.text = f'{prior}.'
        elif "." in prior:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'
    
    # Addition Function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # Add the sign
        self.ids.calc_input.text = f"{prior}{sign}"
    
    # Equal Function
    def equals(self):
        prior = self.ids.calc_input.text
        # Removing Excess
        while not prior[-1].isalnum():
            prior = prior[:-1]
        # Error Management  
        try:
            # Math Execution with Python logic
            self.ids.calc_input.text = str(eval(prior))
        except:
            self.ids.calc_input.text = "Invalid Input"


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()

