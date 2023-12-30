import random
import string

def parolaOlusturma(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola = "".join(random.choice(karakterler) for i in range(uzunluk))
    return parola

# Parola uzunluğunu belirleyebilirsiniz! (varsayılan: 12)
parolaUzunlugu = 16
parolaOlusturma = parolaOlusturma(parolaUzunlugu)

print(f"Oluşturulan Parola: {parolaOlusturma}")
