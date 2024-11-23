class BasicMath:
   pass

class Advance(BasicMath):

    def factorial(self, num):
        fact = 1
        for num in range(1, num+1):
          fact *= num
        return fact

    @staticmethod
    def isprime(number):
        if number <= 1:
            return False
        for num in range (2, int(number **0.5) + 1):
            if number % num == 0:
               return False
        return True


a1 = Advance()


print(a1.factorial(5))
print(a1.isprime(4))
print(a1.isprime(5))
