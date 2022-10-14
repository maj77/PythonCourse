from cmath import sqrt
import os
from pathlib import Path
import timeit
from PIL import Image
from matplotlib import test
import numpy as np

# zad wprowadzanie danych
class Person:
    def __init__(self) -> None:
        self.name = ""
        self.surname = ""
        self.date = 0

    def get_inputs(self):
        self.name, self.surname, self.date = input("Enter name, surname and birth date: ").split()
    
    def print_data(self):
        print(f'Name {self.name}, Surname: {self.surname}, Date: {self.date}')

# zad sejf
class Lock:
    def __init__(self) -> None:
        self.code = [9, 9, 7, 4]

    def change_code(self, new_code):
        self.code = new_code

    def get_keyboard_input(self):
        user_input = []
        for number in self.code:
            user_input.append(int(input()))
        return user_input

    def check_code(self, input_code):
        if(input_code == self.code):
            return "succes"
        else:
            return "wrong code"

# zad ilosc plikow i struktura katalogu
class Dirs:
    def __init__(self) -> None:
        self.file_count = 0

    def count_files(self, path:Path):
        #len(list(path.rglob('*')))
        cnt = 0
        for p in path.rglob('*'):
            cnt += 1
        self.file_count = cnt
    
    def list_dirs(self, path:Path):
        for file in path.rglob('*'):
            print(file.name)
        
    def get_file_count(self):
        return self.file_count

# zad konwesja  rozrzerzen
class Images:
    #def __init__(self) -> None:  

    def to_png(self, path):
        img = Image.open(path)
        img.save(r'converted.png', format='png')
     
    def to_jpg(self, path):
        img = Image.open(path)
        img.save(r'converted', format='jpg')

# zad: usuwanie i podmienianie słow
class Text:
    def __init__(self) -> None:
        self.words = [" się", " i", " oraz", " nigdy", " dlaczego"]
        self.words_dict = {
            " i" : "?oraz",
            " oraz" : " i",
            " nigdy" : " prawie nigdy",
            " dlaczego" : " czemu"
        }

    def del_keywords(self, string):
        for word in self.words:
             string = string.lower().replace(word, '')
        return ' '.join(string.split())

    def replace_keywords(self, string):
        for key in self.words_dict:
            string = string.lower().replace(key, self.words_dict[key])
        string = string.lower().replace("?oraz", " oraz")
        return ' '.join(string.split())

class Algs:
    def __init___(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
    
    def roots(self, a, b, c):
        delta = b*b-4*a*c
        if delta == 0:
            return -b/2*a
        elif delta > 0:
            return ((-b-sqrt(delta))/2*a, (-b+sqrt(delta))/2*a)
        else:
            raise NotImplemented

    def bubble_sort(self, arr):
        for i in range(1,len(arr)-1):
            for j in range(0, len(arr)-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
    
    def dot_product(self, u, v):
        return u*v

    def matrix_sum(self, A, B):
        return A+B
    
    def matrix_mult(self, A, B):
        return np.matmul(A, B)

    def det(self, A):
        return np.linalg.det(A)

class Complex:
    def __init__(self, real, imaginary) -> None:
        self.re = real
        self.im = imaginary
    
    def __str__(self):
        return f"{self.re}+j{self.im:}"

    def __add__(self, number):
        if isinstance(number, float) or isinstance(number, int):
            return Complex(self.re + number, self.im)
        if isinstance(number, Complex):
            return Complex(self.re + number.re, self.im + number.im)
    
    def __sub__(self, number):
        if isinstance(number, float) or isinstance(number, int):
            return Complex(self.re - number, self.im)
        if isinstance(number, Complex):
            return Complex(self.re - number.re, self.im - number.im)

    def __mul__(self, number):
        if isinstance(number, float) or isinstance(number, int):
            return Complex(self.re * number, self.im * number)
        if isinstance(number, Complex):
            re = (self.re * number.re) - (self.im * number.im)
            im = (self.re * number.im) + (self.im * number.re)
            return Complex(re, im)
    
    def __truediv__(self, number):
        if isinstance(number, float) or isinstance(number, int):
            if number == 0:
                raise ZeroDivisionError
            return Complex(self.re / number, self.im / number)
        if isinstance(number, Complex):
            if number.re == 0 and number.im == 0:
                raise ZeroDivisionError
            else:
                re = ((self.re*number.re) + (self.im*number.im)) / (number.re**2 + number.im**2)
                im = ((self.im*number.re) - (self.re*number.im)) / (number.re**2 + number.im**2)
                return Complex(re, im)

    # TODO CALCULATOR: Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora,
    #                  parsującego i wykonującego równanie podane przez użytkownika


#blackbox = Lock()
#print(blackbox.check_code([9,9,7,4]))
#blackbox.change_code([1,2,3,4,5,6])
#print(blackbox.check_code([1,2,3,4,5,6]))

#listdir = Dirs()
#listdir.count_files(Path("D:\Studia_EiT"))
#print(listdir.get_file_count())
#listdir.count_files(Path(r"C:\Users\Marcin\Desktop"))
#print(listdir.get_file_count())
#listdir.list_dirs(Path(r"D:\Studia_EiT\Semestr VII\Python"))

#image = Images()
#image.to_png(r'D:\Studia_EiT\Semestr VII\Python\Lab\Lab1\Untitled.jpg')

#test_text = Text()
#sample_text = "ala ma kota I ten I, DLACZEGO ORAZ ORAZ ORAZ kot NIGdy przenigdy się nie myje, dlaczego tak jest? nie wiem. Ola ma kota oRaZ psa i one też się nigdy nie myją, DlACZEgo?"
#sample_text_converted = test_text.del_keywords(sample_text)
#print(sample_text)
#print(sample_text_converted)
#sample_text2 = "kot ali oraz pies oli nigdy się nie myją! dlaczego tak jest? nigdy się nie dowiemy i basta, nie ma dlaczego oraz i"
#sample_text_converted = test_text.replace_keywords(sample_text2)
#print(sample_text_converted)
#print(sample_text2)

#algorithm = Algs()
#print(algorithm.dot_product(np.array([1, 2, 3, 5]), np.array([2, 2, 2, 2])))
#A = np.random.rand(128,128)
#B = np.random.rand(128,128)
#print(algorithm.matrix_sum(A,B))
#C = np.random.rand(5, 8)
#D = np.random.rand(8, 2)
#print(algorithm.matrix_mult(C,D))
#print(algorithm.matrix_mult(C,D).shape)
#E = np.random.rand(4,4)
#print(algorithm.det(E))

cpx1 = Complex(5, 5)
cpx2 = Complex(2, 4)

cpx3 = cpx1+cpx2
cpx4 = cpx1+2
cpx4 = cpx2/3
print(cpx4.re, cpx4.im)
print(cpx3.re, cpx3.im)
print(cpx1.re, cpx1.im)
print(cpx4)