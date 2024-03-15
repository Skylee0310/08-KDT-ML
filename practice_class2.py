'''
클래스 변수 : 해당 클래스로 생성된 모든 인스턴스(클래스의 현재 생성된 오브젝트)가 공통적으로 사용하는 변수.
=>  클래스 변수는 클래스 내/외부에서 '클래스명.클래스 변수명'으로 접근할 수 있음.

클래스 메서드 :
- 메서드 앞에 @classmethod를 반드시 표시하여 클래스 메서드임을 표시.
=> 클래스 메서드는 객체 인스턴스를 의미하는 self 대신 cls라는 클래스를 의미하는 파라미터를 인수로 전달받음.

'''


class Person :
    count = 0 # 클래스 변수
    def __init__(self, name):
        self.name = name
        Person.count +=1 # class 변수 count 증가
        print(self.name + ' is initialized')

    def work(self, company):
        print(self.name + ' is working in ' + company)
    def sleep(self):
        print(self.name + ' is sleeping')
    @classmethod
    def getCount(cls): # 클래스 메소드
        return cls.count

# Person instance 2개 생성
obj1 = Person('Park')
obj2 = Person('KIM')

# method call
obj1.work('ABCDEF')

obj2.sleep()

# 속성에 직접 접근, 기본적으로는 파이썬에서는 모두 Public
print('current person object is ', obj1.name, ", ", obj2.name)

# class method 호출
print('Person count ==', Person.getCount())

# 클래스 변수에 직접 접근
print(Person.count)
