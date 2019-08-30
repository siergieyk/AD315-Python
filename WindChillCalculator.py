#"A Chill Wind Blows" was written by Siergiey Kolisnichenko on 10/22/2017.
print("\t\t   A Chill Wind Blows")#In this line I put title of my table. I used "\t" in order to push the title towards the center.
print("")#I used this line a spacer, to make my program more visible.
print("     Temp|",end="")#In this line created temperature prefix for my columns.
for columns in range(-20,70,10):#In this line I created range headers.

    print("%3dF|"%columns, end="")#In this line I created column headers, with width of 4 characters. 3 standard characters and an "F" for temperature
print("")#In order to start a new line.
print ("WindSpeed|--------------------------------------------|")#I created this line, in order to create rows header, and a separater for column headers.
#Here I'm starting my for loop.
for windSpeed in range(0,55,5):#here I created range for my rows (wind speeds).
    print(" %4d mph|"%windSpeed, end="")#Here I established size of the cell for rows at 4 characters, and added "mph".
    
    for temperature in range(-20,70,10): #Here I had to redefine range for temperatures.
        print("%4d|"%(35.74+0.6215*temperature-35.75*windSpeed**(0.16)+0.4275*temperature*windSpeed**(0.16)),end="") #Here I combined wind speed and temperatures in a formula in order to calculate wind chill.
    print()
print("   ----------------------------------------------------")#Here I added a bottom cover to the table.
