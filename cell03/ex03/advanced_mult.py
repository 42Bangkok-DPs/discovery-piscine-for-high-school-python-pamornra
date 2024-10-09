table = 0
mtable = 12
while table <= mtable :
  print("table de",table,": ", end="")
  number=0
  while number <= mtable :
    print(table *number, end=" ")
    number +=1
  print(" ")
  table +=1
