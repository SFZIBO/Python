def operasi_array():
    # Membuat list dengan beberapa nilai
    nilai = [10, 20, 30, 40, 50]

    # Menampilkan nilai dalam list
    print("Nilai dalam list:", nilai)

    # Menambahkan nilai baru ke dalam list
    nilai.append(60)
    print("Setelah menambahkan nilai 60:", nilai)

    # Mengakses nilai dalam list berdasarkan indeks
    indeks = 2
    print(f"Nilai pada indeks {indeks}: {nilai[indeks]}")

    # Mengubah nilai dalam list berdasarkan indeks
    nilai[3] = 45
    print("Setelah mengubah nilai pada indeks 3 menjadi 45:", nilai)

    # Menghitung jumlah elemen dalam list
    jumlah_elemen = len(nilai)
    print("Jumlah elemen dalam list:", jumlah_elemen)

    # Menggunakan loop for untuk iterasi melalui list
    print("Iterasi melalui list:")
    for item in nilai:
        print(item)

if __name__ == "__main__":
    operasi_array()
