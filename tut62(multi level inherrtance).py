# MUlti level inheritance
class Dad:
     basketball =1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f'Yes, I dance {self.dance} no of times.'

class GrandSon(Son):
    dance = 6
    def isdance(self):    #overwrited
        return f'Yes, I dance awesomely {self.dance} no of times.'
Howard = Dad()
Tonny = Son()
Peter = GrandSon()

print(Peter.isdance())
print(Tonny.basketball)