# Percabanngan
# Struktur
"""
   1. if -nya
   2. punya kondisi
   3. punya aksi
"""
nama = input (" masukan nama : ")

# percabangan yang inline
if nama == "alqa" : print ("selamat datang")
print("terima kasih")

# Percabangan indentasi
if nama == "alqa" :
    print ("selamat datang")
    print ("selamat belajar python")
print ("bukan bagian percabangan")

# Percabangan 1 kondisi 2 aksi 
# Pakai kata kunci 'else'

if nama == "alqa" :\
    print("selamat datang")
else:
    print( f' anda {nama}, bukan alqa' )
print("terima kasih")
