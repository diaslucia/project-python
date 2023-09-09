#Imprime el carrito del usuario
def getClientCart(client):
    print(f"{client.name} {client.surname} tiene en su carrito: {client.cart}")

#Sumar el total del carrito e imprimirlo
def getTotalCart(cart):
    total = 0
    for item in cart:
         total += item["quantity"] * item["price"]
    print(f"El total del carrito es ${total}") 