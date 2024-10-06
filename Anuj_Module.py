print('''Anuj_Module 2.5.1 (SDL 2.28.2, Python 3.11.3)
Hello from the Anuj_Modules community. https://www.pygame.org/contribute.html''')




def greet():
    print('Hello Buddy!!')    
    

    
def say_hello():
    print('Hello Buddy!,How are you??')
    
# args:- dtype

def introduction(name:'Idhar name bharna hai',
                 age:'int',
                 salary:'float',
                 add:'str')->  None:
    '''This is an Introduction func,
    created by user, you have to give some arguments,
    it will return a wonderful message'''
    
    print(f'Your Name is {name}')
    print(f'Your Age is {age}')  
    print(f'Your Salary is {salary}')   
    print(f'Your Address is {add}')    
    
    
def count(data):
    result = 0
    for i in data:
        result += 1
    return result

def summ(any_data:'list,tuple,set'):
    ans = 0
    
    for i in any_data:
        ans += i
    return ans


def prime_number(num):
    for i in range(2,num):
        if num % i == 0:
            print('Not a Prime Number')
            break
    else:
        print('Prime Number!!')
        
        
        
def give_fibonnaci(num):
    fibo = [0,1]
    
    for i in range(num-2):
        next_num = fibo[-1] + fibo[-2]
        fibo.append(next_num)
    return fibo   



def pattern(w):
    
    word = w.upper().replace(' ','')
    num = len(word)

    for i in range(1,num):
        print(' '*(num-i)+ ' '.join(word[0:i]))

    for i in range(num,0,-1):
        print(' '*(num-i)+ ' '.join(word[0:i]))
        
        

def check_armstrong(num):
    pw = len(str(num))
    ans = 0
    
    for i in str(num):
        ans += int(i)**pw
    return True if ans == num else False




def check_max(data):
    my_max = data[0]
    
    for i in data:
        if i>my_max:
            my_max = i
    return my_max



def give_prime(n1,n2):
    if n1 == n2 == 1:
        print('1 is not a Prime number!!')
        
    elif n1>1 and n2>1:
        all_prime = []
        for num in range(n1,n2+1):

            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                all_prime.append(num)

        return all_prime
    
    else:
        print('Invalid numbers!!')
        
        

        
def check_armstrong(num):
    pw = len(str(num))
    ans = 0
    
    for i in str(num):
        ans += int(i)**pw
    return True if ans == num else False



def give_area(shape = None):
    
    if shape == None:
        area = 0
        print('No Such area for None type Shape!!')
    
    elif shape.lower() == 'rectangle':
        
        l = float(input('Enter length: '))
        b = float(input('Enter breadth: '))
        
        area = l*b
        print(f'Area of {shape} is: {round(area,2)} sq unit')
        
        
    elif shape.lower() == 'circle':
        
        r = float(input('Enter radius: '))
        area = 3.14*r**2
        print(f'Area of {shape} is: {round(area,2)} sq unit')
        
        
    elif shape.lower() == 'triangle':
        
        a = float(input('Enter side a: '))
        b = float(input('Enter side b: '))
        c = float(input('Enter side c: '))
    
        
        s = (a + b + c)/2
        
        if (a+b)>c   and (b+c)>a  and (c+a)>b:
        
            area = (s*(s-a)*(s-b)*(s-c))**0.5
            print(f'Area of {shape} is: {round(area,2)} sq unit')
            
        else:
            print('No such triangle can be formed using given sides!!')
            print('''"a + b" must be greater than "c", as the sum of two side 
            lengths has to exceed the length of the third side!''')
        
    elif shape.lower() == 'square':
        side = float(input('Enter side of a Square: '))
        
        area = side * side
        print(f'Area of {shape} is: {round(area,2)} sq unit')
        
        
    else:
        print('No such shape found!!')
        

                
            
            
def rec_factorial(n):
    if n == 1:
        return n
    else:
        return rec_factorial(n-1)*n
