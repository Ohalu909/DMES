from experta import *
# from collections.abc import Counter
import random
import linecache
from database import Database


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


class DMES(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.my_list = []
        self.serving_type_list = []
        self.bgl_reading = []
        self.kkm_checker = []
        self.meal_recommendation = []
        self.reasoning = []

    @DefFacts()
    def kb_facts(self):
        yield Fact(action="greet")

        yield Menu(menu='q', menu_class='q')
        yield Menu(menu='roti', menu_class='karbohidrat')
        yield Menu(menu='nasi putih', menu_class='karbohidrat')
        yield Menu(menu='nasi', menu_class='karbohidrat')
        yield Menu(menu='nasi tomato', menu_class='karbohidrat')
        yield Menu(menu='nasi goreng', menu_class='karbohidrat')
        yield Menu(menu='roti canai', menu_class='karbohidrat')
        yield Menu(menu='bihun goreng', menu_class='karbohidrat')
        yield Menu(menu='bihun sup', menu_class='karbohidrat')
        yield Menu(menu='bihun kuah', menu_class='karbohidrat')
        yield Menu(menu='mi goreng', menu_class='karbohidrat')
        yield Menu(menu='maggi goreng', menu_class='karbohidrat')
        yield Menu(menu='nasi lemak', menu_class='karbohidrat')
        yield Menu(menu='kuey tiaw goreng', menu_class='karbohidrat')
        yield Menu(menu='kuey tiaw sup siam', menu_class='karbohidrat')
        yield Menu(menu='karipap', menu_class='karbohidrat')
        yield Menu(menu='cucur', menu_class='karbohidrat')
        yield Menu(menu='sandwic', menu_class='karbohidrat')
        yield Menu(menu='nasi minyak', menu_class='karbohidrat')
        yield Menu(menu='nasi hujan panas', menu_class='karbohidrat')
        yield Menu(menu='mi bandung', menu_class='karbohidrat')
        yield Menu(menu='mi kuah', menu_class='karbohidrat')
        yield Menu(menu='mi kari', menu_class='karbohidrat')
        yield Menu(menu='nasi ayam', menu_class='karbohidrat')
        yield Menu(menu='laksa', menu_class='karbohidrat')
        yield Menu(menu='laksa goreng', menu_class='karbohidrat')
        yield Menu(menu='capati', menu_class='karbohidrat')

        yield Menu(menu='sup ayam', menu_class='protein')
        yield Menu(menu='ketam masak lemak', menu_class='protein')
        yield Menu(menu='ikan rebus serai', menu_class='protein')
        yield Menu(menu='ikan stim', menu_class='protein')
        yield Menu(menu='ikan goreng', menu_class='protein')
        yield Menu(menu='ikan bakar', menu_class='protein')
        yield Menu(menu='gulai ikan', menu_class='protein')
        yield Menu(menu='ikan masak masam manis', menu_class='protein')
        yield Menu(menu='gulai ayam', menu_class='protein')
        yield Menu(menu='ayam masak kicap', menu_class='protein')
        yield Menu(menu='daging masak kicap', menu_class='protein')
        yield Menu(menu='gulai daging', menu_class='protein')
        yield Menu(menu='tomyam ayam', menu_class='protein')
        yield Menu(menu='sup tauhu dan telur', menu_class='protein')
        yield Menu(menu='ayam goreng', menu_class='protein')
        yield Menu(menu='ayam bakar', menu_class='protein')
        yield Menu(menu='sup daging', menu_class='protein')
        yield Menu(menu='sup tulang ', menu_class='protein')
        yield Menu(menu='ayam masak lemak', menu_class='protein')
        yield Menu(menu='ayam kamheong', menu_class='protein')
        yield Menu(menu='ayam paprik', menu_class='protein')
        yield Menu(menu='ayam masak merah', menu_class='protein')
        yield Menu(menu='telur goreng', menu_class='protein')
        yield Menu(menu='telur dadar', menu_class='protein')
        yield Menu(menu='gulai telur', menu_class='protein')
        yield Menu(menu='sup telur', menu_class='protein')
        yield Menu(menu='daging bakar', menu_class='protein')
        yield Menu(menu='daging paprik', menu_class='protein')
        yield Menu(menu='daging masak pedas', menu_class='protein')
        yield Menu(menu='ikan masak kicap', menu_class='protein')
        yield Menu(menu='ayam masak sambal', menu_class='protein')
        yield Menu(menu='ikan masak sambal', menu_class='protein')
        yield Menu(menu='daging masak lada', menu_class='protein')
        yield Menu(menu='ikan bakar', menu_class='protein')

        yield Menu(menu='tomyam', menu_class='serat')
        yield Menu(menu='nenas', menu_class='serat')
        yield Menu(menu='mangga', menu_class='serat')
        yield Menu(menu='ulam', menu_class='serat')
        yield Menu(menu='kangkung goreng', menu_class='serat')
        yield Menu(menu='sayur bayam', menu_class='serat')
        yield Menu(menu='bayam goreng', menu_class='serat')
        yield Menu(menu='sayur kangkung', menu_class='serat')
        yield Menu(menu='sayur campur', menu_class='serat')
        yield Menu(menu='kerabu mangga', menu_class='serat')
        yield Menu(menu='kerabu taugeh', menu_class='serat')
        yield Menu(menu='kerabu tauge', menu_class='serat')
        yield Menu(menu='kacang goreng', menu_class='serat')
        yield Menu(menu='kacang buncis goreng', menu_class='serat')
        yield Menu(menu='sawi goreng', menu_class='serat')
        yield Menu(menu='kailan ikan masin', menu_class='serat')
        yield Menu(menu='buah naga', menu_class='serat')
        yield Menu(menu='oren', menu_class='serat')
        yield Menu(menu='tembikai', menu_class='serat')
        yield Menu(menu='epal', menu_class='serat')
        yield Menu(menu='anggur', menu_class='serat')
        yield Menu(menu='kobis goreng', menu_class='serat')
        yield Menu(menu='kerabu kacang botor', menu_class='serat')
        yield Menu(menu='sayur bayam dengan betik', menu_class='serat')
        yield Menu(menu='sayur manis', menu_class='serat')
        yield Menu(menu='betik', menu_class='serat')
        yield Menu(menu='jambu', menu_class='serat')
        yield Menu(menu='sayur goreng', menu_class='serat')
        yield Menu(menu='masak lemak labu', menu_class='serat')
        yield Menu(menu='sayur petola', menu_class='serat')

        yield Menu(menu='air kosong', menu_class='minuman tanpa gula')
        yield Menu(menu='teh o suam tanpa gula', menu_class='minuman tanpa gula')
        yield Menu(menu='teh o ais', menu_class='minuman bergula')
        yield Menu(menu='teh ais', menu_class='minuman bergula')
        yield Menu(menu='ais blended', menu_class='minuman bergula')
        yield Menu(menu='jus oren', menu_class='minuman bergula')
        yield Menu(menu='air sirap', menu_class='minuman bergula')
        yield Menu(menu='ais oren', menu_class='minuman bergula')
        yield Menu(menu='jus tembikai', menu_class='minuman bergula')
        yield Menu(menu='ais sarsi', menu_class='minuman bergula')
        yield Menu(menu='teh o limau ais', menu_class='minuman bergula')
        yield Menu(menu='milo ais', menu_class='minuman bergula')

    @Rule(Fact(action='greet'))
    def ask_reading_type(self):

        db = Database()

        last_reading_type = db.get_last_entry("reading_type")
        last_bgl_reading = float(db.get_last_entry("bgl_reading"))
        last_meal_taken = db.get_last_entry("meal_taken")

        self.declare(Fact(type=last_reading_type.lower()))
        self.declare(Fact(reading=last_bgl_reading))
        self.declare(User(meal_taken='q'))
        value_list = last_meal_taken.split(', ')
        for i in value_list:
            self.declare(User(meal_taken=i))
            self.my_list.append(i)

        print('-----Diabetic Monitoring Expert System-----')

    @Rule(Fact(reading=MATCH.reading))
    def process_action(self, reading):
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

    @Rule(AS.f1 << Action('check_serving_type'),
          AS.f2 << User(meal_taken=MATCH.mta),
          Menu(menu=MATCH.mta,
               menu_class=MATCH.mc))
    def serving_type(self, mc):
        print('serving type = ', mc)
        if mc == 'q':
            self.declare(Action('count_serving_type'))
        else:
            self.serving_type_list.append(mc)

    @Rule(Action('count_serving_type'))
    def count_serving_type(self):
        print("-------------------------------")
        # counter = Counter(self.serving_type_list)
        print("Serving type occurrence counts:")
        # for serving_type, count in counter.items():
        #     print(f"{serving_type}: {count}")
        count_dict = {}

        for item in self.serving_type_list:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        for item, count in count_dict.items():
            print(f'{item}: {count}')
        self.declare(Action('check_kkm_recommendation'))

    @Rule(Action('check_kkm_recommendation'))
    def check_kkm_recommendation(self):
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat']

        # counter_list1 = Counter(kkm_recommendation)
        # counter_list2 = Counter(self.serving_type_list)

        counter_list1 = len(kkm_recommendation)
        counter_list2 = len(self.serving_type_list)

        print("-------------------------------\nKKM recommendation checker:")

        if counter_list1 == counter_list2:
            print('satisfy kkm recommendation')
            self.declare(Action('satisfy'))
            self.kkm_checker.append('mengikut cadangan pemakanan KKM')
        else:
            print('dissatisfy kkm recommendation')
            self.declare(Action('dissatisfy'))
            self.kkm_checker.append('tidak mengikut cadangan pemakanan KKM')

    @Rule(Action('satisfy'),
          Fact(reading_type=MATCH.rt))
    def satisfy_recommendation(self, rt):
        if rt == 'rendah':
            self.declare(Advice('saiz hidangan kecil'))
            self.declare(Advice('tambahkan saiz hidangan'))
        if rt == 'tinggi':
            self.declare(Advice('saiz hidangan besar'))
            self.declare(Advice('kurangkan saiz hidangan'))
        if rt == 'normal':
            self.declare(Advice('saiz hidangan normal'))
            self.declare(Advice('saiz hidangan memuaskan'))

    @Rule(Action('dissatisfy'),
          Fact(reading_type=MATCH.rt))
    def dissatisfy_recommendation(self, rt):
        if rt == 'rendah':
            self.declare(Advice('tidak cukup hidangan'))
        if rt == 'tinggi':
            self.declare(Advice('terlebih hidangan'))
        if rt == 'normal':
            self.declare(Advice('hidangan yang diambil memuaskan'))
        self.declare(Action('check serving count'))

    @Rule(Action('check serving count'))
    def check_serving_count(self):
        print('-----------------------------------------')
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat', 'minuman tanpa gula']

        # counter_list1 = Counter(kkm_recommendation)
        # counter_list2 = Counter(self.serving_type_list)

        counter_list1 = {}
        counter_list2 = {}

        for item in kkm_recommendation:
            if item in counter_list1:
                counter_list1[item] += 1
            else:
                counter_list1[item] = 1

        for item in self.serving_type_list:
            if item in counter_list2:
                counter_list2[item] += 1
            else:
                counter_list2[item] = 1

        for item, count2 in counter_list2.items():
            count1 = counter_list1[item]
            if count2 < count1:
                count3 = count1 - count2
                self.declare(Advice(f"{'tambahkan hidangan ber'}{item}{' sebanyak '}{count3}{' hidangan.'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
            elif count2 > count1:
                count3 = count2 - count1
                self.declare(Advice(f"{'kurangkan hidangan ber'}{item}{' sebanyak '}{count3}{' hidangan.'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
            else:
                self.declare(Advice(f"{item}{' mengikut pecahan hidangan'}"))
                print(f"Item {item}: List1={count1}, List2={count2}")
        self.declare(Action('check_unavailable_serving'))

    @Rule(Action('check_unavailable_serving'))
    def check_unavailable_serving(self):
        kkm_recommendation = ['karbohidrat', 'protein', 'serat', 'serat']

        missing_items = [item for item in kkm_recommendation if item not in self.serving_type_list]
        print('kkm-recs: ', kkm_recommendation)
        print('serving taken: ', self.serving_type_list)
        print('missing items: ', missing_items)
        for i in list(missing_items):
            if i == 'karbohidrat':
                self.declare(Advice('tambah 1 hidangan karbohidrat'))
            elif i == 'protein':
                self.declare(Advice('tambah 1 hidangan protein'))
            elif i == 'serat':
                self.declare(Advice('tambah 2 hidangan serat'))
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

    @Rule(Action('give reasons'),
          Advice(MATCH.reason))
    def give_reasons(self, reason):
        self.reasoning.append(reason)
        print(reason)

# engine = DMES()
# engine.reset()
#
# # print(engine.agenda)
# engine.run()
# #
# print("-----KB-----")
# print(engine.facts)
# print()
# print("-----Reasoning-----")
# print(engine.reasoning)
