class Mahasiswa:
    def __init__ (self, nama, nim, prodi, angkatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan

    def mengambil(self, mataKuliah):
        print(self.nama + ' mengambil ', mataKuliah.nama_mk )
        mataKuliah.nama_mk 
        
class Matkul:
    def __init__(self, nama_mk, kode_mk, sks):
        self.nama_mk = nama_mk
        self.kode_mk = kode_mk
        self.sks = sks

    def diambil(self, mahasiswa):
        print(self.nama_mk + ' diambil oleh ' + mahasiswa.nama)

class Dosen:
    def __init__(self, nama, NIP, prodi):
        self.nama = nama
        self.NIP = NIP
        self.prodi = prodi

    def mengajar(self, matakuliah):
        print(self.nama + ' mengajar ' + matakuliah.nama_mk)


mahasiswa = Mahasiswa('taufik', 2215061064, 'TI', 1998)
mahasiswa2 = Mahasiswa('nabil', 2215061064, 'TI', 1990)

matakuliah = Matkul('AI', 16335453, 3)
matakuliah2 = Matkul('PBO', 16335453, 4)

dosen2 = Dosen('bibi', 1015061003, "TI")
dosen1 = Dosen('yaa ha', 1115061053, "TI")

mahasiswa.mengambil(matakuliah)
mahasiswa.mengambil(matakuliah2)
mahasiswa2.mengambil(matakuliah)
mahasiswa2.mengambil(matakuliah2)
print('\n')

dosen1.mengajar(matakuliah)
dosen2.mengajar(matakuliah2)
print('\n')

matakuliah.diambil(mahasiswa)
matakuliah.diambil(mahasiswa2)
matakuliah.diambil(dosen1)
matakuliah.diambil(dosen2)
print('\n')

matakuliah2.diambil(mahasiswa)
matakuliah2.diambil(mahasiswa2)
matakuliah2.diambil(dosen1)
matakuliah2.diambil(dosen2)