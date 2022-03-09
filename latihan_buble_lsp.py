def garis():
    print("----------------------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing-masimg elemen ke kanan
            if array[j] > array[j+1]:
                #jika lebih besar, tukar ke kiri
                array [j], array[j+1] = array[j+1], array[j]
    return array

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
    n = len(array) #n itu adalah jumlah baris
    #perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n-i-1):
            #membandingkan masing-masimg elemen ke kanan
            if array[j] < array[j+1]:
                #jika lebih besar, tukar ke kiri
                array [j], array[j+1] = array[j+1], array[j]
    return array

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka) /len(angka)

garis()
#input nama
str(input("Nama Kamu : "))

garis()
#input nilai
print("Masukan Sepuluh Buah Nilai")
nilai_1 = int(input("Nilai 1 : "))
nilai_2 = int(input("NIlai 2 : "))
nilai_3= int(input("Nilai 3 : "))
nilai_4= int(input("Nilai 4 : "))
nilai_5= int(input("Nilai 5 : "))
nilai_6= int(input("Nilai 6 : "))
nilai_7= int(input("Nilai 7 : "))
nilai_8= int(input("Nilai 8 : "))
nilai_9= int(input("Nilai 9 : "))
nilai_10= int(input("Nilai 10 : "))

angka = [nilai_1, nilai_2, nilai_3, nilai_4, nilai_5, nilai_6, nilai_7, nilai_8, nilai_9, nilai_10]
garis()
print()

#nilai akhir
print("Hasil Akhir Kamu :")
print("Urutan Angka Ascending : ",(sort_asc(angka)))
print("Urutan Angka Descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka Terbesar : ", max(angka))

#angka terkecil
print("Angka Terkecil : ", min(angka))

#rata-rata
print("Rata-ratanya : ", round(rata_rata(angka),2))
