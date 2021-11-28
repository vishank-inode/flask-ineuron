class Product:
    def __init__(self, name, price, size, qty, description):
        self.name = name
        self.price = price
        self.size = size
        self.qty = qty
        self.description = description

    def __repr__(self):
        return f"Product name: {self.name}, price: {self.price}, qty: {self.qty}, decription: {self.description}"
    def __str__(self):
        return "This is the product name: "+ self.name
    def updateProduct(self, name, product):
        self = product
        

class ProductCollection:
    def __init__(self):
        self.productsList = []

    def addProduct(self,product):
        self.productsList.append(product)
    
    def getListOfProducts(self):
        return self.productsList

d = Product('Battery',10,"20in",10,"This is a battery")

print(d)

collection = ProductCollection()
collection.addProduct(print(d))
print(collection.getListOfProducts())
