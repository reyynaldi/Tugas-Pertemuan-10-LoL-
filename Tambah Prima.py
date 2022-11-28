import ast
list_of_list = ast.literal_eval(input())

def kosong(a):
    return a == []
def tail(a):
    if not(kosong(a)):
        return a[1:]
def listpertama(a):
    return a[0]
def atom(a):
    return not(kosong(a)) and jumlah(a) == 1
def islist(a):
    return not(atom(a))
def jumlah(a):
    if kosong(a):
        return 0
    else:
        try:
            return 1+jumlah(tail(a))
        except TypeError:
            return 1
def islist(L):
    if type(L) == list or not(atom(L)):
        return True
    else:
        return False
def is_prime(n, i = 2):
  if n < 2: return False
  elif n == 2: return True
  elif n % i == 0: return False
  elif (i * i) > n: return True
  else: 
    return is_prime(n, i + 1)

def prima(L):
  if kosong(L):
    return 0
  else:
    if not(islist(listpertama(L))):
      if is_prime(listpertama(L)):
        return listpertama(L)+prima(tail(L))
      else:
        return prima(tail(L))
    else:
      if atom(L):
        return prima(listpertama(L))
      else:
        return prima(listpertama(L))+prima(tail(L))


print(prima(list_of_list))


