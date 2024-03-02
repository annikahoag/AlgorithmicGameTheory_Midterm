
with open('reptocongress2-1.csv') as f:
    reader = f.read()

#List of values in file
data = reader.split(',')

#Setting up 2D array
#Column indices represent ranking
#Row indices represent T. Bond, J.F. Golden, B. Poliquin, Write-In in that order
results = []
for i in range(4):
    col = []
    for j in range(4):
        col.append(0)
    results.append(col)
print(results)

for i in range(5):
    print(data[i])

#Adding values to 1st column
bondCounter=0
for i in range(len(data)):
    if data[i]=='Bond Tiffany':
       bondCounter+=1
    i+=4

print(results)