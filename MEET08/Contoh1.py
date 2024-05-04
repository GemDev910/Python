umur = int(input("Masukkan umur \t: "))

if umur < 17:
    status = input("Menikah [ Y/T ] : ").upper()
    if status == "Y":
        print("Anda boleh ikut pemilu")
    elif status == "T":
        print("Anda tidak boleh ikut pemilu")
    else:
        print("tolong periksa kembali jawaban anda")
elif umur >= 17:
    print("Anda boleh ikut pemilu")
else:
    print("Jawaban salah")