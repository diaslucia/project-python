class Client:
    def __init__(self, name, surname, age, email):
      self.name= name
      self.surname= surname
      self.age= age
      self.email= email
    

    def __str__(self):
        return f"Se registró el cliente {self.name} {self.surname}"