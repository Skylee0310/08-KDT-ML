class Person :
    def __init__(self, name):
        self.name = name
        print(self.name + ' is initialized')

    def work(self, company):
        print(self.name + ' is working in ' + company)
    def sleep(self):
        print(self.name + ' is sleeping')

# Person instance 2개 생성
obj = Person('Park')

# method call
obj.work('ABCDEF')
obj.sleep()

# 속성에 직접 접근, 기본적으로는 파이썬에서는 모두 Public
print('current person object is ', obj.name)
