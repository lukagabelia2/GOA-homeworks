#  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი

num = int(input("text namebr: "))

for i in range(num):
    if i % 2 ==0:
        print(str(i) +"luwia")
    else:
        print(str(i)+"kenti")