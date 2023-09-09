from package.module1 import Client
from package.module2 import getClientCart, getTotalCart

#Se crea el cliente y este compra varios productos
client1 = Client("Lucia", "Dias", 27, "luciadias.dev@gmail.com")
client1.buy("Harina", 5, 310)
client1.buy("Azúcar", 1, 630)
client1.buy("Sal", 2, 230)

#Se imprime el cliente y se calcula el total
getClientCart(client1)
getTotalCart(client1.cart)
