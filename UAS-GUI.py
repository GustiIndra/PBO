import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo 

window = tk.Tk()
window.configure(bg="red")
window.geometry("250x250")
window.resizable(False, False)
window.title("CLASS GARDEN GUI") 

NAMA_TUMBUHAN = tk.StringVar()
JUMLAH_PUPUK = tk.StringVar()
JUMLAH_AIR = tk.StringVar()
SUHU = tk.StringVar()


input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=12,pady=12,fill="x",expand=True)

#  GUI
## Tumbuhan
# 1. Name_Tumbuhan
nama_depan_label = ttk.Label(input_frame,text="Nama Tumbuhan: ")
nama_depan_label.pack(padx=12,fill="x",expand=True)

# 2. Tumbuhan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_TUMBUHAN)
nama_depan_entry.pack(padx=12,fill="x",expand=True)

## Jumlah Pupuk
# 1. Jumlah Pupuk
nama_belakang_label = ttk.Label(input_frame,text="Jumlah Pupuk: ")
nama_belakang_label.pack(padx=12,fill="x",expand=True)

# 2. PUPUK
nama_belakang_entry = ttk.Entry(input_frame,textvariable=JUMLAH_PUPUK)
nama_belakang_entry.pack(padx=12,fill="x",expand=True)

## AIR
# 1. Jumlah Air
nama_belakang_label = ttk.Label(input_frame,text="Jumlah Air: ")
nama_belakang_label.pack(padx=12,fill="x",expand=True)

# 2. Jumlah_Air
nama_belakang_entry = ttk.Entry(input_frame,textvariable=JUMLAH_AIR)
nama_belakang_entry.pack(padx=12,fill="x",expand=True)

#Suhu
# 1. Suhu
nama_belakang_label = ttk.Label(input_frame,text="Suhu yang diperlukan: ")
nama_belakang_label.pack(padx=12,fill="x",expand=True)

# 2. Suhu
nama_belakang_entry = ttk.Entry(input_frame,textvariable=SUHU)
nama_belakang_entry.pack(padx=12,fill="x",expand=True)



## Tombol
def tombol_click():
   
   #Fungsinya akan dipanggil oleh tombol di bawah!
    pesan = f"GARDEN-GST {NAMA_TUMBUHAN.get()} {JUMLAH_PUPUK.get()} {JUMLAH_AIR.get()} {SUHU.get()}!"
    
    showinfo(title="HASIL",message=pesan)

tombol= ttk.Button(input_frame,text="Print Out",command=tombol_click)
tombol.pack(fill='x',expand=True,padx=12,pady=12)


window.mainloop()