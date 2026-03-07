 # NAMA  : Kenzo Juan Winata
# KELAS : IXB
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]
print(f"Data nilai asli: " {nilai_ujian})
nilai_tertinggi_ke_rendah = sorted(nilai_ujian, reverse=True)
print(f"Data setelah diurutkan (Descending): " {nilai_tertinggi_ke_rendah})
tiga_nilai_tertinggi = nilai_tertinggi_ke_rendah[:3]
print(f"Tiga nilai tertinggi (Penerima Beasiswa): {tiga_nilai_tertinggi}")
nilai_untuk_lulus = [nilai for nilai in nilai_tertinggi_ke_rendah if nilai > 60]
print(f"Daftar nilai yang lulus: "{nilai_untuk_lulus})