import tkinter as tk
from fungsi.fungsi_kehadiran import *
from fungsi.fungsi_gui import *

layar = tk.Tk()
layar.title("Universitas Gadjah Mada")
layar.geometry("640x360")

label1 = tk.Label(layar, text = "Program Presensi Mahasiswa TRI", font=("Hershey_Complex", 20, "bold"), pady=20)

gambar = tk.PhotoImage(file = "logo.png")
label2 = tk.Label(layar, image=gambar)

button1 = tk.Button(layar, text = "Input Foto", font = "Hershey_Complex", padx = 33, pady = 4, command = foto)
button2 = tk.Button(layar, text = "Mulai Presensi", font = "Hershey_Complex",padx = 20, pady = 5, command = SystemAttandance)
button3 = tk.Button(layar, text = "Hapus Foto", font = "Hershey_Complex",padx = 30, pady = 4, command = hapus)

label1.pack()
label2.pack(pady=30)
button1.pack()
button2.pack(pady=5)
button3.pack()
layar.mainloop()
