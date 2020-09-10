''' Программа контроля 
рахода семейного бюджета'''
import tkinter as tk
from tkinter import Menu


lst_dohod = []
lst_rashod = []
value_dohod = int()
value_rashod = int()


def inp_dohod():
	'''тут мы вводим наши доходы'''
	ent = tk.Entry(window, width = 20)
	ent.grid(column = 0, row = 5)
	value_dohod = ent.get()
	window.bind_all('KeyPress-Up',clear)# очищаем поля ввода


def inp_rashod():
	'''тут вводим наши расходы'''
	ent = tk.Entry(window, width = 20)
	ent.grid(column = 0 , row = 3)
	value_rashod = ent.get()
	window.bind_all("<KeyPress-Up>",clear)# очищаем поля ввода	


def clear(event):
	''' функция очистки поля после ввода 
	суммы расхода или дохода'''
	if event.keysym == 'Up':
		ent.delete(0, tk.END)



'''здес у нас графическая часть'''
window = tk.Tk()
window.title('Бюджет семьи')
window.geometry('500x350')
btn_1 = tk.Button(window, text = 'Добавить расходы', command = inp_rashod)
btn_2 = tk.Button(window, text= 'Добавить доходы', command = inp_dohod)
btn_1.grid(column = 0, row = 2)
btn_2.grid(column = 0, row = 4)
#frame_1 = tk.Frame(master = window, width = 150 ,height = 150, bg = 'black')
#frame_1.grid(column = 2, row = 2)
menu = Menu(window)
new_item = Menu(menu, tearoff = 0)
new_item_1 = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'Меню', menu = new_item)
'''Добавляем пункты в Меню'''
new_item.add_command(label = 'Создать новый бюджет')
new_item.add_command(label = 'Сохранить файл')
new_item.add_command(label = 'Открыть файл')
window.config(menu = menu)
menu.add_cascade(label = 'Информация',menu = new_item_1)
'''Добавляем пункты в меню "Информация"'''
new_item_1.add_command(label = 'Состояние расходов за  месяц')
new_item_1.add_command(label = 'Состояние расходов на год')


window.mainloop()



