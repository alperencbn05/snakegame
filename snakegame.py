
from tkinter import *
import random

# ayarlar
kare_boyutu = 20
genislik = 400
yukseklik = 400
yem_boyutu = 10
skor = 0

# baslangic
pencere = Tk()
canvas = Canvas(pencere , width=genislik, height=yukseklik)
canvas.pack()

# yilanin baslangic konumu
yilan = [[60 , 100], [40, 100], [20 , 100]]
direction = "Right"

# yemin baslangic konumu
yem = [random.choice(range(0, 400, 20)), random.choice(range(0, 400, 20))]



def yon_degistir(event):
    global direction
    if event.keysym == "Up" and direction != "Down":
        direction = "Up"
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"
    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"
    elif event.keysym == "Right" and direction != "Left":
        direction = "Right" 

def hareket_et():
    global yem
    global yilan
    global direction
    global skor


    # mevcut kafa kordinatlari
    x, y = yilan[0]
    if direction == "Up":
        y -= kare_boyutu
    elif direction == "Down":
        y += kare_boyutu
    elif direction == "Left":
        x -= kare_boyutu
    elif direction == "Right":
        x += kare_boyutu


    yeni_kafa = [x, y]
    yilan.insert(0, yeni_kafa)  # yilanin basina yeni kafa ekle
    yilan.pop()  # yilanin sonundan bir parca sil

    

    canvas.delete("all")  # canvasi temizle

    for parcax , parcay in yilan:
        canvas.create_rectangle(parcax, parcay, parcax + kare_boyutu, parcay + kare_boyutu, fill="green")
    

    
    canvas.create_rectangle(yem[0], yem[1], yem[0] + yem_boyutu, yem[1] + yem_boyutu, fill="red")
    if yilan[0] == yem:
        skor += 1
        yilan.append(yilan[-1])  # yilanin sonuna bir parca ekle
        x = random.choice(range(0, 400, 20))
        y = random.choice(range(0, 400, 20))
        yem = [x, y]
        canvas.create_rectangle(yem[0], yem[1], yem[0] + yem_boyutu, yem[1] + yem_boyutu, fill="red")

    canvas.create_text(50, 10, text="Skor: " + str(skor), font=("Arial", 12), fill="black")

    if oyun_bitti():
        return
    canvas.after(200, hareket_et)


def oyunu_yeniden_baslat():
    global yilan
    global yem
    global skor
    global direction
    global btn
    try: 
        btn.destroy()
    except:
        pass
    try:
        sonskor.destroy()
    except:
        pass
    

    yilan = [[60 , 100], [40, 100], [20 , 100]]
    direction = "Right"
    yem = [random.choice(range(0, 400, 20)), random.choice(range(0, 400, 20))]
    skor = 0
    direction = "Right"
    canvas.delete("all")
    hareket_et()

def oyun_bitti():
    global yilan
    global btn
    global sonskor
    global skor
    

    if yilan[0][0] < 0 or yilan[0][0] >=  genislik or yilan[0][1] < 0 or yilan[0][1] >= yukseklik:
        canvas.delete("all")
        canvas.create_text(genislik // 2, yukseklik // 2, text="Oyun Bitti!", font=("Arial", 24), fill="red")

        btn = Button(pencere, text="Yeniden Başla", command=oyunu_yeniden_baslat)
        canvas.create_window(genislik//2, yukseklik//2 + 40, window=btn)

        sonskor = Label(pencere, text="Skor: " + str(skor), font=("Arial", 12))
        canvas.create_window(genislik//2, yukseklik//2 + 70, window=sonskor , anchor="center")
        




        return True
    
    
    elif yilan[0] in yilan[1:]:
        canvas.delete("all")
        canvas.create_text(genislik // 2, yukseklik // 2, text="Oyun Bitti!", font=("Arial", 24), fill="red")
    
        btn = Button(pencere, text="Yeniden Başla", command=oyunu_yeniden_baslat)
        canvas.create_window(genislik//2, yukseklik//2 + 40, window=btn)

        sonskor = Label(pencere, text="Skor: " + str(skor), font=("Arial", 12))
        canvas.create_window(genislik//2, yukseklik//2 + 70, window=sonskor , anchor="center")
        
        

        return True
    
    else:
        return False





    
pencere.bind("<KeyPress>" , yon_degistir)
hareket_et()
pencere.mainloop()
