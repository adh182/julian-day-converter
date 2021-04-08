#PROGRAM KONVERSI JULIAN DAY KE MASEHI DAN MASEHI KE JULIAN DAY

from tkinter import *
import tkinter.ttk as ttk 
from tkinter.font import Font
from JDMasehiConverter import JDKeMasehi, MasehiKeJD
from tkinter.ttk import Combobox

class Window:

	def __init__(self, master):
		self.master = master
		self.init_window()

	def init_window(self):
		'''Memanggil semua fungsi agar dapat ditampilkan di main window'''

		self.master.title(" JD Masehi Konverter")
		self.fontstyle = Font(family='Times New Roman', size=10)
		self.fontstyle2 = ('Times New Roman', 10, 'bold')
		self.menus()
		self.title()
		self.convert_from_jd()
		self.convert_from_masehi()
		self.result()
		self.convert_button()

	def menus(self):
		'''Membuat menu'''

		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label='Exit', command=self.exit_window)
		file.add_command(label='Delete', command=self.delete)

		show = Menu(menu)
		show.add_command(label='Show Credit', command=self.show_credit)
		show.add_command(label='Hide Credit', command=self.hide_credit)

		menu.add_cascade(label='File', menu=file)
		menu.add_cascade(label='Show', menu=show)

	def exit_window(self):
		'''Keluar dari window/aplikasi'''

		exit()

	def show_credit(self):
		'''Menampilkan credit pada bagian bawah window'''

		self.lbl_version = Label(text='Version 1.2', font=self.fontstyle, fg='gray')
		self.lbl_credit = Label(text='Created by Adh : i_alimurrijal@student.ub.ac.id', font=self.fontstyle, fg='gray')
		self.lbl_version.place(x=120, y=265)
		self.lbl_credit.place(x=20, y=280)

	def hide_credit(self):
		'''Menyembuyikan credit pada bagian bawah window setelah dipanggil menggunakn show_credit()'''

		self.lbl_credit.place_forget()
		self.lbl_version.place_forget()

	def delete(self):
		'''Menghapus text pada label dan entry'''

		self.ent_jd.delete('0', 'end')
		self.ent_tahun.delete('0', 'end')
		self.ent_bulan.delete('0', 'end')
		self.ent_tanggal.delete('0', 'end')
		self.lbl_hasil.configure(text='-')

	def title(self):
		'''Membuat judul program/aplikasi -- diletakkan di bagian atas window'''

		title = Label(text="PROGRAM KONVERSI JD <=> MASEHI", font=self.fontstyle2, fg='dark green')
		title.pack()

	def convert_from_jd(self):
		'''Membuat radiobutton Julian Day dan Masehi serta label konversi dari Julian Day'''

		lbl_convert_from = Label(text='Konversi dari : ', font=self.fontstyle2)
		lbl_convert_from.place(x=40, y=20)

		self.RadioValue = IntVar()
		self.RadioValue.set(0)
		self.rdb_jd = Radiobutton(text='Julian Day', variable=self.RadioValue, value=0)
		self.rdb_masehi = Radiobutton(text='Masehi', variable=self.RadioValue, value=1)
		self.rdb_jd.place(x=45, y=40)
		self.rdb_masehi.place(x=45, y=85)

		entry_input_jd = StringVar()
		self.ent_jd = Entry(text=entry_input_jd, font=self.fontstyle, bg='lightgreen', width=30, justify='center')
		self.ent_jd.place(x=70, y=65)

	def convert_from_masehi(self):
		'''Membuat label konversi dari masehi, entry untuk tahun, tanggal dan bulan'''

		lbl_tahun = Label(text="Tahun", font=self.fontstyle)
		lbl_bulan = Label(text='Bulan', font=self.fontstyle)
		lbl_tanggal = Label(text='Tanggal', font=self.fontstyle)
		lbl_tahun.place(x=70, y=105)
		lbl_bulan.place(x=70, y=130)
		lbl_tanggal.place(x=70, y=155)

		input_tahun = StringVar()
		input_bulan = StringVar()
		input_tanggal = StringVar()
		self.ent_tahun = Entry(text=input_tahun, font=self.fontstyle, bg='lightgreen', width=15, justify='center')
		self.ent_bulan = Entry(text=input_bulan, font=self.fontstyle, bg='lightgreen', width=15, justify='center')
		self.ent_tanggal = Entry(text=input_tanggal, font=self.fontstyle, bg='lightgreen', width=15, justify='center')

		self.ent_tahun.place(x=130, y=105)
		self.ent_bulan.place(x=130, y=130)
		self.ent_tanggal.place(x=130, y=155)

	def result(self):
		'''Membuat label hasil'''

		lbl_show_hasil = Label(text='Hasil konversi : ', font=self.fontstyle2)
		lbl_show_hasil.place(x=40, y=180)

		self.lbl_hasil = Label(text='-', font=self.fontstyle2, bg='lightgreen', width=25, justify='center')
		self.lbl_hasil.place(x=70, y=200)

	def convert_button(self):
		'''Membuat button / tombol konversi'''

		style = ttk.Style()
		style.configure('TButton', font=self.fontstyle2, bg='dark green', width=10)
		btn_convert = ttk.Button(text='Konversi', style='TButton', command=self.konversi)
		btn_convert.place(x=200, y=240)

	def konversi(self):
		'''Mengkonversi Julian Day ke Masehi dan sebaliknya sesuai dengan value Radiobutotn yang ditunjukkan.
		Menggunakan modul JDMasehiConverter yang telah dibuat sebelumnya'''

		try:
			if self.RadioValue.get() == 0:
				julian_day = float(self.ent_jd.get())
				result = JDKeMasehi(julian_day)
				self.lbl_hasil.configure(text=result.konversi_ke_masehi())

			elif self.RadioValue.get() == 1:
				tahun = int(self.ent_tahun.get())
				bulan = int(self.ent_bulan.get())
				tanggal = int(self.ent_tanggal.get())

				result = MasehiKeJD(tahun, bulan, tanggal)
				self.lbl_hasil.configure(text=result.konversi_ke_JD())
			else:
				None

		except ValueError:
			return None


root = Tk()
app = Window(root)
root.geometry('300x300')
root.resizable(0,0)
icon_photo = PhotoImage(file='calendar_icon.png')
root.iconphoto(False, icon_photo)
root.mainloop()