from superhero import Codinghero

class Qahero(Codinghero):
    def __init__(self, name, secretIdentity, proficientLanguage, bugs, automationTool):
        super().__init__(name, secretIdentity, proficientLanguage, bugs)
        self.automationTool = automationTool
        self.testCases = 0


#calls the parent's method does not override it! 
    def writeTests(self, testCoverage):
        super().writeTests(testCoverage)
        print(f"Uses {self.automationTool} for automation testing!")
        self.testCases += 10


    def testSuite(self):
        print(f"{self.name} runs full test suite using {self.automationTool}")
        self.bugsFixed += 8


    def __str__(self):
        return (f"{super().__str__()} tool: {self.automationTool} tests: {self.testCases}")