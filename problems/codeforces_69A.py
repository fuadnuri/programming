n = int(input())
forces = []
for i in range(n):
    inp=input().split()
    x,y,z=int(inp[0]),int(inp[1]),int(inp[2])
    forces.append((x,y,z))

x=0
y=0
z=0

for c in forces:
    x+=c[0]
    y+=c[1]
    z+=c[2]

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")

