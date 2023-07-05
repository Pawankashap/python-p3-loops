#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
      print(counter)
      counter -= 1
    print("Happy New Year!")
    #pass

# def fizzbuzzPrinter():
#     for num in range(1, 101):
#         print(fizzbuzz(num))


def fizzbuzz():
    for num in range(1, 101):
      if num % 3 == 0 and num % 5 == 0:
          print("FizzBuzz")
      elif num % 3 == 0:
          print("Fizz")
      elif num % 5 == 0:
          print("Buzz")
      else:
          print(num)
    #pass

def reverseString(str):
  reversedStr = ""
  for i in range(len(str)):
    reversedStr = str[i] + reversedStr
  return reversedStr

def square_integers(int_list):
    # code goes here!
    return list(map(lambda num: num ** 2, int_list))
    #pass
