def floyd(n):
     count = 1
     string = ""
     for i in range(1,n+2):
          for j in range(1,i):
              string = string + " " + str(count)
              count = count + 1
          print(string)
          string = ""
print floyd(6)

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
#None
