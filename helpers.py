screen_helper = """
ScreenManager:
    MenuScreen:
    LoginScreen:
    SignUpScreen:
    IntroScreen1:
    IntroScreen2:
    IntroScreen3:
    MainScreen:
    CarbScreen1:
    CarbScreen2:
    ReadingTypeScreen:
    AskBGLScreen:
    AskMealTakenScreen:
    OutputScreen:
    OutputScreen2:
    OutputScreen3:

<MenuScreen>:
    name: 'menu'
    Image:
        source: 'asset/8.png'  
        size_hint: (0.4, 0.4)  
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}  
    MDLabel: 
        text: 'Diabetes Monitoring Expert System'
        font_style: "H6"
        pos_hint: {'center_x':0.6, 'center_y':0.75}
    MDRaisedButton:
        text: 'Log Masuk'
        size_hint: (0.6, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'Daftar'
        size_hint: (0.6, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press: root.manager.current = 'signup'
    # MDRaisedButton:
    #     text: 'Testing'
    #     size_hint: (0.6, 0.05)
    #     pos_hint: {'center_x':0.5, 'center_y':0.4}
    #     on_press: 
    #         on_text_validate: (app.dmes_logic())
    #         root.manager.current = 'output'
    # MDLabel: 
    #     text: 'Sekiranya anda pesakit diabetes, pastikan anda mempunyai alat cek gula sebelum menggunakan aplikasi ini untuk hasil yang lebih memuaskan.'
    #     # font_style: "H6"
    #     pos_hint: {'center_x':0.6, 'center_y':0.3}
    # MDRaisedButton:
    #     text: "Set theme"
    #     size_hint: (0.6, 0.05)
    #     pos_hint: {'center_x':0.5, 'center_y':0.3}
    #     on_release: app.switch_theme_style()
            
    

<LoginScreen>:
    name: 'login'
    MDLabel: 
        text: 'Log Masuk ke DMES'
        font_style: "H6"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.9}
    MDLabel: 
        text: 'Sila masukkan maklumat akaun anda'
        pos_hint: {'center_x':0.55, 'center_y':0.8}
    MDTextField:
        id: username
        hint_text: "Isi nama pengguna"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: password
        hint_text: "Isi kata laluan"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        password: True
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDCheckbox:
        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint:{'center_x': 0.14, 'center_y': 0.43}
        on_active: app.show_password(*args)
    MDLabel:
        id: password_text
        text: "Tunjuk kata laluan"
        pos_hint:{'center_x': 0.7, 'center_y': 0.43}
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            on_text_validate: (app.login(username, password))
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<SignUpScreen>:
    name: 'signup'
    MDLabel: 
        text: 'Jom cipta akaun DMES anda!'
        pos_hint: {'center_x':0.65, 'center_y':0.8}
    MDTextField:
        id: username
        hint_text: "Cipta nama pengguna"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id: password
        hint_text: "Cipta kata laluan"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            on_text_validate: (app.signup(username, password))
            root.manager.current = 'login'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<IntroScreen1>
    name: 'intro1'
    MDLabel: 
        text: 'Apa itu Diabetes?'
        font_style: "H6"
        pos_hint: {'center_x':0.58, 'center_y':0.85}
        elevation: 10
        color: "grey"
    MDLabel:
        text: "Diabetes adalah penyakit kronik yang berlaku apabila pankreas tidak menghasilkan insulin yang mencukupi atau apabila tubuh tidak dapat menggunakan insulin dengan berkesan."
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "blue"
    MDLabel:
        text: "Insulin merupakan hormon yang mengawal glukosa dalam darah."
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "blue"
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            root.manager.current = 'intro2'
    MDRectangleFlatButton:
        text: 'Skip'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'main'

<IntroScreen2>
    name: 'intro2'
    MDLabel: 
        text: 'Apa itu "Expert System"?'
        font_style: "H6"
        pos_hint: {'center_x':0.58, 'center_y':0.85}
        elevation: 10
        color: "grey"
    MDLabel:
        text: "Sebuah program komputer yang menggunakan teknologi kecerdasan buatan (AI) untuk mensimulasikan penilaian dan perilaku manusia yang memiliki kepakaran dalam suatu bidang tertentu."
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        theme_text_color: "Custom"
        text_color: "blue"
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            root.manager.current = 'intro3'
    MDRectangleFlatButton:
        text: 'Skip'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'main'

<IntroScreen3>
    name: 'intro3'
    MDLabel: 
        text: 'Apa itu DMES?'
        font_style: "H6"
        pos_hint: {'center_x':0.58, 'center_y':0.85}
        elevation: 10
        color: "grey"
    MDLabel:
        text: 'Singkatan untuk "Diabetic Monitoring Expert System"'
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "blue"
    MDLabel:
        text: 'Sebuah "Expert system" untuk pesakit diabetes memantau paras gula dalam darah sambil merancang pemakanan harian'
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "blue"
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            root.manager.current = 'main'

<MainScreen>:
    name: 'main'
    id: main
    MDLabel: 
        text: 'Selamat datang ke DMES ^_^'
        font_style: "H6"
        pos_hint: {'center_x':0.58, 'center_y':0.85}
        elevation: 10
        color: "grey"
    MDCard:
        orientation: 'vertical'
        size_hint: (0.8, 0.2)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        BoxLayout:
            orientation: 'vertical'
            padding: "8dp"
            MDLabel:
                id: data_label
                text: "11.9"  
                font_size: "55sp"
                # size_hint: None, None
                size: self.texture_size
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                color: 128, 128, 128, 1  
            MDLabel:
                text: "mmol/L"  
                font_size: "15sp"
                # size_hint: None, None
                size: self.texture_size
                pos_hint: {"center_x": 0.9, "center_y": 0.8}
                color: 0.5, 0.5, 0.5, 1    
            MDLabel:
                id: data_label_2
                text: "yy:mm/dd"  
                font_size: "15sp"
                # size_hint: None, None
                size: self.texture_size
                pos_hint: {"center_x": 0.9, "center_y": 0.5}
                color: 0.5, 0.5, 0.5, 1  
            MDLabel:
                text: "Paras gula terakhir dimasukkan"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
    MDRaisedButton:
        text: 'Masukkan rekod hari ini'
        size_hint: (0.6, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'reading_type'
    MDRaisedButton:
        text: 'Nasihat sebelum ini'
        size_hint: (0.6, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: 
            on_text_validate: (app.dmes_logic())
            root.manager.current = 'output'
    MDRaisedButton:
        text: 'Pertukaran Karbohidrat'
        size_hint: (0.6, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.manager.current = 'carb_intro'
    MDRectangleFlatButton:
        text: 'Keluar'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<CarbScreen1>
    name: 'carb_intro'
    MDLabel: 
        text: 'Berapa banyak karbohidrat yang anda perlukan?'
        font_style: "H6"
        halign: "center"
        pos_hint: {'center_x':0.58, 'center_y':0.85}
        elevation: 10
        color: "grey"
    MDLabel:
        text: 'Secara umumnya, perempuan memerlukan 3 hingga 4 unit karbohidrat manakala lelaki memerlukan 4 hingga 5 unit karbohidrat untuk setiap hidangan utama dan 1 hingga 2 unit karbohidrat untuk hidangan snek. Keperluan ini bergantung juga kepada tahap aktiviti fizikal anda.'
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        theme_text_color: "Custom"
        text_color: "blue"
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.manager.current = 'carb_exchange'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'main'

<CarbScreen2>:
    name: 'carb_exchange'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        MDLabel:
            text: 'Pertukaran Karbohidrat'
            theme_text_color: "Primary"
            halign: 'center'
            font_style: 'H6'
            size_hint_y: None
            height: dp(56)
        MDLabel:
            text: 'Senarai makanan untuk 1 unit karbohidrat:'
            theme_text_color: "Secondary"
            halign: 'center'
            size_hint_y: None
            height: dp(24)
        ScrollView:
            size_hint: (1, 1)
            GridLayout:
                id: carb_grid
                cols: 4 
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height
        MDRectangleFlatButton:
            text: 'Kembali'
            size_hint_y: None
            height: dp(48)
            pos_hint: {'center_x':0.5, 'center_y':0.4}
            on_press: root.manager.current = 'main'
                     
<ReadingTypeScreen>:
    name: 'reading_type'
    MDProgressBar:
        value: 30
    MDLabel: 
        text: 'Apakah jenis bacaan anda?'
        pos_hint: {'center_x':0.65, 'center_y':0.85}
    MDRaisedButton:
        text: 'Sebelum sarapan'
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        on_press: 
            app.add_reading_type("Sebelum sarapan")
            root.manager.current = 'ask_bgl'
    MDRaisedButton:
        text: 'Selepas sarapan'
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press: 
            app.add_reading_type("Selepas sarapan")
            root.manager.current = 'ask_bgl'
    MDRaisedButton:
        text: 'Selepas makan tengah hari'
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: 
            app.add_reading_type("Selepas makan tengah hari")
            root.manager.current = 'ask_bgl'
    MDRaisedButton:
        text: 'Selepas makan malam'
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: 
            app.add_reading_type("Selepas makan malam")
            root.manager.current = 'ask_bgl'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'main'

<AskBGLScreen>:
    name: 'ask_bgl'
    MDProgressBar:
        value: 60
    MDLabel: 
        text: 'Berapakah bacaan paras gula anda (mmol/L)?'
        pos_hint: {'center_x':0.6, 'center_y':0.8}
    MDTextField:
        id: task_text
        hint_text: "Masukkan bacaan paras gula"
        helper_text: "Diperoleh dari ujian gula dalam darah"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            on_text_validate: (app.add_bgl_reading(task_text))
            root.manager.current = 'ask_meals_taken'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'reading_type'
        
<AskMealTakenScreen>:
    name: 'ask_meals_taken'
    MDProgressBar:
        value: 100
    MDLabel: 
        text: 'Apa yang anda makan?'
        pos_hint: {'center_x':0.6, 'center_y':0.8}
    MDTextField:
        id: task_text
        hint_text: "Masukkan hidangan diambil"
        helper_text: "Contoh: nasi putih, ikan goreng, dll"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            on_text_validate: (app.add_meal_taken(task_text))
            on_text_validate: (app.dmes_logic())
            root.manager.current = 'output'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'ask_bgl'
      
<OutputScreen>:
    name: 'output'
    ScrollView:
        size_hint: (1, None)
        height: self.parent.height  
        MDGridLayout:
            id: output_grid
            cols: 0.6
            spacing: dp(10)
            padding: dp(10)
            height: self.minimum_height
            MDTopAppBar:
                id: toolbar
                title: "Nasihat DMES"
                elevation: 4
                pos_hint: {'top': 1}
            MDLabel: 
                id: result_label0
                text: ""
                # size_hint_y: None  
                pos_hint: {'center_x':0.55, 'center_y':0.95}
            MDLabel: 
                id: result_label1
                text: ""
                pos_hint: {'center_x':0.55, 'center_y':0.9}
            MDLabel: 
                text: "Cadangan pemakanan seterusnya:"
                font_style: "H6"
                theme_text_color: "Secondary"
                pos_hint: {'center_x':0.55, 'center_y':0.6}
            MDLabel: 
                id: result_label2
                text: ""
                size_hint_y: None
                pos_hint: {'center_x':0.55, 'center_y':0.55}
            # MDLabel: 
            #     id: result_label3
            #     text: ""
            #     font_style: "Caption"
            #     size_hint_y: None
            #     pos_hint: {'center_x':0.55, 'center_y':0.2}
            MDRaisedButton:
                text: 'Seterusnya'
                # size_hint_y: None
                pos_hint: {'center_x':0.5, 'center_y':0.1}
                on_press: 
                    # app.update_main_card()
                    root.manager.current = 'output2'  

<OutputScreen2>
    name: 'output2'
    MDTopAppBar:
        id: toolbar
        title: "Nasihat DMES"
        elevation: 4
        pos_hint: {'top': 1}
    MDLabel:
        text: 'Walaupun anda dibenarkan untuk menikmati makanan dan minuman manis dalam diet seharian, anda perlu ingat bahawa pengambilan utama karbohidrat sepatutnya datang daripada sumber buah, sayur, bijirin, susu rendah lemak dan yogurt.'
        halign: "center"
        font_style: "Caption"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "blue"
    MDLabel: 
        id: result_label3
        text: ""
        # font_style: "Caption"
        halign: "center"
        size_hint_y: None
        pos_hint: {'center_x':0.5, 'center_y':0.7}
    MDRaisedButton:
        text: 'Seterusnya'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            root.manager.current = 'output3'
    MDRectangleFlatButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: 
            root.manager.current = 'output'

<OutputScreen3>
    name: 'output3'
    MDTopAppBar:
        id: toolbar
        title: "Nasihat DMES"
        elevation: 4
        pos_hint: {'top': 1}
    MDLabel:
        text: 'Suku,Suku,Separuh oleh KKM juga merupakan sebahagian daripada cara mengatur pengambilan kalori.'
        halign: "center"
        # font_style: "Caption"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "blue"
    MDLabel:
        text: 'Makanan seperti karbohidrat dan protein mengandungi lebih banyak kalori berbanding serat, oleh itu, disarankan untuk mengambil keduanya hanya 1/4 setiap satu dalam sepinggan.'
        halign: "center"
        # font_style: "Caption"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "blue"
    MDRaisedButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: 
            root.manager.current = 'output2'
    MDRectangleFlatButton:
        text: 'Keluar'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: 
            app.update_main_card()
            root.manager.current = 'main'
"""