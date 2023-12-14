def bagi_angka():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")

    except ValueError:
        print("Error: Masukkan harus berupa angka.")
    except ZeroDivisionError:
        print("Error: Tidak dapat melakukan pembagian oleh nol.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Program selesai.")

if __name__ == "__main__":
    bagi_angka()
