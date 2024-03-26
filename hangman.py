import random
liste=["panda","yunus","kelebek","kedi","aslan","balık"]
kelime=random.choice(liste)
adam=['''
  +-----+
  O     |
 /|\    |
  |     |
 / \    |
      -----''','''
 +-----+
  O     |
 /|\    |
  |     |
 /      |
      -----''','''
 +-----+
  O     |
 /|\    |
  |     |
        |
      -----''','''
 +-----+
  O     |
 /|\    |
        |
        |
      -----''','''
 +-----+
  O     |
 /|     |
        |
        |
      -----''','''
 +-----+
  O     |
  |     |
        |
        |
      -----''','''
 +-----+
  O     |
        |
        |
        |
      -----''','''
 +-----+
        |
        |
        |
        |
      -----''']
dogruHarf = []
yanlisHarf = []
hak = len(adam)

while hak > 0:
    out = ""
    for harf in kelime:
        if harf in dogruHarf:
            out += harf
        else:
            out += "_"
    print("Kelime: ", out)
    print(adam[len(adam) - hak])
    
    girHarf = input("Bir harf girin: ").lower()

    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print(girHarf, "zaten girildi.")
        continue

    if girHarf in kelime:
        print("Doğru harf!")
        dogruHarf.append(girHarf)
        if set(kelime) == set(dogruHarf):
            print("Tebrikler, kelimeyi buldunuz! Kelime:", kelime)
            break
    else:
        print("Yanlış harf!")
        yanlisHarf.append(girHarf)
        hak -= 1

if hak == 0:
    print("Hakkınız kalmadı. Adam asıldı!")
  
