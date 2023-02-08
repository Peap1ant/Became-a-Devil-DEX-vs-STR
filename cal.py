# ------ Import modules ------

import tkinter
import tkinter.font


# ------ Window option ------

# def window

win = tkinter.Tk()

# window title name

win.title('덱스 힘 비교기')

# window geometry

win.geometry('600x350+0+0')
win.resizable(False, False)

# font
font = tkinter.font.Font(family="Arial", size=10)

# title
title_text = tkinter.Label(win, text='덱 힘 비교기')
title_text.pack(side='top')

# maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=500, y=30)


# ------ Some labels, entry box ------

# description

description_label = tkinter.Label(win, text='스탯 입력')
description_label.place(x=150, y=30)

# min_atk
min_label = tkinter.Label(win, text='최소 대미지')
min_label.place(x=50, y=50)

min_entry = tkinter.Entry(win, width=20)
min_entry.place(x=150, y=51)

# max_atk

max_label = tkinter.Label(win, text='최대 공격력')
max_label.place(x=50, y=70)

max_entry = tkinter.Entry(win, width=20)
max_entry.place(x=150, y=71)

# atk

atk_label = tkinter.Label(win, text='공격력')
atk_label.place(x=50, y=90)

atk_entry = tkinter.Entry(win, width=20)
atk_entry.place(x=150, y=91)


# atk %

atk_mul_label = tkinter.Label(win, text='공격력 %')
atk_mul_label.place(x=50, y=110)

atk_mul_entry = tkinter.Entry(win, width=20)
atk_mul_entry.place(x=150, y=111)

# crit

crit_label = tkinter.Label(win, text='치명타 공격력 %')
crit_label.place(x=50, y=130)

crit_entry = tkinter.Entry(win, width=20)
crit_entry.place(x=150, y=131)

# stren

stren_label = tkinter.Label(win, text='STR')
stren_label.place(x=50, y=150)

stren_entry = tkinter.Entry(win, width=20)
stren_entry.place(x=150, y=151)

# str %

str_mul_label = tkinter.Label(win, text='STR %')
str_mul_label.place(x=50, y=170)

str_mul_entry = tkinter.Entry(win, width=20)
str_mul_entry.place(x=150, y=171)

# dex

dex_label = tkinter.Label(win, text='DEX')
dex_label.place(x=50, y=190)

dex_entry = tkinter.Entry(win, width=20)
dex_entry.place(x=150, y=191)

# dex %

dex_mul_label = tkinter.Label(win, text='DEX %')
dex_mul_label.place(x=50, y=210)

dex_mul_entry = tkinter.Entry(win, width=20)
dex_mul_entry.place(x=150, y=211)

# elemental

ele_label = tkinter.Label(win, text='속성 공격력')
ele_label.place(x=50, y=230)

ele_entry = tkinter.Entry(win, width=20)
ele_entry.place(x=150, y=231)

# stren increase

stren_inc_label = tkinter.Label(win, text='STR 증가치')
stren_inc_label.place(x=50, y=250)

stren_inc_entry = tkinter.Entry(win, width=20)
stren_inc_entry.place(x=150, y=251)

# str % increase

str_mul_inc_label = tkinter.Label(win, text='STR % 증가치')
str_mul_inc_label.place(x=50, y=270)

str_mul_inc_entry = tkinter.Entry(win, width=20)
str_mul_inc_entry.place(x=150, y=271)

# dex increase

dex_inc_label = tkinter.Label(win, text='DEX 증가치')
dex_inc_label.place(x=50, y=290)

dex_inc_entry = tkinter.Entry(win, width=20)
dex_inc_entry.place(x=150, y=291)

# dex % increase

dex_mul_inc_label = tkinter.Label(win, text='DEX % 증가치')
dex_mul_inc_label.place(x=50, y=310)

dex_mul_inc_entry = tkinter.Entry(win, width=20)
dex_mul_inc_entry.place(x=150, y=311)

# ------ Some funtions for fin_dmg ------


