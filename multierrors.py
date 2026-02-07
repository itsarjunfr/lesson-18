try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    div = num1/num2
    print(div)
    print(div1)

except NameError as ex:
    print('Exception:', ex)
except ZeroDivisionError:
    print('A number cannot be divided by 0.')
except ValueError: 
    print('Enter numerical values only.')

finally: 
    print('Code has run successfully.')
    