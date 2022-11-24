# 2312 최혜민
class Employee:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    

class Manager(Employee):
    def __init__(self, id, name, code, manager_s):
        super().__init__(id, name, code)
        self.manager_s = manager_s

    def __str__(self):
        return str(self.id) + "\t" + str(self.name) + "\t" + str(self.code) + "\t" + str(self.manager_s)

class SalesMan(Employee):
    def __init__(self, id, name, code, sales_s):
        super().__init__(id, name, code)
        self.sales_s = sales_s
    
    def __str__(self):
        return str(self.id) + "\t" + str(self.name) + "\t" + str(self.code) + "\t" + str(self.sales_s)

class Temporary(Employee):
    def __init__(self, id, name, code, temporary_s, priory):
        super().__init__(id, name, code)
        self.temporary_s = temporary_s
        self.priory = priory

    def __str__(self):
        return str(self.id) + "\t" + str(self.name) + "\t" + str(self.code) + "\t" + str(self.temporary_s) + "\t" + str(self.priory)

res = []
while(True):
    e = list(map(str, input('사번, 이름, 기본급코드, 수당, 계약기간 입력(종료 0) : ').split(' ')))

    if e[0] == '0':
        break
    elif e[0][2:4] == "RM":
        res.append(Manager(e[0], e[1], e[2], e[3]))
    elif e[0][2:4] == "RS":
        res.append(SalesMan([0], e[1], e[2], e[3]))
    elif e[0][2:4] == "TE":
        res.append(Temporary(e[0], e[1], e[2], e[3], e[4]))

print("<<객체 생성 확인>>")
for i in res:
    print(i)

print("Manager", end="")
print("*"*30)
print("*"*37)
print("SalesMan", end="")
print("*"*29)
print("*"*37)
print("Temporary", end="")
print("*"*28)
print("*"*37)