class cal():

    def __init__(self) -> float:

        self.fin_dmg = 0
        self.atk = 0

        # for destroy labels

        self.use_counter = 0

        # for error label

        self.error_zero_label = tkinter.Label(
            win, text='공격력과 치명타 공격력 %은 0이 될 수 없습니다!')
        self.error_none_label = tkinter.Label(win, text='빈칸은 존재 할 수 없습니다!')

    def cal_fin_dmg(self):

        if self.use_counter == 1:
            self.fin_dmg_label.destroy()
            self.fin_dmg_str_label.destroy()
            self.fin_dmg_str_enff_label.destroy()
            self.fin_dmg_str_mul_label.destroy()
            self.fin_dmg_str_mul_enff_label.destroy()
            self.fin_dmg_dex_label.destroy()
            self.fin_dmg_dex_enff_label.destroy()
            self.fin_dmg_dex_mul_label.destroy()
            self.fin_dmg_dex_mul_enff_label.destroy()
        
        elif self.use_counter == 2:
            self.error_zero_label.destroy()

        elif self.use_counter == 3:
            self.error_none_label.destroy()

        else:
            pass

        # get some entry

        self.min_atk = min_entry.get()
        self.max_atk = max_entry.get()
        self.atk = atk_entry.get()
        self.atk_mul = atk_mul_entry.get()
        self.crit = crit_entry.get()
        self.stren = stren_entry.get()
        self.str_mul = str_mul_entry.get()
        self.dex = dex_entry.get()
        self.dex_mul = dex_mul_entry.get()
        self.ele = ele_entry.get()
        self.stren_inc = stren_inc_entry.get()
        self.str_mul_inc = str_mul_inc_entry.get()
        self.dex_inc = dex_inc_entry.get()
        self.dex_mul_inc = dex_mul_inc_entry.get()

        # error message

        if self.min_atk == '' or self.max_atk == '' or self.atk == '' or self.atk_mul == '' or self.crit == '' or self.stren == '' or self.str_mul == '' or self.dex == '' or self.dex_mul == '' or self.ele == '' or self.stren_inc == '' or self.str_mul_inc == '' or self.dex_inc == '' or self.dex_mul_inc == '':
            self.error_none_label = tkinter.Label(win, text='빈칸은 존재 할 수 없습니다!')
            self.error_none_label.place(x=300, y=250)

            self.use_counter = 3

        # convert str to float

        self.min_atk = float(self.min_atk)
        self.max_atk = float(self.max_atk)
        self.atk = float(self.atk)
        self.atk_mul = float(self.atk_mul)
        self.crit = float(self.crit)
        self.stren = float(self.stren)
        self.str_mul = float(self.str_mul)
        self.dex = float(self.dex)
        self.dex_mul = float(self.dex_mul)
        self.ele = float(self.ele)
        self.stren_inc = float(self.stren_inc)
        self.str_mul_inc = float(self.str_mul_inc)
        self.dex_inc = float(self.dex_inc)
        self.dex_mul_inc = float(self.dex_mul_inc)

        # calculate final atk

        self.fin_atk = (((self.min_atk + self.max_atk) / 2) + self.atk)

        # some calculate for errors

        self.atk_mul += 100
        self.str_mul += 100
        self.dex_mul += 100

        # final dmg calculate

        self.fin_dmg = ((self.ele + self.fin_atk + (self.stren * 5) * (self.str_mul / 100)) * (self.atk_mul + (
            (0.1 * self.dex) * (self.dex_mul / 100)) / 100) * (self.crit + ((0.15 * self.dex) * (self.dex_mul / 100)))) / 10000

        self.fin_dmg = round(self.fin_dmg, 1)

        self.fin_dmg_label = tkinter.Label(
            win, text=f'미적용 최종 대미지 : {self.fin_dmg:,}')
        self.fin_dmg_label.place(x=300, y=50)

        # str dmg calculate

        self.fin_dmg_str = ((self.ele + self.fin_atk + ((self.stren + self.stren_inc) * 5) * (self.str_mul / 100)) * (self.atk_mul + (
            (0.1 * self.dex) * (self.dex_mul / 100)) / 100) * (self.crit + ((0.15 * self.dex) * (self.dex_mul / 100)))) / 10000

        self.fin_dmg_str = round(self.fin_dmg_str, 1)

        self.fin_dmg_str_label = tkinter.Label(
            win, text=f'STR 적용 최종 대미지 : {self.fin_dmg_str:,}')
        self.fin_dmg_str_label.place(x=300, y=70)

        # error message

        if self.crit == 0 or self.fin_atk == 0:
            self.error_zero_label = tkinter.Label(
                win, text='공격력과 치명타 공격력 %은 0이 될 수 없습니다!')
            self.error_zero_label.place(x=300, y=230)
            self.fin_dmg_label.destroy()
            self.fin_dmg_str_label.destroy()

            self.use_counter = 2

        self.fin_dmg_str_enff = (self.fin_dmg_str / self.fin_dmg) * 100

        self.fin_dmg_str_enff = round(self.fin_dmg_str_enff, 1)

        self.fin_dmg_str_enff_label = tkinter.Label(
            win, text=f'STR 적용 최종 대미지 효율 % : {self.fin_dmg_str_enff:,} %')
        self.fin_dmg_str_enff_label.place(x=300, y=90)

        # str % dmg calculate

        self.fin_dmg_str_mul = ((self.ele + self.fin_atk + (self.stren * 5) * ((self.str_mul + self.str_mul_inc) / 100)) * (
            self.atk_mul + ((0.1 * self.dex) * (self.dex_mul / 100)) / 100) * (self.crit + ((0.15 * self.dex) * (self.dex_mul / 100)))) / 10000

        self.fin_dmg_str_mul = round(self.fin_dmg_str_mul, 1)

        self.fin_dmg_str_mul_label = tkinter.Label(
            win, text=f'STR % 적용 최종 대미지 : {self.fin_dmg_str_mul:,}')
        self.fin_dmg_str_mul_label.place(x=300, y=110)

        self.fin_dmg_str_mul_enff = (self.fin_dmg_str_mul / self.fin_dmg) * 100

        self.fin_dmg_str_mul_enff = round(self.fin_dmg_str_mul_enff, 1)

        self.fin_dmg_str_mul_enff_label = tkinter.Label(
            win, text=f'STR % 적용 최종 대미지 효율 % : {self.fin_dmg_str_mul_enff:,} %')
        self.fin_dmg_str_mul_enff_label.place(x=300, y=130)

        # dex dmg calculate

        self.fin_dmg_dex = ((self.ele + self.fin_atk + (self.stren * 5) * (self.str_mul / 100)) * (self.atk_mul + ((0.1 * (self.dex + self.dex_inc))
                            * (self.dex_mul / 100)) / 100) * (self.crit + ((0.15 * (self.dex + self.dex_inc)) * (self.dex_mul / 100)))) / 10000

        self.fin_dmg_dex = round(self.fin_dmg_dex, 1)

        self.fin_dmg_dex_label = tkinter.Label(
            win, text=f'DEX 적용 최종 대미지 : {self.fin_dmg_dex:,}')
        self.fin_dmg_dex_label.place(x=300, y=150)

        self.fin_dmg_dex_enff = (self.fin_dmg_dex / self.fin_dmg) * 100

        self.fin_dmg_dex_enff = round(self.fin_dmg_dex_enff, 1)

        self.fin_dmg_dex_enff_label = tkinter.Label(
            win, text=f'DEX 적용 최종 대미지 효율 % : {self.fin_dmg_dex_enff:,} %')
        self.fin_dmg_dex_enff_label.place(x=300, y=170)

        # dex % dmg calculate

        self.fin_dmg_dex_mul = ((self.ele + self.fin_atk + (self.stren * 5) * (self.str_mul / 100)) * (self.atk_mul + ((0.1 * self.dex) * (
            (self.dex_mul + self.dex_mul_inc) / 100)) / 100) * (self.crit + ((0.15 * self.dex) * ((self.dex_mul + self.dex_mul_inc) / 100)))) / 10000

        self.fin_dmg_dex_mul = round(self.fin_dmg_dex_mul, 1)

        self.fin_dmg_dex_mul_label = tkinter.Label(
            win, text=f'DEX % 적용 최종 대미지 : {self.fin_dmg_dex_mul:,}')
        self.fin_dmg_dex_mul_label.place(x=300, y=190)

        self.fin_dmg_dex_mul_enff = (self.fin_dmg_dex_mul / self.fin_dmg) * 100

        self.fin_dmg_dex_mul_enff = round(self.fin_dmg_dex_mul_enff, 1)

        self.fin_dmg_dex_mul_enff_label = tkinter.Label(
            win, text=f'DEX % 적용 최종 대미지 효율 % : {self.fin_dmg_dex_mul_enff:,} %')
        self.fin_dmg_dex_mul_enff_label.place(x=300, y=210)

        self.use_counter = 1


c = cal()


# ------ Button ------

# button
btn = tkinter.Button(text='계산하기', width=10, command=c.cal_fin_dmg)
btn.place(x=500, y=320)


# ------ Open Window ------

win.mainloop()


# ------ Code end ------
