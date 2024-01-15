import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class Application(tk.Tk):
    def __init__(self):
        self.city_codes = [
            ('01', 'القاهرة', 'Cairo'),
            ('02', 'الإسكندرية', 'Alexandria'),
            ('03', 'بورسعيد', 'Port Said'),
            ('04', 'السويس', 'Suez'),
            (11, 'دمياط', 'Damietta'),
            (12, 'الدقهلية', 'Dakahlia'),
            (13, 'الشرقية', 'Sharqia'),
            (14, 'القليوبية', 'Qalyubia'),
            (15, 'كفر الشيخ', 'Kafr el-Sheikh'),
            (16, 'الغربية', 'Gharbia'),
            (17, 'المنوفية', 'Monufia'),
            (18, 'البحيرة', 'Beheira'),
            (19, 'الإسماعيلية', 'Ismailia'),
            (21, 'الجيزة', 'Giza'),
            (22, 'بني سويف', 'Beni Suef'),
            (23, 'الفيوم', 'Fayyum'),
            (24, 'المنيا', 'Minya'),
            (25, 'أسيوط', 'Asyut'),
            (26, 'سوهاج', 'Sohag'),
            (27, 'قنا', 'Qena'),
            (28, 'أسوان', 'Aswan'),
            (29, 'الأقصر', 'Luxor'),
            (31, 'البحر الأحمر', 'Red Sea'),
            (32, 'الوادى الجديد', 'New Valley'),
            (33, 'مطروح', 'Matrouh'),
            (34, 'شمال سيناء', 'North Sinai'),
            (35, 'جنوب سيناء', 'South Sinai'),
            (88, 'خارج الجمهورية', 'Outside Republic')
        ]
        self.id_guess = []
        self.generation = 0


        super().__init__()
        # Title and geometry
        self.title("ID Details")
        self.geometry("400x600")

        # ID Check Label
        id_check_label = ttk.Label(self, text="ID Check")
        id_check_label.grid(column=0, row=0, padx=10, pady=10, sticky="w"  )
        id_check_label = ttk.Label(self, text="ID Guess")
        id_check_label.grid(column=1, row=2, padx=10, pady=10, sticky="w")

        # ID Check Entry
        self.id_check_entry = ttk.Entry(self)
        self.id_check_entry.grid(column=0, row=1, padx=10, pady=10, sticky="w")
        #------------------------------
        # Buttons
        convert_button1 = ttk.Button(self, text="Convert!", command=self.call_both_functions)
        convert_button1.grid(column=1, row=1, padx=5, pady=5, sticky="N")

        # Buttons
        convert_button = ttk.Button(self, text="Convert!", command=self.call_3_fuc)
        convert_button.grid(column=1, row=11, padx=10, pady=10, sticky="w")

        exit_button = ttk.Button(self, text="Exit!", command=self.destroy)
        exit_button.grid(column=1, row=12, padx=10, pady=10, sticky="w")
        # ------------------------------

        # Separator
        separator = ttk.Separator(self, orient="horizontal")
        separator.grid(column=0, row=2, padx=15, pady=15, sticky="ew")

        #------------------------------------------------test
        # birthday Label
        birthday_label = ttk.Label(self, text="birthday like :👇️ ↗　20050210 ")
        birthday_label.grid(column=0, row=3, padx=10, pady=10, sticky="w")
        self.birthday_entry = ttk.Entry(self)
        self.birthday_entry.grid(column=0, row=5, padx=10, pady=10, sticky="w")
        #-----------------------------------------------



        # gender Label
        gender_label = ttk.Label(self, text="gender")
        gender_label.grid(column=0, row=7, padx=10, pady=10, sticky="w")
        # gender Combobox
        self.gender_combobox = ttk.Combobox(self)
        self.gender_combobox.grid(column=0, row=8, padx=10, pady=10, sticky="w")
        self.gender_combobox["values"] = ("Male","Female")

        #-----------------------------------------
        # Separator
        separator = ttk.Separator(self, orient="horizontal")
        separator.grid(column=0, row=12, padx=12, pady=10, sticky="ew")

        # -----------------------------------------


        # City Label
        city_label = ttk.Label(self, text="City")
        city_label.grid(column=0, row=9, padx=14, pady=10, sticky="w")


        # City Combobox
        self.city_combobox = ttk.Combobox(self)
        self.city_combobox.grid(column=0, row=10, padx=10, pady=10, sticky="w")
        # Create a list of formatted strings containing both English name and number
        city_codes = [
            ('01', 'القاهرة', 'Cairo'),
            ('02', 'الإسكندرية', 'Alexandria'),
            ('03', 'بورسعيد', 'Port Said'),
            ('04', 'السويس', 'Suez'),
            (11, 'دمياط', 'Damietta'),
            (12, 'الدقهلية', 'Dakahlia'),
            (13, 'الشرقية', 'Sharqia'),
            (14, 'القليوبية', 'Qalyubia'),
            (15, 'كفر الشيخ', 'Kafr el-Sheikh'),
            (16, 'الغربية', 'Gharbia'),
            (17, 'المنوفية', 'Monufia'),
            (18, 'البحيرة', 'Beheira'),
            (19, 'الإسماعيلية', 'Ismailia'),
            (21, 'الجيزة', 'Giza'),
            (22, 'بني سويف', 'Beni Suef'),
            (23, 'الفيوم', 'Fayyum'),
            (24, 'المنيا', 'Minya'),
            (25, 'أسيوط', 'Asyut'),
            (26, 'سوهاج', 'Sohag'),
            (27, 'قنا', 'Qena'),
            (28, 'أسوان', 'Aswan'),
            (29, 'الأقصر', 'Luxor'),
            (31, 'البحر الأحمر', 'Red Sea'),
            (32, 'الوادى الجديد', 'New Valley'),
            (33, 'مطروح', 'Matrouh'),
            (34, 'شمال سيناء', 'North Sinai'),
            (35, 'جنوب سيناء', 'South Sinai'),
            (88, 'خارج الجمهورية', 'Outside Republic')
        ]
        city_names_and_numbers = [f"{english_name} ({code})" for code, _, english_name in city_codes]
        # city_names_and_numbers = [f"{english_name} ({number})" for _, _, english_name in self.city_codes1]
        self.city_combobox["values"] = city_names_and_numbers
        self.city_combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

    def on_combobox_select(self, event):
        # Get the selected city from the combobox
        selected_city = self.city_combobox.get()

        # Find the corresponding city code in the city_codes list
        for code, _, english_name in self.city_codes:
            if f"{english_name} ({code})" == selected_city:
                # Perform actions based on the selected city
                print(f"Selected city code: {code}")
                self.id_guess.insert(7, code)
                break

    # -----------------------------------------




    def convert(self):



        print("Convert clicked!")
    def find_Year_birth(self):

        old = 0
        new = 0

        input_value = self.id_check_entry.get()
        num_str = str(input_value)
        if len(num_str) < 14:
            tkinter.messagebox.showinfo('Here is your ID', "Invalid ID format. Please enter a valid 14-digit ID.")
            return
        first_digit = int(num_str[0])

        if first_digit == 2:
            print("You belong to the 1900 generation.")
            old += 19
            self.generation += 1900
        elif first_digit == 3:
            print("You belong to the 2000 generation.")
            new += 20
            self.generation+=2000
        else:
            print("Invalid ID format or generation not recognized.")

        # year
        num_str1 = str(input_value)

        two_digits = num_str1[1:3]
        if first_digit == 2:
            year1=(print(f"The year you belong to is:{old}{two_digits}"))

        elif first_digit == 3:
            year1=(print(f"The year you belong to is:{new}{two_digits}"))

        # month
        num_str2 = str(input_value)
        two_digits1 = num_str2[3:5]
        self.month1=(print("\nThe month you belong to is:", two_digits1))


        # day
        num_str3 = str(input_value)
        two_digits2 = num_str3[5:7]
        print("The day you belong to is:", two_digits2)

        if first_digit == 2:
            print(f"your birthday is :{old}{two_digits}\{two_digits1}\{two_digits2}  ")


        elif first_digit == 3:

            print(f"your birthday is :{new}{two_digits}\{two_digits1}\{two_digits2}  ")




    def find_place_you_in(self):
        self.city_codes = [
            ('01', 'القاهرة', 'Cairo'),
            ('02', 'الإسكندرية', 'Alexandria'),
            ('03', 'بورسعيد', 'Port Said'),
            ('04', 'السويس', 'Suez'),
            (11, 'دمياط', 'Damietta'),
            (12, 'الدقهلية', 'Dakahlia'),
            (13, 'الشرقية', 'Sharqia'),
            (14, 'القليوبية', 'Qalyubia'),
            (15, 'كفر الشيخ', 'Kafr el-Sheikh'),
            (16, 'الغربية', 'Gharbia'),
            (17, 'المنوفية', 'Monufia'),
            (18, 'البحيرة', 'Beheira'),
            (19, 'الإسماعيلية', 'Ismailia'),
            (21, 'الجيزة', 'Giza'),
            (22, 'بني سويف', 'Beni Suef'),
            (23, 'الفيوم', 'Fayyum'),
            (24, 'المنيا', 'Minya'),
            (25, 'أسيوط', 'Asyut'),
            (26, 'سوهاج', 'Sohag'),
            (27, 'قنا', 'Qena'),
            (28, 'أسوان', 'Aswan'),
            (29, 'الأقصر', 'Luxor'),
            (31, 'البحر الأحمر', 'Red Sea'),
            (32, 'الوادى الجديد', 'New Valley'),
            (33, 'مطروح', 'Matrouh'),
            (34, 'شمال سيناء', 'North Sinai'),
            (35, 'جنوب سيناء', 'South Sinai'),
            (88, 'خارج الجمهورية', 'Outside Republic')
        ]
        input_value = self.id_check_entry.get()
        prefix = (str(input_value)[7:9])

        for code, arabic_name, english_name in self.city_codes:
            if prefix == code:
                print(f"The location associated with ID prefix {prefix} is: {english_name} -- {arabic_name} ")
                return

        print(f"No location found for ID prefix {prefix}")
    def find_male_female(self):
        input_value = self.id_check_entry.get()
        num_str3 = str(input_value)
        person = int(num_str3[11:13])
        # person = str(input_value)[11:13]
        if person % 2 == 0:
            print("you are female")
        else:
            print("you are male")
    def call_both_functions(self):
        self.convert()
        self.find_Year_birth()
        self.find_place_you_in()
        self.find_male_female()







    #------------------------------------ the ID Guess

    def find_Year_birth_guess(self):

        input_value1 = self.birthday_entry.get()

        num_str1 =str(input_value1)
        if len(num_str1) < 8:
            print('Here is your ID',"Invalid ID format. Please enter a valid 8-digit ID.")
            return
        first_digit1 = int(num_str1[0])

        if first_digit1 == 1:  # 1900 --> 2
            print("You belong to the 1900 generation.")
            self.id_guess.insert(0, 2)
        elif first_digit1 == 2:  # 2000 --> 3
            print("You belong to the 2000 generation.")
            self.id_guess.insert(0, 3)
        else:
            print("Invalid ID format or generation not recognized.")
        # year

        two_digits = int(num_str1[2:4])  # (05)
        self.id_guess.insert(1, "{:02}".format(two_digits))

        #3050210  01  063  9  6
        #20050210

        # month
        two_digits1 = int(num_str1[4:6]) #(02 , 11 )
        self.id_guess.insert(2, "{:02}".format(two_digits1))

        # day
        two_digits2 = int(num_str1[6:8]) #(02 ~ 12)
        self.id_guess.insert(3, "{:02}".format(two_digits2))




        #-----------------------------------


        # the goverment numbers

        x=163
        self.id_guess.insert(8, x)



    def gender_select(self):
        selected_gender = self.gender_combobox.get()

        if "Male" in selected_gender:
            # Add the found code to id_guess

            self.id_guess.insert(12, 9)  # Assuming the position where the code should be inserted
        elif "Female" in selected_gender:
            self.id_guess.insert(12, 8)


        y = 6
        self.id_guess.append( y)

        concatenated_number = int("".join(map(str, self.id_guess)))
        print(concatenated_number)
        tkinter.messagebox.showinfo('Here is your ID', str(concatenated_number))
        self.id_guess.clear()

    def get_selected_value(self):
        selected_value = self.city_combobox.get()
        print("Selected Value:", selected_value)


    def call_3_fuc(self):
        self.convert()
        self.find_Year_birth_guess()
        self.gender_select()
        print("         ^^^ ^    \t this is goverment code i cant guess them")
        print("**the 163 and the 6 in the end is just guess beacause its goverment code ,cant guess it sorry ")
        print("thank you :)")




app =Application()
app.mainloop()
