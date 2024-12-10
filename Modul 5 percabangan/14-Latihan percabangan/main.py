# meminta input tatal belanja dari pengguna
total_belanja = float(input("masukan total belanja anda(dalam ribu):"))

#percabangan untuk menentukan hadiah
if total_belanja > 500000:
   hadiah = "anda mendapatkan mouse dan keybord"
else:
   hadiah = "anda mendapatkan gantungan kunci"

# menampilakan hasil
print(hadiah)