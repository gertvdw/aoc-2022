"""
Quick and dirty.

"""

with open("inputs/day8.txt") as f:
  rows = [line.strip() for line in f.readlines()]

width = len(rows[0])
height = len(rows)

display = rows[:]
edgeTrees = 2*width + 2*(height-2)
visibleFromEdge = 0

def scenic_scores(scenery):
    scores = []
    scoremap = [[0 for x in range(len(scenery[0]))] for y in range(len(scenery))]
    for i in range(width):
        for j in range(height):
            column = [c[j] for c in scenery]
            c = (column[0:i][::-1], column[i+1::], scenery[i][0:j][::-1], scenery[i][j+1::])
            score = 1
            for whatever in c:
                if len(whatever) > 0:
                    tf = [w >= scenery[i][j] for w in whatever]
                    if True in tf:
                        score *= (tf.index(True) + 1)
                    else:
                        score *= len(tf)
                else:
                    score *= 0
            scores.append(score)
            scoremap[i][j] = score
    print(max(scores))
    return scoremap

for y in range(1, height-1):
  for x in range(1, width-1):
    tree = int(rows[y][x])
    blockingFromLeft = ["{0},{1}".format(i, y) for i in range(0,x) if int(rows[y][i]) >= tree]
    blockingFromRight = ["{0},{1}".format(i, y) for i in range(x+1,width) if int(rows[y][i]) >= tree]
    blockingFromTop = ["{0},{1}".format(x, i) for i in range(0, y) if int(rows[i][x]) >= tree]
    blockingFromBottom = ["{0},{1}".format(x, i) for i in range(y+1,height) if int(rows[i][x]) >= tree]

    if len(blockingFromLeft) == 0 or len(blockingFromRight) == 0 or len(blockingFromTop) == 0 or len(blockingFromBottom) == 0:
      visibleFromEdge = visibleFromEdge + 1
      display[y] = display[y][:x] + "#" + display[y][x+1:]
    else:
      display[y] = display[y][:x] + " " + display[y][x+1:]

print("Visible from edge: %d" % visibleFromEdge)
print("Around the edge: %d" % edgeTrees)
print("Total: %d" % (visibleFromEdge + edgeTrees))

for line in display:
  print(line)

scores = scenic_scores(rows)

# Uncomment this to show a useless heatmap
# import seaborn
# import matplotlib.pyplot as plt
# heatmap = seaborn.heatmap(data = scores)
# plt.show()