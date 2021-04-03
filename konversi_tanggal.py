from JDMasehiConverter import JDKeMasehi, MasehiKeJD


lahir = MasehiKeJD(2000, 2, 18)
merdeka = MasehiKeJD(1945, 8, 17)
sekarang = MasehiKeJD(2020, 10, 3)
tanggal1 = MasehiKeJD(2012, 11, 13)
tanggal2 = MasehiKeJD(2010, 7, 11)

lama_lahir = sekarang.konversi_ke_JD() - lahir.konversi_ke_JD()
lama_merdeka = sekarang.konversi_ke_JD() - merdeka.konversi_ke_JD()
selisih_hari = tanggal1.konversi_ke_JD() - tanggal2.konversi_ke_JD()

print("Hari yang dilalui sejak lahir : {} hari".format(lama_lahir))
print("Hari yang dilalui sejak merdeka {} hari".format(lama_merdeka))
print("Selisih antara peristiwa : {} hari".format(selisih_hari))

jd1 = JDKeMasehi(2431684.5)
jd2 = JDKeMasehi(2455388.5)
jd3 = JDKeMasehi(2457447.9505)

print("JD 2431684.5 adalah ", jd1.konversi_ke_masehi())
print("JD 2455388.5 adalah ", jd2.konversi_ke_masehi())
print("JD 2457447.9505 adalah ", jd3.konversi_ke_masehi())