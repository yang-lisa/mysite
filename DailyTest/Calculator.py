class Calculator:

    def __init__(self):
        pass


    def add(self, a, b):
        result = a + b
        print('result:', result)
        return result

    def minus(self, a, b):
        result = a - b
        print('result:', result)
        return result

    def multip(self, a, b):
        result = 0.0
        result = a * b
        print('result:', result)
        return result

    def div(self, a, b):
        result = 0.0
        result = a / b
        print('result:', result)
        return result




if __name__ == "__main__":
    cal = Calculator()
