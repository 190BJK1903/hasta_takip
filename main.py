#siniflar class

class Hasta():
    def __init__(self, name, problem, yas):
        self.name = name
        self.problem = problem
        self.yas = yas
        self.liste = []

    def problem_ekle(self, problem):
        self.liste.append(problem)
    



hasta = Hasta("Ricardo Quaresma", "ayak kirigi", 38)   #
hasta2 = Hasta("Anderson Talisca", "bas agrisi", 30)    


print(hasta.name, hasta.problem, hasta.yas)
print(hasta2.problem)



