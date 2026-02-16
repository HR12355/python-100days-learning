from tkinter import *

def miles_to_km():
    """マイルをキロメートルに変換"""
    miles = float(input.get())
    km = miles * 1.609
    result_km_label.config(text=f"{km}") # configは上書き更新する
    # f-stringの方がバグを防ぐ

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)


equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

result_km_label = Label(text=0, font=("Arial", 12, "bold"))
result_km_label.grid(column=1, row=1)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()