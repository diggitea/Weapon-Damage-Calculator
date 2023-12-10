from tkinter import *
import random
import csv


class Gui:
    def __init__(self, window):
        self.weapon_list: list = []
        with open('weapons.csv', 'r') as csvfile:
            content = csv.reader(csvfile, delimiter=',')

            for line in content:
                self.weapon_list.append(line)
        self.window = window
        self.stats_frame = Frame(self.window)
        self.strength_label = Label(self.stats_frame, text='STR modifier:')
        self.strength_entry = Entry(self.stats_frame, width=2)
        self.dexterity_label = Label(self.stats_frame, text='DEX modifier:')
        self.dexterity_entry = Entry(self.stats_frame, width=2)
        self.level_label = Label(self.stats_frame, text='Character level:')
        self.level_entry = Entry(self.stats_frame, width=2)
        self.weapon_frame = Frame(self.window)
        self.weapon_label = Label(self.weapon_frame, text='Weapon:')
        self.weapon_listbox = Listbox(self.weapon_frame)
        for i in range(1,len(self.weapon_list)):
            self.weapon_listbox.insert(i+1,self.weapon_list[i][0])
        self.choice_button = Button(self.weapon_frame, text='OK', command=self.start)
        self.text_frame = Frame(self.window)
        self.text1 = Label(self.text_frame)
        self.text2 = Label(self.text_frame)
        self.mods_frame = Frame(self.window)
        self.prof_num = IntVar()
        self.prof_button = Checkbutton(self.mods_frame, variable=self.prof_num, onvalue=1, offvalue=0)
        self.ability_label = Label(self.mods_frame)
        self.ability_num = IntVar()
        self.str_button = Radiobutton(self.mods_frame, variable=self.ability_num, value=1)
        self.dex_button = Radiobutton(self.mods_frame, variable=self.ability_num, value=2)
        self.roll_button = Button(self.mods_frame, text='ROLL', command=self.roll)
        self.message = Label(self.window, text='Welcome!')
        self.result = Label(self.window)

        self.strength_label.pack(side='left')
        self.strength_entry.pack(side='left')
        self.dexterity_label.pack(side='left')
        self.dexterity_entry.pack(side='left')
        self.level_label.pack(side='left')
        self.level_entry.pack(side='left')
        self.stats_frame.pack()
        self.weapon_label.pack()
        self.weapon_listbox.pack()
        self.choice_button.pack()
        self.weapon_frame.pack()
        self.message.pack()

    def start(self):
        try:
            weapon_choice: int = self.weapon_listbox.curselection()[0] + 1
            try:
                strength: int = int(self.strength_entry.get().strip())
                dexterity: int = int(self.dexterity_entry.get().strip())
                level: int = int(self.level_entry.get().strip())
                self.text1.config(text=f'The {self.weapon_list[weapon_choice][0]} is a {self.weapon_list[weapon_choice][1]} {self.weapon_list[weapon_choice][5]} weapon that does {self.weapon_list[weapon_choice][2]} {self.weapon_list[weapon_choice][3]} damage and weighs {self.weapon_list[weapon_choice][4]} pounds.')
                self.text2.config(text=f'Properties: {self.weapon_list[weapon_choice][6]}, {self.weapon_list[weapon_choice][7]}, {self.weapon_list[weapon_choice][8]}, {self.weapon_list[weapon_choice][9]}'.rstrip(', '))
                self.prof_button.config(text=f'Proficiency (+{(2+((level-1)//4))})')
                self.str_button.config(text=f'STR (+{strength})')
                self.dex_button.config(text=f'DEX (+{dexterity})')
                if 'finesse' in self.weapon_list[weapon_choice][6:9]:
                    self.ability_label.config(text=f'You may choose between STR and DEX:')
                    self.str_button.config(state=NORMAL)
                    self.dex_button.config(state=NORMAL)
                    self.str_button.deselect()
                    self.dex_button.deselect()

                else:
                    if self.weapon_list[weapon_choice][5] == 'Melee':
                        self.ability_label.config(text=f'This weapon uses STR:')
                        self.dex_button.config(state=DISABLED)
                        self.str_button.config(state=NORMAL)
                        self.str_button.select()
                    else:
                        self.ability_label.config(text=f'This weapon uses DEX:')
                        self.str_button.config(state=DISABLED)
                        self.dex_button.config(state=NORMAL)
                        self.dex_button.select()




                self.text1.pack()
                self.text2.pack(side='left')
                self.text_frame.pack()
                self.prof_button.pack()
                self.ability_label.pack()
                self.str_button.pack()
                self.dex_button.pack()
                self.roll_button.pack()
                self.mods_frame.pack()

            except:
                self.message.config(text='Please enter correct STR, DEX and LVL values.')

        except:
            self.message.config(text='Please choose a weapon.')




    def roll(self):
        try:
            weapon_choice: int = self.weapon_listbox.curselection()[0] + 1
            proficiency: int = 0
            ability: int = 0
            if self.prof_num.get() == 1:
                proficiency = (2+((int(self.level_entry.get().strip())-1)//4))
            if self.ability_num.get() == 1:
                ability = int(self.strength_entry.get().strip())
            else:
                ability = int(self.dexterity_entry.get().strip())

            dice_list: list = self.weapon_list[weapon_choice][2].split('d')
            dice_quant: int = int(dice_list[0])
            dice_type: int = int(dice_list[1])
            dice_total: int = 0
            for i in range(dice_quant):
                dice_total += random.randint(1, dice_type)
            total: int = dice_total + proficiency + ability
            self.result.config(text=f'Your {self.weapon_list[weapon_choice][0]} did {dice_total}({self.weapon_list[weapon_choice][2]}) + {proficiency} + {ability} = {total} damage.')
            self.result.pack()

        except:
            self.message.config(text='Please enter correct STR, DEX and LVL values.')



