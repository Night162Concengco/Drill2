#numbers#

from pyscript import display, document



def adding_numbers(f):
    document.getElementById("result").innerHTML = ""
    number1 = float(document.getElementById('num1').value)

    number2 = float(document.getElementById('num2').value)
    
    sum = number1 + number2


    display(f'The sum of {number1} and {number2} is {sum}', target='result')
 

def subtracting_numbers(f):
    document.getElementById("result").innerHTML = ""
    number1 = float(document.getElementById('num1').value)

    number2 = float(document.getElementById('num2').value)
    
    sum = number1 - number2

    display(f'The difference of {number1} and {number2} is {sum}', target='result')
