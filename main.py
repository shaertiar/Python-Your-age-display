import tkinter as tk
import time

# Возвраст
year = 2000
month = 12
day = 11

# Функция обновления возвраста
def update_age():
    age = str(round(60.7 - (time.time() / 31468812.4296 + 1970 - (year + (month + day/30.436)/12)), 10))
    # age = str(round(time.time() / 31468812.4296 + 1970 - (year + (month + day/30.436)/12), 10))

    zeroes = '0' * (10 - len(age.split('.')[1])) if len(age.split('.')[1]) < 10 else ''
    
    text['text'] = age + zeroes

    root.after(10, update_age)

# Создание кона
root = tk.Tk()
root.title('Your age')
root.attributes('-fullscreen', True)

# Создание текста
text = tk.Label(root, text='', font='a 100')

# Размещение элементов 
tk.Label(root, text='', font='Times 100').pack(expand=True)
tk.Label(root, text='Тебе осталось', font='a 50').pack(expand=True)
# tk.Label(root, text='Твой возвраст', font='a 50').pack(expand=True)
text.pack(expand=True)
tk.Label(root, text='', font='Times 300').pack(expand=True)

# Запуск отчета времени
update_age()

# Запуск приложения
root.mainloop()