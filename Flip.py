import numpy as np#memanggil library numpy untuk mengolah array
import imageio#memanggil library imageio untuk mengolah array
import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar

img = imageio.imread("Cat.png")#sebuah fungsi yang membaca file gambar dan mengembalikan sebuah array NumPy yang merepresentasikan gambar tersebut

img_height = img.shape[0] #menetapkan nilai dari tinggi gambar ke dalam variabel img_height
img_width = img.shape[1] #menetapkan nilai dari lebar gambar ke dalam variabel img_width
img_channel = img.shape[2] #menetapkan nilai dari jumlah channel atau saluran warna pada gambar ke dalam variabel img_channel
img_type = img.dtype #menetapkan tipe data (data type) dari elemen pada array gambar ke dalam variabel img_type.

img_flip_horizontal = np.zeros(img.shape, img_type)#membuat sebuah array NumPy kosong dengan dimensi yang sama dengan gambar yang dibaca oleh imageio.imread(), dan tipe data yang sama dengan tipe data dari gambar tersebut.Fungsi np.zeros() dari NumPy digunakan untuk membuat array yang diisi dengan nol
img_flip_vertical = np.zeros(img.shape, img_type) # membuat sebuah array NumPy kosong dengan dimensi yang sama dengan gambar yang dibaca oleh imageio.imread(), dan tipe data yang sama dengan tipe data dari gambar tersebut.

#Membalik gambar secara horizontal
for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1. memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
        for c in range(0, img_channel):#  memulai sebuah perulangan atau loop, di mana variabel c akan mengambil nilai dari 0 hingga img_channel-1, dengan increment sebesar 1.
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]# mengisi setiap piksel pada img_flip_horizontal dengan piksel yang sesuai dari gambar img, yang telah di-flip secara horizontal.

#Membalik gambar secara vertical
for y in range(0, img_height):  # memulai sebuah perulangan atau loop, di mana variabel y akan mengambil nilai dari 0 hingga img_height-1, dengan increment sebesar 1.
    for x in range(0, img_width):  # sebuah perulangan atau loop, di mana variabel x akan mengambil nilai dari 0 hingga img_width-1, dengan increment sebesar 1.
        for c in range(0,img_channel):  #  memulai sebuah perulangan atau loop, di mana variabel c akan mengambil nilai dari 0 hingga img_channel-1, dengan increment sebesar 1.
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]#mengisi setiap piksel pada img_flip_horizontal dengan piksel yang sesuai dari gambar img, yang telah di-flip secara Vertical.

#Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal)#menampilkan gambar
plt.title("Flip Horizontal")#membuat judul pada plot
plt.show()#menampilkan plot
plt.imshow(img_flip_vertical)#menampilkan gambar
plt.title("Flip Vertical")#membuat judul pada plot
plt.show()#menampilkan plot