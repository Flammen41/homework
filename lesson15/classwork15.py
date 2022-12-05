# class Student():
#     def __init__(self, name, surname, zno_u, zno_m):
#         self.name=name
#         self.surname=surname
#         self.certs=[]
#         self.zno_u = zno_u
#         self.zno_m = zno_m
#
#     def displayinfo(self):
#         print(self.name)
#         print(self.surname)
#         print("cert:", ", ".join(self.certs))
#         print("zno:",self.zno)
#
#     def calculate_rate(self):
#         return (self.zno_u + self.zno_m)/2
#
# student1 = Student('Anton', 'Kovalev', 95,69)
# student2 = Student('Vasya', 'Bedov', 92,59)
# student3 = Student('Sasha', 'Klev', 88,49)
#
# std_list = [student1,student2,student3]
# print(std_list)
# rate_list = sorted([std.calculate_rate() for std in std_list], reverse=True)
# print(rate_list)
########
# #Task2
# class Parcel:
#     parcel_count = 0
#     parcel_limit = 4
# def init(self, height, length, width) -> None:
#     if Parcel.parcel_count == Parcel.parcel_limit:
#         print(f'Parcel limit reached: {Parcel.parcel_limit}')
#         return
#     self.height = height
#     self.length = length
#     self.width = width
#     Parcel.parcel_count += 1
#
# def calculate_volume(self):
#     return self.width * self.length * self.height
#
# par1 = Parcel(34,5,4)
# par2 = Parcel(34,55,344)
# par3 = Parcel(33,54,44)
# par4 = Parcel(34,55,144)
# par5 = Parcel(34,55,244)
#
# par_list = [par1,par2,par3,par4,par5]
# print(par_list)
# par_volume = sorted([(par.calculate_volume()) for par in par_list])
# print(par_volume)
#######################3
class Triangle:
    def __int__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (1/2) * (self.a+self.b+self.c)

triangle1 = Triangle(3,4,3)
triangle2 = Triangle(6,8,8)

print(square(triangle1))

print(perimeter(triangle2))
