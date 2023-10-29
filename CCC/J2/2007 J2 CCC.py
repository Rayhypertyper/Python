x = input
while x != 'TTYL':
  x = input()
  if x == 'CU':
    print("see you")	
    continue
  if x == ':-)':
    print("I'm happy")
    continue
  if x ==";-)":
    print("wink")
    continue
  if x == ":-(":
    print("I'm unhappy")
    continue
  if x == ":-P":
    print("stick out my tongue")
    continue
  if x == "(~.~)":
    print("sleepy")
    continue
  if x == "TA":
    print("totally awesome")
    continue
  if x == "CCC":
    print("Canadian Computing Competition")
    continue
  if x == "CUZ":
    print("because")
    continue
  if x == "TY":
    print("thank-you")
    continue
  if x == "YW":
    print("you're welcome")
    continue
  if x == "TTYL":
    print("talk to you later")
    continue
  elif x != 'CU' or ':-)' or ';-)' or ':-(' or ':-p' or '(~.~)' or 'TA' or 'CCC' or 'CUZ' or 'TY' or 'YW' or 'TTYL':
      print(x)