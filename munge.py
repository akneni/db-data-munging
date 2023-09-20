# Place code below to do the munging part of this assignment.


with open("./data/raw_data.txt", 'r') as f:
    data = f.read()

# Each relevent row starts with a year, so we'll 
# split the stata by '\n' and only use rows that start with 4 numbers
data = data.split("\n")
include_heading = True
lst = []
for line in data:
    line = line.strip()

    # Only add the relevent lines
    if (line == "") or (not line[:4].isdigit()):
        if (line[:4] == 'Year') and include_heading:
            include_heading = False
        else:
            continue

    # Replace all whitespace with a single space
    while ('  ' in line):
        line = line.replace('  ', ' ')
    
    # Append them to the list lst
    lst.append(line.split())


# Now, we need to deal with missing values that are denoted by '*'
# We will fill them with "NaN" for now and then ignore them when analyzing data

for sublst in lst:
    for i, elem in enumerate(sublst):
        if '*' in elem:
            sublst[i] = 'NaN'


# Covert Centicelcius into farenheight
for i in range(1, len(lst)): # skip the header row
    sublist = lst[i]

    for j in range (1, len(sublist)-1): # Skip the two year columns
        if sublist[j] != 'NaN':
            sublist[j] = round(((float(sublist[j]) / 100) * 1.8), 1) # convert units
            sublist[j] = str(sublist[j]) # turn it back into a string for the .join() method



# Now we save the cleaned data to a file called clean_data.csv

lst = [','.join(i) for i in lst]
lst = '\n'.join(lst)

with open('./data/clean_data.csv', 'w') as f:
    f.write(lst)







