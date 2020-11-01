# 讀取檔案
def read_file(filename, products):
	with open(filename, "r", encoding = "utf-8") as f:
		for p in f:
			if "商品,價格" in p:
				continue
			name, price = p.strip().split(",")
			products.append([name, price])
	print(products)
	return products

#使用者記帳
def buying_record(products):
	while True :
		name = input("請輸入商品名稱：")
		price = int(input("請輸入商品價格："))
		products.append([name, price])
		quit = input("請問還需繼續記帳嗎(Y/N):")
		if quit.lower() == "n":
			break
	print(products)
	return products

# 列印記帳明細
def buying_detail(products):
	for line in products:
		print(f"{line[0]}的價格為{line[1]}元")
	return line

# 寫成CSV檔 write_file
def write_file(filename, products):
	with open(filename, "w", encoding = "utf-8") as f:
		f.write("商品,價格\n")
		for line in products:
			f.write(line[0] + "," + str(line[1]) + "\n")

# 程式啟動點
def main():
	products = []
	import os
	filename = "products.csv"
	if os.path.isfile(filename):
		print("file was found")
		read_file(filename, products)
	else:
		print("file doesn't be found")
	buying_record(products)
	buying_detail(products)
	write_file(filename, products)
	return products
main()