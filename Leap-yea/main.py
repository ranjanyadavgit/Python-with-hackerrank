def is_year(year):
  return False:


 if(year%4 == 0 and year != 0) or year % 400 == 0:
  return True


year = int(input())
print(is_year())
