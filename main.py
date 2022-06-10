var1 = input("Give me a number, not a string. ")
if type(var1) == str:
  print("\nLet's see.  Your variable is a stri- wait what?!")
  print("I thought you typed a number?")
else:
  print("Your variable is NOT a string.")
print("\nOh, I forgot.  Everything is a string by default...  let's convert.")
var2 = int(var1)
if type(var2) == str:
  print("Your variable is still a string.")
else:
  print("Now your variable is NOT a string.")
print("\n The End. :-)")