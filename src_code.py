class StringCalculator:
    def add(self, numbers):
        if numbers == '':
            return 0
        sum = 0        
        lst = list(map(int ,numbers.split(",")))
        for i in lst:
            if (i < 0):
                raise Exception("Negatives not allowed",i)
            if(i<=1000):
                sum += i 
        return sum
        
obj = StringCalculator()
str = input("Enter")
print(obj.add(str))
