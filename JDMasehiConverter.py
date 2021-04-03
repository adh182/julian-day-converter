#MODULE KONVERSI JULIAN DAY KE MASEHI DAN MASEHI KE JULIAN DAY
#ISLAMUDDIN ALIMURRJAL (185090300111018)

import numpy as np

class JDKeMasehi:
	'''
	KONSVERSI JD KE MASEHI
	Parameter:
	JD = julian day
	Keluaran :
		tanggal = tanggal hasil konversi 
		bulan = bulan hasil konversi
		tahun = tahun hasil konversi
		waktu = berupa jam, menit, detik
	'''

	def __init__(self, JD):
		self.JD = JD
		self.tahun = 0
		self.bulan = 0
		self.tanggal = 0

	def hitung_variabel(self):
		JD1 = self.JD + 0.5
		Z = int(JD1)
		F = JD1 - Z

		if Z == 229916:
			A = Z
		else:
			AA = int((Z - 1867216.25)/36524.25)
			A = Z + 1 + AA - int(AA/4)

		B = A + 1524
		C = int((B - 122.1)/365.25)
		D = int(365.25*C)
		E = int((B-D)/30.6001)

		return B, C, D, E, F

	def hitung_waktu(self, waktu):
		'''Menghitung waktu berupa jam, menit dan detik'''
		jam = int(waktu*24)
		menit = int(((waktu*24) - jam)*60)
		detik = int(((((waktu*24) - jam)*60)-menit)*60)

		return int(jam), int(menit), int(detik)

	def konversi_ke_masehi(self):
		'''Mengkonversi JD ke Masehi'''


		B, C, D, E, F = self.hitung_variabel()

		self.tanggal = B - D - int(30.6001*E)

		if E == 14 or E == 15:
			self.bulan = E - 13

		elif E < 14:
			self.bulan = E - 1

		if self.bulan == 1 or self.bulan == 2:
			self.tahun = C - 4715
		elif self.bulan > 2:
			self.tahun = C-4716

		jam, menit, detik = self.hitung_waktu(F)

		hasil = "{}/{}/{}   {}:{}:{}".format(self.tahun, self.bulan, self.tanggal, jam, menit, detik)

		return hasil


class MasehiKeJD:
	'''
	KONSVERSI MASEHI KE JULIAN DAY
	Parameter:
	tahun = tahun yang ingin dikonversi
	bulan = bulan yang ingin dikonversi
	tanggal = tanggal yang ingin dikonversi
	Keluaran :
		julian_day = julian day
	'''

	def __init__(self, tahun, bulan, tanggal):
		self.tahun = tahun
		self.bulan = bulan
		self.tanggal = tanggal
		self.Gregorian = True

	def isGregorian(self):
		''' 
		Menentukan apakah tanggal yang diinput merupakan kalender Gregorian
		atau bukan (kalender Julian)
		'''

		if self.tanggal < 15:
			if self.bulan < 10:
				if self.tahun <= 1582:
					self.Gregorian == False
				else:
					self.Gregorian == True

		return self.Gregorian

	def hitung_JD(self, Y, M, D):
		'''Menghitung Julian day'''

		if self.isGregorian() == True:
			A = int(Y/100)
			B = 2 + int(A/4) - A

		elif self.isGregorian() == False:
			B = 0

		JD = 1720994.5 + int(365.25*Y) + int(30.6001*(M+1) + B + D)
		return JD

	def isLeap(self):
		kabisat = False
		if self.tahun % 4 == 0:
			if self.tahun % 100 == 0:
				if self.tahun % 400 == 0:
					kabisat = True
				else:
					kabisat = False
			else:
				kabisat = True
		else:
			kabisat = False

		return kabisat 

	def hari_dalam_bulan(self):
		tanggal = []
		if self.bulan in [4, 6, 9, 11]:
			tanggal = np.arange(1,31)
		elif self.bulan == 1:
			tanggal = np.arange(1,32)
		elif self.bulan == 2:
			if self.isLeap():
				tanggal = np.arange(1,30)
			else:
				tanggal = np.arange(1,29)
		elif self.bulan in [3, 5, 7, 8, 10, 12]:
			tanggal = np.arange(1,32)
		else:
			tanggal = [0]

		return tanggal

	def konversi_ke_JD(self):
		'''Mengkonversikan masehi ke Julian Day'''

		if self.tahun >= -4712:

			julian_day = 0

			if self.tahun == 1582 and self.bulan == 10:
				if self.tanggal in np.arange(5,15):
					julian_day = 'Tanggal tidak tersedia'
				else:
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)

			elif self.bulan <= 2:
				hari = self.hari_dalam_bulan()
				if self.tanggal in hari:
					self.bulan = self.bulan + 12
					self.tahun = self.tahun -1
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)
				else:
					julian_day = 'Tanggal tidak tersedia'

			elif self.bulan > 12:
				julian_day = 'Bulan tidak teredia'

			else:
				self.bulan = self.bulan
				self.tahun = self.tahun

				hari = self.hari_dalam_bulan()
				if self.tanggal in hari:
					julian_day = self.hitung_JD(self.tahun, self.bulan, self.tanggal)
				else:
					julian_day = 'Tanggal tidak tersedia'

		else:
			julian_day = 'Tahun tidak tersedia'

		return julian_day