import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar

img = imageio.imread("Kucing.png")#sebuah fungsi yang membaca file gambar dan mengembalikan sebuah array NumPy yang merepresentasikan gambar tersebut

img_height = img.shape[0] #menetapkan nilai dari tinggi gambar ke dalam variabel img_height
img_width = img.shape[1] #menetapkan nilai dari lebar gambar ke dalam variabel img_width
img_channel = img.shape[2] #menetapkan nilai dari jumlah channel atau saluran warna pada gambar ke dalam variabel img_channel
img_type = img.dtype #menetapkan tipe data (data type) dari elemen pada array gambar ke dalam variabel img_type.

#Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)#membuat sebuah array numpy dengan bentuk (shape) yang sama dengan gambar img, yang berisi semua nilai nol dengan unsigned integer dengan panjang 8 bit

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):#deklarasi fungsi Python yang dinamakan inversi_grayscale. Fungsi ini memiliki satu parameter masukan (input) yang dinamakan nilai.Fungsi ini dirancang untuk melakukan inversikan nilai
    for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = nilai - gray #mengurangi nilai dengan gray
            img_inversi[y][x] = (gray, gray, gray)# mengubah nilai piksel pada gambar img_inversi pada baris y, kolom x, sehingga menjadi gambar kebalikan dari gambar asli yang terdiri dari warna-warna yang diubah menjadi keabuan.

#Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):#mendefinisikan sebuah fungsi Python yang bernama inversi_grayscale dengan satu parameter masukan nilai
    for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            red = nilai - red#mengurangi nilai dengan red
            green = img[y][x][1]# mengambil nilai komponen warna hijau (Green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = nilai - green#mengurangi nilai dengan green
            blue = img[y][x][2]# mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = nilai - blue#mengurangi nilai dengan blue
            img_inversi[y][x] = (red, green, blue)# mengubah nilai piksel pada gambar img_inversi pada baris y, kolom x, sehingga menjadi gambar kebalikan dari gambar asli yang terdiri dari warna-warna yang diubah menjadi RGB.

#Menampilkan hasil inversi
inversi_grayscale(255)#melakukan konversi ke inversi pada variable inversi_grayscale
plt.imshow(img_inversi)#menampilkan gambar
plt.title("Inversi Grayscale")#membuat judul pada plot
plt.show()#menampilkan plot

inversi_rgb(255)#melakukan konversi ke inversi pada variable inversi_rgb
plt.imshow(img_inversi)#menampilkan gambar
plt.title("Inversi RGB")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk log
def log(c):#mendefinisikan sebuah fungsi Python yang bernama log dengan satu parameter masukan c
    for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  #sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = int(c * np.log(gray + 1)) #perhitungan untuk menampilkan data log
            if gray > 255: #mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:#mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_log[y][x] = (gray, gray, gray)# mengubah nilai piksel pada gambar img_inversi pada baris y, kolom x, sehingga menjadi gambar kebalikan dari gambar asli yang terdiri dari warna-warna yang diubah menjadi keabuan.

#Menampilkan hasil log
log(35)#mengatur nilai log
plt.imshow(img_log)#menampilkan gambar
plt.title("Log")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk inversi log
def inlog(c):#mendefinisikan sebuah fungsi Python yang bernama inlog dengan satu parameter masukan c
    for y in range(0, img_height):  #memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  #sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = int(c * np.log(255 - gray + 1))#perhitungan untuk menampilkan data inlog
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_inlog[y][x] = (gray, gray, gray)#menetapkan nilai keabuan yang sama untuk setiap komponen warna (merah, hijau, dan biru) pada piksel yang berada pada baris y, kolom x, pada gambar img_inlog.
#Menampilkan hasil inversi log
inlog(35)#mengatur nilai inlog
plt.imshow(img_inlog)#menampilkan gambar
plt.title("Inversi & Log")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y):#mendefinisikan sebuah fungsi Python yang bernama nthpower dengan satu parameter masukan c dan y
    thc = c / 100#mendefinisikan nilai thc
    thy = y / 100#mendefinisikan nilai thy
    for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambile img_widl nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = int(thc * pow(gray, thy))#perhitungan untuk menampilkan data nthpower
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#menetapkan nilai keabuan yang sama untuk setiap komponen warna (merah, hijau, dan biru) pada piksel yang berada pada baris y, kolom x, pada gambar img_nthpower.

#Menampilkan hasil
nthpower(45, 90)#mengatur nilai nth power
plt.imshow(img_nthpower)#menampilkan gambar
plt.title("Nth Power")#membuat judul pada plot
plt.show()#menampilkan plot

#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):#mendefinisikan sebuah fungsi Python yang bernama nthrootpower dengan satu parameter masukan c dan y
    thc = c / 100#mendefinisikan nilai thc
    thy = y / 100#mendefinisikan nilai thy
    for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
        for x in range(0, img_width):  #sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
            red = img[y][x][0]  #  mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
            gray = int(thc * pow(gray, 1./thy))#perhitungan untuk menampilkan data nthrootpower
            if gray > 255:  # mengatur nilai gray jika 255 maka gambar berubah menjadi gray
                gray = 255
            if gray < 0:  # mengatur nilai gray jika 0 maka gambar berubah menjadi putih
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)# menetapkan nilai keabuan yang sama untuk setiap komponen warna (merah, hijau, dan biru) pada piksel yang berada pada baris y, kolom x, pada gambar img_nthpower.
#Menampilkan hasil
nthrootpower(45, 90)#mengatur nilai nthrootpower
plt.imshow(img_nthrootpower)#menampilkan gambar
plt.title("Nth Root Power")#membuat judul pada plot
plt.show()#menampilkan plot