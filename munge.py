# Place code below to do the munging part of this assignment.


with open("./data/raw_data.txt", 'r') as f:
    data = f.read()

# Each relevent row starts with a year, so we'll 
# split the stata by '\n' and only use rows that start with 4 numbers
data = data.split("\n")
lst = []
for line in data:
    line = line.strip()
    if (line == "") or (not line[:4].isdigit()):
        continue

    # Replace all whitespace with a single space
    while ('  ' in line):
        line = line.replace('  ', ' ')
    
    # Append them to the list lst
    lst.append(line.split())


# Now, we need to deal with missing values that are denoted by '*'
# We will fill them in with a zero for now

for sublst in lst:
    for i, elem in enumerate(sublst):
        if '*' in elem:
            sublst[i] = '0'



# Now we save the cleaned data to a file called clean_data.csv

lst = [','.join(i) for i in lst]
lst = '\n'.join(lst)

with open('./data/clean_data.csv', 'w') as f:
    f.write(lst)







