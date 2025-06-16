def run():
  code = "print('Hello World')"
  eval(code)

  user_input = input("Enter a number: ")
  try:
    result = int(user_input) / 0
    print(   result  )
  except:
    print("something went wrong")

  temp = []
  for i in range(0,10):
      temp.append(i)
  for i in range(0,10):
      temp.append(i)



