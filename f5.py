import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

# تعیین اندازه پنجره
root.geometry("400x200")

# تعریف تابع برای به‌روزرسانی زمان
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# نمایش زمان
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()