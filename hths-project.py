import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout          #Imports, used kivy for python GUI
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import os
kivy.require("1.11.1")
info = ""

class LoginPage(GridLayout):            #login page code start
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username: "))

        self.Username = TextInput(multiline=False)          #username text input
        self.add_widget(self.Username)

        self.add_widget(Label(text="Password: "))

        self.Password= TextInput(multiline=False)           #password text input
        self.add_widget(self.Password)

        self.submit = Button(text="Login")
        self.submit.bind(on_press=self.submit_button)       #button login submission
        self.add_widget(Label())
        self.add_widget(self.submit)

    def submit_button(self, instance):
        Username = self.Username.text
        Password = self.Password.text
        print(f"Attempting to login as {Username}....")

        Home = f"Hello, {Username}"
        Risk_ID.home_page.update_home(Home)

        Risk_ID.screen_manager.current = "Home"

class HomePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="top", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
        self.Checkpatient = Button(text="Check Patient")
        self.Checkpatient.bind(on_press=self.Checkpatient_button)
        self.add_widget(self.Checkpatient)

    def Checkpatient_button(self, instance):
        Risk_ID.screen_manager.current = "Patient"


    def update_home(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size =(self.message.width*0.9, None)

class PatientPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Patient: "))

        self.Patientfile = TextInput(multiline=False)          #patient file input
        self.add_widget(self.Patientfile)

        self.PatientFileSubmit = Button(text="Scan File")
        self.PatientFileSubmit.bind(on_press=self.submit_patient_file)       #button login submission
        self.add_widget(self.PatientFileSubmit)


    def submit_patient_file(self, instance):
        with open("patient.txt", "r") as patient_file_temp:
            patient_file_contents = patient_file_temp.read().lower()
            if patient_file_contents.find("coronary artery disease"):
                info = "[b]I have seen the patient has Coronary Artery Disease,\n I advise the patient to quit smoking,\n reduce/stop consumption of alcohol, maintain healthy weight and\n diet, regular exercise, and come back every 6 months for checkup.[/b]"
                Risk_ID.screen_manager.current = "Info"

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.info = Label(halign="center", valign="top", font_size=20, markup=True, text="[b]I have seen the patient has Coronary Artery Disease,\n I advise the patient to quit smoking,\n reduce/stop consumption of alcohol, maintain healthy weight and\n diet, regular exercise, and come back every 6 months for checkup.[/b]")
        self.add_widget(self.info)

    def update_info(self, info):
        self.info.text = info


class DoctorApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.Login_page = LoginPage()
        screen = Screen(name="Login")
        screen.add_widget(self.Login_page)
        self.screen_manager.add_widget(screen)

        self.home_page = HomePage()
        screen = Screen(name="Home")
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        self.patient_page = PatientPage()
        screen = Screen(name="Patient")
        screen.add_widget(self.patient_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    Risk_ID = DoctorApp()
    Risk_ID.run()
