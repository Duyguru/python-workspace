import random

def get_bilgisayar_hamlesi():
    secenekler = ["taş", "kağıt", "makas"]
    return random.choice(secenekler)

def kazanma_durumu(hamle, bilgisayar_hamlesi):
    if bilgisayar_hamlesi == hamle:
        return "Berabere"
    elif (hamle == "taş" and bilgisayar_hamlesi == "makas") or \
         (hamle == "kağıt" and bilgisayar_hamlesi == "taş") or \
         (hamle == "makas" and bilgisayar_hamlesi == "kağıt"):
        return "Kazandınız"
    else:
        return "Kaybettiniz"

def oyun():
    while True:
        hamle = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
        if hamle not in ["taş", "kağıt", "makas"]:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue

        bilgisayar_hamlesi = get_bilgisayar_hamlesi()
        print(f"Bilgisayarın hamlesi: {bilgisayar_hamlesi}")
        
        sonuc = kazanma_durumu(hamle, bilgisayar_hamlesi)
        print(sonuc)
        
        tekrar_oyna = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if tekrar_oyna != 'e':
            print("Oyun bitti. Teşekkürler!")
            break

if __name__ == "__main__":
    oyun()

