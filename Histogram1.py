import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt

img = imageio.imread("Kucing.png")#membaca gambar dengan nama sunset.jpg dan menyimpannya ke dalam variable image

img_height = img.shape[0] #menetapkan nilai dari tinggi gambar ke dalam variabel img_height
img_width = img.shape[1] #menetapkan nilai dari lebar gambar ke dalam variabel img_width
img_channel = img.shape[2] #menetapkan nilai dari jumlah channel atau saluran warna pada gambar ke dalam variabel img_channel

img_grayscale = np.zeros(img.shape, dtype=np.uint8)#membuat sebuah array numpy dengan bentuk (shape) yang sama dengan gambar img, yang berisi semua nilai nol dengan unsigned integer dengan panjang 8 bit

for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
        red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        gray = (int(red) + int(green) + int(blue)) / 3  # menghitung nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x, pada gambar img.
        img_grayscale[y][x] = (gray, gray, gray)#mengubah nilai piksel pada gambar img_inversi pada baris y, kolom x, sehingga menjadi gambar kebalikan dari gambar asli yang terdiri dari warna-warna yang diubah menjadi keabuan.

plt.imshow(img_grayscale)#menampilkan gambar
plt.title("Grayscale")#membuat judul pada plot
plt.show()#menampilkan semua plot

