class BrowserHistory(object):
    def __init__(self, homepage):
        self.stk1 = []
        self.stk2 = []
        self.visit(homepage)

    def visit(self, url):
        self.stk1.append(url)
        self.stk2 = []

    def back(self, steps):
        while steps and len(self.stk1) > 1:
            self.stk2.append(self.stk1.pop())
            steps -= 1
        return self.stk1[-1]

    def forward(self, steps):
        while steps and self.stk2:
            self.stk1.append(self.stk2.pop())
            steps -= 1
        return self.stk1[-1]

# Example usage in Python 2:
# obj = BrowserHistory("homepage.com")
# obj.visit("page1.com")
# print obj.back(1)
# print obj.forward(1)
