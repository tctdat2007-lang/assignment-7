seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("Enter the number of a month (1-12): "))
if month in (10, 11, 12):
    season = seasons[0]
elif month in (1, 2, 3):
    season = seasons[1]
elif month in (4, 5, 6):
    season = seasons[2]
elif month in (7, 8, 9):
    season = seasons[3]
else:
    season = "Invalid month number."

print(f"The season is: {season}")
