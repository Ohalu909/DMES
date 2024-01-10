from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import pandas as pd


from helpers import screen_helper

from experta import *

from database import Database
from dmes import DMES

db = Database()
es = DMES()

Window.size = (300, 500)


class MenuScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignUpScreen(Screen):
    pass

class IntroScreen1(Screen):
    pass

class IntroScreen2(Screen):
    pass

class IntroScreen3(Screen):
    pass

class MainScreen(Screen):
    pass

class CarbScreen1(Screen):
    # Reference for information in this screen:
    # Muiz. (2017, April 18). Pengiraan karbohidrat untuk pesakit diabetes - PENDIDIKAN PESAKIT. PENDIDIKAN PESAKIT. http://pendidikanpesakit.myhealth.gov.my/pengiraan-karbohidrat-bagi-pesakit-diabetes/
    pass

class CarbScreen2(Screen):
    def on_pre_enter(self, *args):
        self.add_datatable()

    def add_datatable(self):
        try:
            excel_file_path = r"C:\Users\Afifah Abdul Halim\DMES\carbo_exchange.xlsx"
            df = pd.read_excel(excel_file_path, sheet_name="Sheet1")

            column_names = df.columns.tolist()
            data = df.values.tolist()

            datatable = MDDataTable(
                size_hint=(0.9, 0.5),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                column_data=[
                    (col_name, dp(30)) for col_name in column_names
                ],
                row_data=data
            )

            self.add_widget(datatable)
        except Exception as e:
            print(f"An error occurred: {e}")
        
class ReadingTypeScreen(Screen):
    pass


class AskBGLScreen(Screen):
    pass


class AskMealTakenScreen(Screen):
    pass


class OutputScreen(Screen):
    pass

class OutputScreen2(Screen):
    pass

class OutputScreen3(Screen):
    pass

class User(Fact):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignUpScreen(name='signup'))
sm.add_widget(IntroScreen1(name='intro1'))
sm.add_widget(IntroScreen2(name='intro2'))
sm.add_widget(IntroScreen3(name='intro3'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(CarbScreen1(name='carb_intro'))
sm.add_widget(CarbScreen2(name='carb_exchange'))
sm.add_widget(ReadingTypeScreen(name='reading_type'))
sm.add_widget(AskBGLScreen(name='ask_bgl'))
sm.add_widget(OutputScreen(name='output'))
sm.add_widget(OutputScreen2(name='output2'))
sm.add_widget(OutputScreen3(name='output3'))

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8

        return screen

    def show_password(self, checkbox, value):
        try:
            password_textfield = self.root.ids.password

            if value:
                password_textfield.password = False
                self.root.password_text.text = "Sembunyi kata laluan"
            else:
                password_textfield.password = True
                self.root.password_text.text = "Tunjuk kata laluan"
        except Exception as e:
            print(f"An error occurred: {e}")

    def signup(self, username, password):
        db.register_user(username.text, password.text)

    def login(self, username, password):
        login_result = db.authenticate_user(username.text, password.text)
        if login_result:
            try:
                print('username: ', username.text)
                app = MDApp.get_running_app()
                app.root.current = 'intro1'
                # app.root.current = 'main'
                print('successfully redirect to intro1 screen')

                bgl_reading = db.get_last_entry("bgl_reading")
                entry_date = db.get_last_entry("entry_date")
                main_screen = self.root.get_screen("main")
                if bgl_reading is not None:
                    main_screen.ids.data_label.text = str(bgl_reading)
                    main_screen.ids.data_label_2.text = str(entry_date)
                else:
                    main_screen.ids.data_label.text = "0"

            except Exception as e:
                print("Error:", e)
        else:
            print('incorrect credentials')
            # Login failed
            snackbar = Snackbar(text="Nama pengguna/kata laluan salah!")
            snackbar.open()

    def add_reading_type(self, rt):
        db.insert_reading_type(rt)

    def add_bgl_reading(self, bgl):
        db.insert_bgl_reading(bgl.text)

    def add_meal_taken(self, mt):
        db.insert_meal_taken(mt.text)

    def dmes_logic(self):
        es.reset()
        es.run()

        output_screen = self.root.get_screen("output")
        output_screen2 = self.root.get_screen("output2")

        result_label0 = output_screen.ids.result_label0
        result_label1 = output_screen.ids.result_label1
        result_label2 = output_screen.ids.result_label2
        result_label3 = output_screen2.ids.result_label3

        result_label0.text = ""
        result_label1.text = ""
        result_label2.text = ""
        result_label3.text = ""

        result_label0.text = "\n".join(es.bgl_reading)
        result_label1.text = "\n".join(es.kkm_checker)
        result_label2.text = "\n".join(es.meal_recommendation)
        result_label3.text = "\n".join(es.reasoning)

        es.bgl_reading.clear()
        es.kkm_checker.clear()
        es.meal_recommendation.clear()
        es.reasoning.clear()

        current_screen = self.root.current
        if current_screen != 'output':
            self.root.current = 'output'

    def update_main_card(self):
        bgl_reading = db.get_last_entry("bgl_reading")
        # entry_date = db.get_second_last_entry("entry_date")
        entry_date = db.get_secondary_column("bgl_reading", "entry_date")
        print("entry_date: ", entry_date)
        main_screen = self.root.get_screen("main")
        if bgl_reading is not None:
            # main_screen.ids.data_label.text = str(bgl_reading)
            main_screen.ids.data_label_2.text = str(entry_date) 
        else:
            main_screen.ids.data_label.text = "0"

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Blue" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


if __name__ == '__main__':
    DemoApp().run()
