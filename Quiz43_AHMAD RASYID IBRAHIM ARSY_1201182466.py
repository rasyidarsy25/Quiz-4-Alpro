listGPA= [2.1,2.5,4,3]
def hadiah (GPA):
    bonus = 500000
    hadiah = GPA * bonus
    return hadiah

for GPA in listGPA :
        if GPA > 2.5:
            print("Total hadiah anda adalah : Rp", hadiah(GPA))
        else :
            print("Maaf coba lagi")