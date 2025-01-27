from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fSema = Semaphore(0)
        self.bSema = Semaphore(0)
        self.fbSema = Semaphore(0)
        self.nSema = Semaphore(1)

    # printFizz outputs "fizz"
    def fizz(self, printFizz: callable) -> None:
        for i in range(3, self.n + 1, 3):
            if i % 5 != 0:
                self.fSema.acquire()
                printFizz()
                self.nSema.release()

    # printBuzz outputs "buzz"
    def buzz(self, printBuzz: callable) -> None:
        for i in range(5, self.n + 1, 5):
            if i % 3 != 0:
                self.bSema.acquire()
                printBuzz()
                self.nSema.release()

    # printFizzBuzz outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: callable) -> None:
        for i in range(15, self.n + 1, 15):
            self.fbSema.acquire()
            printFizzBuzz()
            self.nSema.release()

    # printNumber outputs a number
    def number(self, printNumber: callable) -> None:
        for i in range(1, self.n + 1):
            self.nSema.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fbSema.release()
            elif i % 3 == 0:
                self.fSema.release()
            elif i % 5 == 0:
                self.bSema.release()
            else:
                printNumber(i)
                self.nSema.release()
