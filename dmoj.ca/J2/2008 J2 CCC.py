playlist = ["A", "B", "C", "D", "E"]
o = 0
x = input()
y = int(input())
while x != '4' and y != '1':
  if x == '1':
    for i in range(y):
      playlist.append(playlist[0])
      playlist.pop(0)
  if x == '2':
    for j in range(y):
      playlist.insert(0, playlist[4])
      playlist.pop(5)
  if x == '3':
    for k in range(y):
      playlist.insert(0, playlist[1])
      playlist.pop(2)   
  x = input()
  y = int(input())

print(*playlist, sep=' ')