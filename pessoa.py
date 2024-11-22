class People:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        print('Nome:{}\nIdade:{}'.format(self.name, self.age))

    def run(self, run):
        if run:
            print(f"{self.name} está correndo")
        else:
            print(f"{self.name} não está correndo")

    def eat(self, eat):
        if eat:
            print(f"{self.name} está comendo")
        else:
            print(f"{self.name} não está comendo")




