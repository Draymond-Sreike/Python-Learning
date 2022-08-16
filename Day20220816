'''
a = int("123")
print(a)
a += 1
print(a)
'''
class Student:
    native_pace = '广东'
    def eat(self):
        print("学生在吃饭中")
    @classmethod
    def cm(cls):
        print("类方法")
    @staticmethod
    def sm():
        print("静态方法")
'''
stu = Student()
stu.eat()
Student.eat(stu)
#下面部分无需多此一举括号中再传入实例对象，否则会抛异常
#stu.eat(stu)  #TypeError: Student.eat() takes 1 positional argument but 2 were given
'''
std = Student()
print(std.native_pace)
print(Student.native_pace)
#在创建了对象之后，若在调用std.native_pace = '广东揭阳揭西'进行实例的变量修改之"前"用Student.native_pace = '广东揭阳'
#进行修改，则std实例的该变量会受到影响
Student.native_pace = '广东揭阳'
print(std.native_pace)
print(Student.native_pace)
std.native_pace = '广东揭阳揭西'
print(std.native_pace)
print(Student.native_pace)
Student.native_pace = '广东揭阳揭西棉湖'
print(std.native_pace)
print(Student.native_pace)
#在创建了对象之后，若在调用std.native_pace = '广东揭阳揭西'进行实例的变量修改之"后"用Student.native_pace = '广东揭阳'
#进行修改，则std实例的该变量将不再受到影响
print("----------------类方法------------------")
Student.cm()
std.cm()
#下面部分无需多此一举括号中再传入类对象，否则会抛异常
#std.cm(Student) #TypeError: Student.cm() takes 1 positional argument but 2 were given
print("----------------静态方法------------------")
Student.sm()
std.sm()
