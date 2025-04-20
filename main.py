from superhero import Codinghero
from qahero import Qahero

#creating our coding superhero
def main():
    
devHero = Codinghero(
    name = "Azaari",
    secretIdentity = "Code Ninja",
    proficientLanguage = "Python",
    bugs = "bugs enemy"
)


#Create QA superhero

qasuperHero = Qahero(
    name = "Gatwiri",
    secretIdentity = "Fine QA!",
    proficientLanguage = "Javascript",
    bugs = "Flaky Tests",
    automationTool = "Cypress"
)


#demonstration of powers
print("\n=== Codinghero in Action ===")
devHero.cleanCode(50)
devHero.writeTests(80)
devHero.debug()
print(devHero)



print("\n=== Codinghero in Action ===")
qasuperHero.writeTests(85)
qasuperHero.testSuite()
qasuperHero.drinkCoffee()
print(qasuperHero)

main()