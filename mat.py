#/usr/bin/python3
# ﺏ , Written by Şefik Efe aka f4T1H21
def faktoriyel(x):
    if x == 0:
        return 1
    else:
        return x * faktoriyel(x-1)

def permutasyon(n,r,tekrarli=0):
    if tekrarli == 1:
        return int(faktoriyel(n) / faktoriyel(r))
    else:
        return int(faktoriyel(n) / faktoriyel(n-r))

def kombinasyon(n,r):
    return int(permutasyon(n,r) / faktoriyel(r))

def fibonacci(t):
    if t <= 1:
        return t
    else:
        return fibonacci(t-1) + fibonacci(t-2)

print("""<!-- Şefik Efe tarafından 2021-2022 eğitim öğretim yılı Matematik proje ödevi olarak klavyeye alınmıştır. -->
Hoş geldiniz, lütfen yapmak istediğiniz işlemi seçiniz:

f <x>     | Faktöriyel hesapla
p <n> <r> | Permütasyon hesapla
t <n> <r> | Tekrarlı permütasyon hesapla
k <n> <r> | Kombinasyon hesapla
i <t>     | t. fibonacci terimini hesapla

ç) Çıkış
""")

while True:
    try:
        giris = input(":>> ")

        if giris.startswith("f"):
            x = int(giris.split(" ")[1])
            print("{}! = {}".format(x, faktoriyel(x)))

        elif giris.startswith("p"):
            n = int(giris.split(" ")[1])
            r = int(giris.split(" ")[2])
            print("P({},{}) = {}".format(n, r, permutasyon(n, r)))

        elif giris.startswith("t"):
            n = int(giris.split(" ")[1])
            r = int(giris.split(" ")[2])
            print("Tekrarlı P({},{}) = {}".format(n, r, permutasyon(n, r, 1)))

        elif giris.startswith("k"):
            n = int(giris.split(" ")[1])
            r = int(giris.split(" ")[2])
            print("C({},{}) = {}".format(n, r, kombinasyon(n, r)))

        elif giris.startswith("i"):
            t = int(giris.split(" ")[1])
            print("F{} = {}".format(t, fibonacci(t)))

        elif giris.startswith("ç"):
            print("\n    Çıkış yapıldı.\n")
            exit(0)

        else:
            print("Hatalı giriş yaptınız!")
            continue

    except IndexError:
        print("Hata! İşlemin yapılabilmesi için yeterli terim girilmeli!")
    except ValueError:
        print("İfadeler arası en fazla bir boşluk olmalı!")
    except KeyboardInterrupt:
        print("\n\n    Çıkış yapıldı.\n")
        exit(0)
    except Exception as e:
        print(f"\nHata: {e}")
        exit(1)