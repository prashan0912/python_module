


class Product:
    def __init__(self,id,model,price):
        print("constructor call when creation of object")
        self.id = id;
        self.model = model;
        self.price = price;
     
# product = Product();

Product.id = "123"
Product.model = "#1231239012"
Product.price = "3000"

print(Product)

print(Product.id)


product2 = Product("123","#1230892","30000")
print(product2)