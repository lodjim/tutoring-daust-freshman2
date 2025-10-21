cars = [
    {"model": "Tesla S3", "registration number": "122F3", "price": 1343},
    {"model": "BMW X5", "registration number": "AB1234", "price": 52000},
    {"model": "Audi A4", "registration number": "CD5678", "price": 41000},
    {"model": "Toyota Corolla", "registration number": "EF9012", "price": 22000},
    {"model": "Ford Mustang", "registration number": "GH3456", "price": 65000},
    {"model": "Honda Civic", "registration number": "IJ7890", "price": 24000},
    {"model": "Mercedes C-Class", "registration number": "KL1122", "price":47000},
    {"model": "Nissan Leaf", "registration number": "MN3344", "price": 29000},
    {"model": "Chevrolet Camaro", "registration number": "OP5566", "price": 60000},
    {"model": "Kia Sportage", "registration number": "QR7788", "price": 27000}
]
max_price_model = ""
max_price = 0
for car in cars:
    price = car["price"]
    model = car["model"]
    if price > max_price:
        max_price = price
        max_price_model = model
    
print("The most expensive car in this list is:",max_price_model,"the price is:",max_price)
