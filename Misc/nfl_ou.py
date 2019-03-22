ou_num = 0
team1 = ""
team2 = ""
tm1spread = 0

ou_num = input("What is the over/under? ")
team1 = input("What is the first team? ")
tm1spread = input("What is that team's spread? ")
team2 = input("What is the second team? ")
ou_num = float(ou_num)
tm1spread = float(tm1spread)
tm2spread = -tm1spread

"""
over/under = tm1score + tm2score
tm1score = tm2score + tm2spread
tm2score = tm1score + tm1spread
over/under = tm1score + tm1score + tm1spread
tm1score = (over/under - tm1spread)/2
tm2score = (over/under - tm2spread)/2
"""
tm1score = (ou_num - tm1spread)/2
tm2score = (ou_num - tm2spread)/2

if tm1score > tm2score:
  print(team1 + " defeats " + team2 + " with a score of " + str(int(tm1score)) + "-" + str(int(tm2score)))
else:
  print(team2 + " defeats " + team1 + " with a score of " + str(int(tm2score)) + "-" + str(int(tm1score)))
