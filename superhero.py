class Codinghero:
    def __init__(self, name, secretIdentity, proficientLanguage, bugs):
        self.name = name
        self.secretIdentity = secretIdentity
        self.proficientLanguage = proficientLanguage
        self.bugs = bugs
        self.bugsFixed = 0
        self._energy = 100 #Private attribute 


#method to make the code clean

    def cleanCode(self, linesOfCode):
        if self._energy >=30:
            print(f"{self.name} writes clean{self.linesOfCode} lines with {self.proficientLanguage}!")
            self._energy -= 30
            self.bugsFixed +=1
        else:
            print(f"{self.name} needs coffee while fixing bugs!")


#method to write tests to fix /prevent bugs 

    def writeTests(self, testCoverage):
        print(f"{self.name} writes tests on{testCoverage} of the codebase!")
        self.bugsFixed += 3

    
 #method to restore energy using coffee

    def drinkCoffee(self):
        self._energy = 100
        print(f"{self.name} loves coffee and code!")


#method for debugging!
    def debug(self):
        print(f"{self.name} strives to {self.bugs} while tracing changes!")
        self.bugsFixed +=4

    
    def __str__(self):
        return (f"{self.name} | Secret: {self.secretIdentity} | Language: {self.proficientLanguage} | Bugs Fixed: {self.bugsFixed}")


        
        