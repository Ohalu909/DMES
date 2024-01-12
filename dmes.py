from experta import *
from collections import Counter
import random
import linecache
from database import Database
import logging
import pandas as pd


class Action(Fact):
    pass


class User(Fact):
    pass


class Menu(Fact):
    menu = Field(str, mandatory=True)
    menu_class = Field(str, mandatory=True)


class Advice(Fact):
    pass


class MealPlan(Fact):
    pass

# This KnowledgeEngione class manages the working memory of the expert system
# It contains the Facts and Rules
# Rules will use the Facts during the inference process
class DMES(KnowledgeEngine):
    def __init__(self):
        super().__init__()

        # To cconfigure logging (INFO, WARNING, ERROR, DEBUG)
        # logging.basicConfig(level=logging.INFO)
        # logging.getLogger('expert').setLevel(logging.INFO)
        # logging.getLogger('experta.clips').setLevel(logging.INFO)
        # logging.getLogger('experta.defrule').setLevel(logging.INFO)

        # print(logging.getLogger('expert').getEffectiveLevel())
        # print(logging.getLogger('experta.clips').getEffectiveLevel())
        # print(logging.getLogger('experta.defrule').getEffectiveLevel())

        # These lists will hold the output for the Rules that will be used in UI implementation
        self.my_list = []
        self.serving_type_list = []
        self.bgl_reading = []
        self.kkm_checker = []
        self.meal_recommendation = []
        self.reasoning = []
        self.missing_meal = []

        # self.my_list.clear()
        # self.serving_type_list.clear()
        # self.bgl_reading.clear()
        # self.kkm_checker.clear()
        # self.meal_recommendation.clear()
        # self.reasoning.clear()
        # self.missing_meal.clear()

    # This is the knowledge base that contains all the Facts
    @DefFacts() 
    def kb_facts(self):
        yield Fact(action="greet")

        # Menu is a Fact that holds the information about the meal taken and its class in the food pyramid
        excel_file_path = "carbo_exchange.xlsx"
        df = pd.read_excel(excel_file_path, sheet_name="Sheet2")

        for index, row in df.iterrows():
            yield Menu(menu=row['menu'], menu_class=row['menu_class'])

        # yield Menu(menu='q', menu_class='q')
        # yield Menu(menu='roti', menu_class='karbohidrat')
        # yield Menu(menu='nasi putih', menu_class='karbohidrat')
        # yield Menu(menu='nasi', menu_class='karbohidrat')
        # yield Menu(menu='nasi tomato', menu_class='karbohidrat')
        # yield Menu(menu='nasi goreng', menu_class='karbohidrat')
        # yield Menu(menu='roti canai', menu_class='karbohidrat')
        # yield Menu(menu='bihun goreng', menu_class='karbohidrat')
        # yield Menu(menu='bihun sup', menu_class='karbohidrat')
        # yield Menu(menu='bihun kuah', menu_class='karbohidrat')
        # yield Menu(menu='mi goreng', menu_class='karbohidrat')
        # yield Menu(menu='maggi goreng', menu_class='karbohidrat')
        # yield Menu(menu='nasi lemak', menu_class='karbohidrat')
        # yield Menu(menu='kuey tiaw goreng', menu_class='karbohidrat')
        # yield Menu(menu='kuey tiaw sup siam', menu_class='karbohidrat')
        # yield Menu(menu='karipap', menu_class='karbohidrat')
        # yield Menu(menu='cucur', menu_class='karbohidrat')
        # yield Menu(menu='sandwic', menu_class='karbohidrat')
        # yield Menu(menu='nasi minyak', menu_class='karbohidrat')
        # yield Menu(menu='nasi hujan panas', menu_class='karbohidrat')
        # yield Menu(menu='mi bandung', menu_class='karbohidrat')
        # yield Menu(menu='mi kuah', menu_class='karbohidrat')
        # yield Menu(menu='mi kari', menu_class='karbohidrat')
        # yield Menu(menu='mi hailam', menu_class='karbohidrat')
        # yield Menu(menu='nasi ayam', menu_class='karbohidrat')
        # yield Menu(menu='laksa', menu_class='karbohidrat')
        # yield Menu(menu='laksa goreng', menu_class='karbohidrat')
        # yield Menu(menu='capati', menu_class='karbohidrat')

        # yield Menu(menu='sup ayam', menu_class='protein')
        # yield Menu(menu='ketam masak lemak', menu_class='protein')
        # yield Menu(menu='ikan rebus serai', menu_class='protein')
        # yield Menu(menu='ikan stim', menu_class='protein')
        # yield Menu(menu='ikan goreng', menu_class='protein')
        # yield Menu(menu='ikan bakar', menu_class='protein')
        # yield Menu(menu='gulai ikan', menu_class='protein')
        # yield Menu(menu='ikan masak masam manis', menu_class='protein')
        # yield Menu(menu='gulai ayam', menu_class='protein')
        # yield Menu(menu='ayam masak kicap', menu_class='protein')
        # yield Menu(menu='daging masak kicap', menu_class='protein')
        # yield Menu(menu='gulai daging', menu_class='protein')
        # yield Menu(menu='tomyam ayam', menu_class='protein')
        # yield Menu(menu='sup tauhu dan telur', menu_class='protein')
        # yield Menu(menu='ayam goreng', menu_class='protein')
        # yield Menu(menu='ayam bakar', menu_class='protein')
        # yield Menu(menu='sup daging', menu_class='protein')
        # yield Menu(menu='sup tulang ', menu_class='protein')
        # yield Menu(menu='ayam masak lemak', menu_class='protein')
        # yield Menu(menu='ayam kamheong', menu_class='protein')
        # yield Menu(menu='ayam paprik', menu_class='protein')
        # yield Menu(menu='ayam masak merah', menu_class='protein')
        # yield Menu(menu='telur goreng', menu_class='protein')
        # yield Menu(menu='telur dadar', menu_class='protein')
        # yield Menu(menu='gulai telur', menu_class='protein')
        # yield Menu(menu='sup telur', menu_class='protein')
        # yield Menu(menu='daging bakar', menu_class='protein')
        # yield Menu(menu='daging paprik', menu_class='protein')
        # yield Menu(menu='daging masak pedas', menu_class='protein')
        # yield Menu(menu='ikan masak kicap', menu_class='protein')
        # yield Menu(menu='ayam masak sambal', menu_class='protein')
        # yield Menu(menu='ikan masak sambal', menu_class='protein')
        # yield Menu(menu='daging masak lada', menu_class='protein')
        # yield Menu(menu='ikan bakar', menu_class='protein')

        # yield Menu(menu='tomyam', menu_class='serat')
        # yield Menu(menu='nenas', menu_class='serat')
        # yield Menu(menu='mangga', menu_class='serat')
        # yield Menu(menu='ulam', menu_class='serat')
        # yield Menu(menu='kangkung goreng', menu_class='serat')
        # yield Menu(menu='sayur bayam', menu_class='serat')
        # yield Menu(menu='bayam goreng', menu_class='serat')
        # yield Menu(menu='sayur kangkung', menu_class='serat')
        # yield Menu(menu='sayur campur', menu_class='serat')
        # yield Menu(menu='kerabu mangga', menu_class='serat')
        # yield Menu(menu='kerabu taugeh', menu_class='serat')
        # yield Menu(menu='kerabu tauge', menu_class='serat')
        # yield Menu(menu='kacang goreng', menu_class='serat')
        # yield Menu(menu='kacang buncis goreng', menu_class='serat')
        # yield Menu(menu='sawi goreng', menu_class='serat')
        # yield Menu(menu='kailan ikan masin', menu_class='serat')
        # yield Menu(menu='buah naga', menu_class='serat')
        # yield Menu(menu='oren', menu_class='serat')
        # yield Menu(menu='tembikai', menu_class='serat')
        # yield Menu(menu='epal', menu_class='serat')
        # yield Menu(menu='anggur', menu_class='serat')
        # yield Menu(menu='kobis goreng', menu_class='serat')
        # yield Menu(menu='kerabu kacang botor', menu_class='serat')
        # yield Menu(menu='sayur bayam dengan betik', menu_class='serat')
        # yield Menu(menu='sayur manis', menu_class='serat')
        # yield Menu(menu='betik', menu_class='serat')
        # yield Menu(menu='jambu', menu_class='serat')
        # yield Menu(menu='sayur goreng', menu_class='serat')
        # yield Menu(menu='masak lemak labu', menu_class='serat')
        # yield Menu(menu='sayur petola', menu_class='serat')

        # yield Menu(menu='air kosong', menu_class='minuman tanpa gula')
        # yield Menu(menu='teh o suam tanpa gula', menu_class='minuman tanpa gula')
        # yield Menu(menu='teh o ais', menu_class='minuman bergula')
        # yield Menu(menu='teh ais', menu_class='minuman bergula')
        # yield Menu(menu='ais blended', menu_class='minuman bergula')
        # yield Menu(menu='jus oren', menu_class='minuman bergula')
        # yield Menu(menu='air sirap', menu_class='minuman bergula')
        # yield Menu(menu='ais oren', menu_class='minuman bergula')
        # yield Menu(menu='jus tembikai', menu_class='minuman bergula')
        # yield Menu(menu='ais sarsi', menu_class='minuman bergula')
        # yield Menu(menu='teh o limau ais', menu_class='minuman bergula')
        # yield Menu(menu='milo ais', menu_class='minuman bergula')

        
    # This is how the Rules are being created
    # It will have the @Rule tag to specify it as a Rule
    # We will specify the premises as the arguments for Rule
    @Rule(Fact(action='greet'))
    def ask_reading_type(self):

        db = Database()

        # Data about the user from the local database will be retrieved here to be used in the inferencing process
        last_reading_type = db.get_last_entry("reading_type")
        last_bgl_reading = float(db.get_last_entry("bgl_reading"))
        last_meal_taken = db.get_last_entry("meal_taken")

        # The declared data will be declared as Facts to be used in the inferencing process
        self.declare(Fact(type=last_reading_type.lower()))
        self.declare(Fact(reading=last_bgl_reading))
        self.declare(User(meal_taken='q'))
        value_list = last_meal_taken.split(', ')
        for i in value_list:
            self.declare(User(meal_taken=i))
            self.my_list.append(i)
        
        excel_file_path = "carbo_exchange.xlsx"
        df = pd.read_excel(excel_file_path, sheet_name="Sheet2")
        for value in self.my_list:
            if value not in df.iloc[:, 0].values:
                self.missing_meal.append(value)
        if not self.missing_meal:
            print("All values exist in the first column.")
        else:
            print("MISSING VALUES:", self.missing_meal)
        print("MISSING VALUES:", self.missing_meal)
        print('-----Diabetic Monitoring Expert System-----')

    # This rule check the reading type of the patient's blood glucose level
    # It is based on the standard bgl reading that is applicable to all diabetic patients
    # Approved by the Human Expert
    @Rule(Fact(reading=MATCH.reading))
    def reading_type(self, reading):
        if reading < 3.9:
            self.declare(Fact(reading_type="rendah"))
            self.bgl_reading.append('Bacaan gula anda RENDAH')
            print("Bacaan gula anda RENDAH.")
        elif reading > 10:
            self.declare(Fact(reading_type="tinggi"))
            self.bgl_reading.append('Bacaan gula anda TINGGI')
            print("Bacaan gula anda TINGGI.")
        else:
            self.declare(Fact(reading_type="normal"))
            self.bgl_reading.append('Bacaan gula anda NORMAL')
            print("Bacaan gula anda NORMAL.")
        self.declare(Action('print_list'))

    @Rule(Action('print_list'))
    def print_menu_list(self):
        print("Current menu taken list:", self.my_list)
        self.declare(Action('check_serving_type'))

    # This Rule checks the serving type of the meal taken by the user
    # It will go through the Facts list to find th type of class of the food taken by the user
    @Rule(AS.f1 << Action('check_serving_type'),
          AS.f2 << User(meal_taken=MATCH.mta),
          Menu(menu=MATCH.mta,
               menu_class=MATCH.mc))
    def serving_type(self, mc, mta):
        print('serving type = ', mc)
        print('menu taken = ', mta)
        if mc == 'q':
            self.declare(Action('count_serving_type'))
        else:
            self.serving_type_list.append(mc)
        
        # try:
        #     df = pd.read_excel('carbo_exchange.xlsx', 'Sheet2')

        #     if mta not in df.iloc[:, 0].values:
        #         self.missing_meal.append(mta)
        #         raise Exception(f"Meal '{mta}' not found in the Excel file.")
        #     else:
        #         print(mta, ' exist in Excel')
        #         if mc == 'q':
        #             self.declare(Action('count_serving_type'))
        #         else:
        #             # self.serving_type_list.append(mc)
        #             pass

        # except Exception as e:
        #     print(f"Error: {e}")

    # This Rule will count the occurence of the type of class to check with the KKM recommendation
    @Rule(Action('count_serving_type'))
    def count_serving_type(self):
        print("-------------------------------")
        counter = Counter(self.serving_type_list)
        print("Serving type occurrence counts:")
        for serving_type, count in counter.items():
            print(f"{serving_type}: {count}")

        self.declare(Action('check_kkm_recommendation'))

    @Rule(Action('check_kkm_recommendation'))
    def check_kkm_recommendation(self):
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat']

        counter_list1 = Counter(kkm_recommendation)
        counter_list2 = Counter(self.serving_type_list)

        print("-------------------------------\nKKM recommendation checker:")

        if counter_list1 == counter_list2:
            print('satisfy kkm recommendation')
            self.declare(Action('satisfy'))
            self.kkm_checker.append('Mengikut cadangan pemakanan KKM')
        else:
            print('dissatisfy kkm recommendation')
            self.declare(Action('dissatisfy'))
            self.kkm_checker.append('Tidak mengikut cadangan pemakanan KKM')

    # This Rule will check the size of the meal taken base on the bgl reading and and if it satisfy KKM recommendation
    @Rule(Action('satisfy'),
          Fact(reading_type=MATCH.rt))
    def satisfy_recommendation(self, rt):
        if rt == 'rendah':
            self.declare(Advice('Saiz hidangan kecil.'))
            self.declare(Advice('Tambahkan saiz hidangan.'))
        if rt == 'tinggi':
            self.declare(Advice('Saiz hidangan besar.'))
            self.declare(Advice('Kurangkan saiz hidangan.'))
        if rt == 'normal':
            self.declare(Advice('Saiz hidangan normal.'))
            self.declare(Advice('Saiz hidangan memuaskan.'))

    # This rule will check if the meal taken has enough counts of the food class recommemded by the KKM
    @Rule(Action('dissatisfy'),
          Fact(reading_type=MATCH.rt))
    def dissatisfy_recommendation(self, rt):
        if rt == 'rendah':
            self.declare(Advice('Tidak cukup hidangan.'))
        if rt == 'tinggi':
            self.declare(Advice('Terlebih hidangan.'))
        if rt == 'normal':
            self.declare(Advice('Hidangan yang diambil memuaskan.'))
        self.declare(Action('check serving count'))

    # This rule will specify what type of food class that the user should increase or decreaase based on their meal taken
    @Rule(Action('check serving count'))
    def check_serving_count(self):
        print('-----------------------------------------')
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat', 'minuman tanpa gula']

        counter_list1 = Counter(kkm_recommendation)
        counter_list2 = Counter(self.serving_type_list)

        for item, count2 in counter_list2.items():
            count1 = counter_list1[item]
            if count2 < count1:
                count3 = count1 - count2
                self.declare(Advice(f"{'Tambahkan hidangan ber'}{item}{' sebanyak '}{count3}{' hidangan.'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
            elif count2 > count1:
                count3 = count2 - count1
                self.declare(Advice(f"{'Kurangkan hidangan ber'}{item}{' sebanyak '}{count3}{' hidangan.'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
            else:
                self.declare(Advice(f"{item}{' mengikut pecahan hidangan.'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
        self.declare(Action('check_unavailable_serving'))

    # This rule will check the mnissing food class in the user meal taken list, and add advises as part of the final output
    @Rule(Action('check_unavailable_serving'))
    def check_unavailable_serving(self):
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat']

        missing_items = [item for item in kkm_recommendation if item not in self.serving_type_list]
        print('kkm-recs: ', kkm_recommendation)
        print('serving taken: ', self.serving_type_list)
        print('missing items: ', missing_items)
        for i in list(missing_items):
            if i == 'karbohidrat':
                self.declare(Advice('Tambah 1 hidangan karbohidrat.'))
            elif i == 'protein':
                self.declare(Advice('Tambah 1 hidangan protein.'))
            elif i == 'serat':
                self.declare(Advice('Tambah 2 hidangan serat.'))
            else:
                pass
        self.declare(Action('find next meal'))

    @Rule(Action('find next meal'),
          Fact(type=MATCH.t))
    def find_next_meal(self, t):
        if t == 'sebelum sarapan':
            self.declare(Fact(next_meal='sarapan'))
        if t == 'selepas sarapan':
            self.declare(Fact(next_meal='makan tengah hari'))
        if t == 'selepas makan tengah hari':
            self.declare(Fact(next_meal='makan malam'))
        if t == 'selepas makan malam':
            self.declare(Fact(next_meal='sarapan'))
        self.declare(Action('recommended meal'))

    # This rule will fetch recommended meals for user's next meal 
    # Reference for meal recommendation:
    # Kementerian Kesihatan Malaysia . Portal Rasmi Kementerian Kesihatan Malaysia. (n.d.). https://moh.gov.my/index.php/pages/view/1905  
    @Rule(Action('recommended meal'),
          Fact(next_meal=MATCH.nm))
    def recommended_meal(self, nm):
        print('next meal: ', nm)
        if nm == 'sarapan':
            file_path = 'breakfast'
            total_lines = sum(1 for line in open(file_path))
            random_line_number = random.randint(1, total_lines)
            random_line = linecache.getline(file_path, random_line_number).strip()
            print("Recommended meal for next meal:", random_line)
            self.meal_recommendation.append("(Sarapan): " + random_line)
        if nm == 'makan tengah hari':
            file_path = 'lunch'
            total_lines = sum(1 for line in open(file_path))
            random_line_number = random.randint(1, total_lines)
            random_line = linecache.getline(file_path, random_line_number).strip()
            print("Recommended meal for next meal:", random_line)
            self.meal_recommendation.append("(Makan tengah hari): " + random_line)
        if nm == 'makan malam':
            file_path = 'dinner'
            total_lines = sum(1 for line in open(file_path))
            random_line_number = random.randint(1, total_lines)
            random_line = linecache.getline(file_path, random_line_number).strip()
            print("Recommended meal for next meal:", random_line)
            self.meal_recommendation.append("(Makan malam): " + random_line)
        self.declare(Action('give reasons'))

    # This rule append all advices and outputs from Rules before, to be used in UI implementation
    @Rule(Action('give reasons'),
          Advice(MATCH.reason))
    def give_reasons(self, reason):
        self.reasoning.append(reason)
        print(reason)
    #     self.declare(Action('clear list'))

    # @Rule(Action('clear list'))
    # def clear_list(self):
    #     self.my_list.clear()
    #     self.serving_type_list.clear()
    #     self.bgl_reading.clear()
    #     self.kkm_checker.clear()
    #     self.meal_recommendation.clear()
    #     self.reasoning.clear()
    #     self.missing_meal.clear()

engine = DMES()
engine.reset()

# print(engine.agenda)
engine.run()
# #
# print("-----KB-----")
# print(engine.facts)
# print()
# print("-----Reasoning-----")
# print(engine.reasoning)