#menampilkan histogram gambar grayscale
hg = np.zeros((256))#membuat array numpy satu dimensi baru dengan ukuran (shape) (256,), yang dikenal sebagai histogram
for x in range(0, 256):# menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hg[x] = 0 #mengatur nilai 0 pada elemen x dari array numpy hg.
for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
        gray = img_grayscale[y][x][0]#mengambil nilai keabuan (grayscale) dari piksel yang berada pada baris y, kolom x pada gambar grayscale img_grayscale.
        hg[gray] += 1 #m menambahkan nilai 1 ke elemen gray dari array numpy hg.
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)#membuat array numpy satu dimensi baru dengan ukuran (shape) (100,).
plt.hist(hg, bins, color="black", alpha=0.5)#  membuat histogram menggunakan library matplotlib.pyplot (biasanya diimpor sebagai plt).
plt.title("Histogram")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgr = np.zeros((256))#membuat array numpy satu dimensi baru dengan ukuran (shape) (256)
hgg = np.zeros((256))#membuat array Numpy pada variable hgr dengan ukuran (shape) (256,) yang diisi dengan nilai nol.
hgb = np.zeros((256))#membuat array Numpy pada variable hgb dengan ukuran (shape) (256,) yang diisi dengan nilai nol.
hgrgb = np.zeros((768)) #membuat array Numpy pada variable hgrgb dengan ukuran (shape) (768,) yang diisi dengan nilai nol.

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hg[x] = 0 #mengatur nilai 0 pada elemen x dari array numpy hg.
    hgg[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgg
    hgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgb

for x in range(0, 768):#menjalankan perulangan (loop) untuk variabel x .
    hgrgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgrgb

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hgr[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgr
    hgg[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgg
    hgb[x] = 0  # menginisialisasikan nilai x ke 0 pada variable hgb

for x in range(0, 768):#menjalankan perulangan (loop) untuk variabel x .
    hgrgb[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgrgb

# th = int(256/64)
temp = [0]#menyimpan sementara nilai atau hasil perhitungan dalam pemrosesan data atau algoritma yang lebih kompleks.
for y in range(0, img.shape[0]):# melakukan perulangan (loop) untuk variabel y dengan nilai mulai dari 0 hingga img.shape[0] - 1.
    for x in range(0, img.shape[1]):#melakukan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga img.shape[1] - 1.
        red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        blue = img[y][x][2]  # mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        green = green + 256 #mengatur nilai green dengan menambahkan nilai 256
        blue = blue + 512 #mengatur nilai blue dengan menambahkan nilai 512
        #         temp.append(green)
        hgrgb[red] += 1#menambahkan nilai 1 setiap parameter red pada nilai rata-rata piksel
        hgrgb[green] += 1#menambahkan nilai 1 setiap parameter green pada nilai rata-rata piksel
        hgrgb[blue] += 1#menambahkan nilai 1 setiap parameter blue pada nilai rata-rata piksel

binsrgb = np.linspace(0, 768, 100)# membuat array numpy satu dimensi baru dengan ukuran (shape) (0,768,100,)
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)# membuat histogram menggunakan library matplotlib.pyplot (biasanya diimpor sebagai plt).

# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#membuat judul pada plot
plt.show()#menampilkan semua plot

for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        red = img[y][x][0]  # mengambil nilai komponen warna merah (red) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        green = img[y][x][1]  # mengambil nilai komponen warna hijau (green) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        blue = img[y][x][2]  #mengambil nilai komponen warna biru (blue) pada piksel yang berada pada baris y, kolom x, pada gambar img.
        hgr[red] += 1#menambahkan nilai 1 setiap parameter hgr pada nilai rata-rata piksel
        hgg[green] += 1#menambahkan nilai 1 setiap parameter hgg pada nilai rata-rata piksel
        hgb[blue] += 1#menambahkan nilai 1 setiap parameter hgb pada nilai rata-rata piksel

bins = np.linspace(0, 256, 100)# membuat array numpy yang berisi 100 bilangan yang merata terdistribusi antara 0 dan 256.
plt.hist(hgr, bins, color="red", alpha=0.5)#membuat histogram menggunakan library matplotlib.pyplot
plt.title("Histogram Red")#membuat judul pada plot
plt.show()#menampilkan semua plot

plt.hist(hgg, bins, color="green", alpha=0.5)#membuat histogram menggunakan library matplotlib.pyplot
plt.title("Histogram Green")#membuat judul pada plot
plt.show()#menampilkan semua plot

plt.hist(hgb, bins, color="blue", alpha=0.5)#membuat histogram menggunakan library matplotlib.pyplot (biasanya diimpor sebagai plt).
plt.title("Histogram Blue")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgk = np.zeros((256))#membuat array Numpy pada variable hgk dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
c = np.zeros((256))#membuat array Numpy pada variable c dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hgk[x] = 0 #menginisialisasikan nilai x ke 0 pada variable hgk
    c[x] = 0# menginisialisasikan nilai x ke 0 pada variable c

for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        hgk[gray] += 1# menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel

c[0] = hgk[0]#mengatur nilai c sama dengan hgk
for x in range(1, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    c[x] = c[x - 1] + hgk[x]#rumus dari perulangan dengan menambahkan nilai hgk

hmaxk = c[255]#mengambil nilai yang terdapat pada index ke-255 dari array c dan menyimpannya dalam variabel hmaxk.

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    c[x] = 190 * c[x] / hmaxk#rumus dari perulangan dengan membagi nilai hgk

plt.hist(c, bins, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="hitam") dan transparansi 50% (alpha=0.5) menggunakan data yang dihitung sebelumnya
plt.title("Histogram Grayscale Kumulatif")#membuat judul pada plot
plt.show()#menampilkan semua plot

hgh = np.zeros((256))#membuat array Numpy pada variable hgh dengan elemen yang diinisialisasi ke nilai nol dengan panjang nilai 256
h = np.zeros((256))#membuat array numpy dengan ukuran (shape) (256,) yang berisi nol di setiap elemennya.
c = np.zeros((256))#membuat array numpy dengan ukuran (shape) (256,) yang berisi nol di setiap elemennya.

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hgh[x] = 0#mengatur nilai 0 pada elemen array hgh pada indeks yang sesuai dengan nilai x.
    h[x] = 0#mengatur nilai 0 pada elemen array hgh pada indeks yang sesuai  pada variable h
    c[x] = 0#mengatur nilai 0 pada elemen array hgh pada indeks yang sesuai  pada variable c

for y in range(0, img_height):  # melakukan perulangan pada setiap piksel pada sumbu y untuk variable img_height
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        hgh[gray] += 1 #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel

h[0] = hgh[0] #mengatur nilai h samadengan hgh
for x in range(1, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    h[x] = h[x - 1] + hgh[x]#rumus dari perulangan dengan menambahkan nilai hgh

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    h[x] = h[x] / img_height / img_width#rumus dari perulangan dengan membagi img_height dengan img_widthmembagi nilai pada elemen array h pada indeks yang sesuai dengan nilai x dengan hasil perkalian dari img_height dan img_width.


for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    hgh[x] = 0#menginisialisasikan nilai x ke 0 pada variable hgh

for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
        gray = img_grayscale[y][x][0]  # mengambil nilai piksel gray pada titik (y,x)
        gray = h[gray] * 255#perhitungan mengalikan nilai h dengan 255
        hgh[int(gray)] += 1 #menambahkan 1 pada elemen array hgh pada indeks yang sesuai dengan nilai gray yang dikonversi menjadi integer.

c[0] = hgh[0]#mengassign nilai hgh[0] pada index ke-0 dari array c
for x in range(1, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    c[x] = c[x - 1] + hgh[x]#mengassign nilai pada elemen array c pada indeks yang sesuai dengan nilai x dengan penjumlahan antara nilai pada elemen sebelumnya (c[x - 1]) dan nilai pada array hgh pada indeks yang sama (hgh[x]).


hmaxk = c[255]#mengambil nilai yang terdapat pada index ke-255 dari array c dan menyimpannya dalam variabel hmaxk.

for x in range(0, 256):#menjalankan perulangan (loop) untuk variabel x dengan nilai mulai dari 0 hingga 255 (inklusif).
    c[x] = 190 * c[x] / hmaxk # mengassign nilai pada elemen array c pada indeks yang sesuai dengan nilai x dengan hasil perkalian antara 190, nilai pada elemen c pada indeks tersebut, dan pembagian dengan nilai hmaxk.

plt.hist(c, bins, color="black", alpha=0.5)#untuk menggambar histogram dengan warna hitam (color="hitam") dan transparans
plt.title("Histogram Grayscale Hequalisasi")#membuat judul pada plot
plt.show()#menampilkan semua plot