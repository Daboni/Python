# class

# +,-,*,/ 4가지 기능을 갖는 계산기 클래스
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + sellf.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# Constructor
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + sellf.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# Inheritance
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# Overriding
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else :
            return self.first / self.second

