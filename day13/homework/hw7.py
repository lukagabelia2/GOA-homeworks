# ომხმარებელს შემოატაინეთ 2 რიცხვი, და შემდეგ გამოიყენეთ შედარების ოპერატორები რა რიცხვსაც შეიყვანს მომხმარებელი, მასე გამოიყენთ შედარების ოპერატორები ==,!=,<,>,<=,=>.

a = int(input("text a number:"))
b = int(input("text a namber2:"))

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#ეს დავალება რომ შემსრულებინა პირველად ავიღე ცვლადი და შემდეგ მივანიჭე input() რადგან იქ ჩაწერილი ინფორმაცია გამომეტანა ტერმინალში,პირობა გვეუბნება რომ გამოგვატანა ციფრი,ამისთის კი საჭრო იყო input-ის int-რად გადაქევა,ეს იმიტომ რომ intup()  არის string-ი


#1)თუ ჩვენ პირველად შევიყვანდით ერთი და იგივე ციფრებს მაშინ მივიღებდით Trues რადგან == აღნიშნავშს "ტოლს"
#2)თუ ჩვენ ავიგებდით სხვადასხვა ციფრებს მაშინ ტერმინალშ მივიღებდით True რადგან != აღმიშნავს "არ უდრის"
#3)თუ ჩვენ ავიღებდით a ცვლადს უფრო პატარას ვიდრე b ეს იქნებოდა სწორი(True),რადგან < აღნიშნავს "ნაკლებობას"
#4) თუ ჩვენ ავიღებდით a ცვლად უფრო დიდს ვიდრე b ცვლად მაშნ მივიღებდით* True,რადგან > აღნიშნავს "მეტობას"
#5)თუ ჩვენ ავირებდით a ცვლადს უფრო პატარას ვიდრე b ეს იქნება სწორი(True),ასევე სწორი იქნებოდა როდესაც ავიღებდით ერთნაირ ციფრებს რადგან <= აღნიშნავს "ნაკლებია ან ტოოლს"
#6)თუ ჩვენ ავიღებდით a ცვლადს უფრო დიდს ვდრე b მაშინ მივიღებდით სწორს(True),ასევე როდესაც ავიღებდით ერთნაირ რიცხვებს რადგან >= აღნიშნავს "მეტია ან ტოლს"