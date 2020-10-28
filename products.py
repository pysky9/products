products = []
while True:
	product = []
	name = input("請輸入商品名稱：　")
	if name == "q":
		break
	price = input("請輸入商品價格：　")
	product.append(name)
	product.append(price)
	products.append(product)
print(products)