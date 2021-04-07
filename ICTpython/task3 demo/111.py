for g in range(2,13):
  for k in range(1,13):
    if ((g**k) % 13) == 1:
      print('g =',g,'k =',k,'g ^ k =',g**k)
  print("\n")