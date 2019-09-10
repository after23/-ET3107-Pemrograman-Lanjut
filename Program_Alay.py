def glosarium(huruf): #fungsi untuk memetakan huruf bisa menjadi versi alaynya
    if (huruf == 'a'): return '@'
    elif (huruf == 'i'): return '1'
    elif (huruf == 'o'): return '0'
    elif (huruf == 's'): return '$'
    elif (huruf == 'e'): return '3'
    else: return huruf

word = input('Enter a word:') 
if len(word) > 0 and word.isalpha(): #mengecek apakah input benar2 huruf
    temp = word.lower() #menkonversi text masukkan ke huruf kecil
    l = len(temp)
    new = '' #list of str kosong untuk menampung kata alay
    for i in range(l):
        if (i == (l - 3) and temp[(l-3):l] == 'nya'): #untuk akhiran -nya akan dijadikan .x
            new = new + '.x'
            break
        elif (i % 2 == 0): #untuk huruf dengan indeks genap akan diubah sesuai fungsi glosarium
            new = new + glosarium(temp[i])
        elif (i % 2 == 1): #untuk huruf dengan indeks ganjil akan dijadikan huruf besar
            new = new + temp[i].upper()
else:
    print('empty')
print(new)