import tkinter as tk
from tkinter import ttk
from GapScanner import getGaps
import pandas as pd
import threading
import time




window = tk.Tk()
window.geometry('480x500')
window.resizable(False, False)
window.title("Gap Scanner")
main_frame = tk.Frame(window)
main_frame.pack(fill="both", expand=1)

my_canvas = tk.Canvas(main_frame, bg="black")
my_canvas.pack(side="left", fill="both", expand=1)





loading = True
csv = pd.DataFrame()

l = tk.Label(window, text="This may take about 1 minute.", font=('Arial', 16), background="#000000", fg="#FFFFFF")
l.place(relx=0.5, rely=0.5, anchor="center")
def load():
    while (loading):
        l.configure(text="This may take about 1 minute")
        time.sleep(1)
        window.update()
        l.configure(text="This may take about 1 minute.")
        time.sleep(1)
        window.update()
        l.configure(text="This may take about 1 minute..")
        time.sleep(1)
        window.update()
        l.configure(text="This may take about 1 minute...")
        time.sleep(1)
        window.update()



def doProcess():
    global csv
    global loading
    csv = getGaps()
    loading = False

t1 = threading.Thread(target=doProcess)
t1.start()


load()


t1.join()

l.destroy()
my_scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
my_scrollbar.pack(side="right", fill="y")

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = tk.Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")
style= ttk.Style()
style.theme_use('clam')
style.configure("TEntry", fieldbackground='#000000', foreground='#FFFFFF')
# print(csv)
for i in range(0, csv.shape[0]):
    e = ttk.Entry(second_frame, font=('Arial', 16), style="TEntry")
    e.grid(row=i, column=0)
    
    e.insert("end", csv["Ticker"][i])
    e.config(state='readonly')
    e = ttk.Entry(second_frame, font=('Arial', 16), style="TEntry")
    e.grid(row=i, column=1)
    
    e.insert("end", csv["Gap"][i])
    e.config(state='readonly')




window.mainloop()