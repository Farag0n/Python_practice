txt = input("Ingresa un texto: \n")
maxTxt = 20

def veriMaxlong(text, numberText):

    if numberText > len(text):
        print(txt)
    elif numberText < len(text):
        print(text[:numberText])

        
veriMaxlong(txt, maxTxt)   
        



    


