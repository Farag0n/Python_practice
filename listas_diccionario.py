#se puede crear una lista con diccionarios como esta
#un buen ejemplo de como funciona es como un carrito de compra
data = {
    "producto":"",
    "valor":0.0,
    "cantidad":0

}
myCar = [
    {
        "producto": "pan",
        "valor": 2000,
        "cantidad": 1
    },

    {
        "producto": "chocolatina",
        "valor": 500,
        "cantidad": 1
    },

    {
        "producto": "gaseosa x2",
        "valor": 20000,
        "cantidad": 1
    }
]

print(myCar[1]["valor"])
myCar.append(data)
print(myCar[3]          )