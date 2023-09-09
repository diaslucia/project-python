class Client:
    def __init__(self, name, surname, age, email):
      self.name= name
      self.surname= surname
      self.age= age
      self.email= email
      self.cart= []
    
    def __str__(self):
        return f"Se registró el cliente {self.name} {self.surname}"
    
    #Se agregar al carrito del ususario el producto y la cantidad
    def buy(self, product, quantity, price):
          self.cart.append({"product": product, "quantity": quantity, "price": price})
       