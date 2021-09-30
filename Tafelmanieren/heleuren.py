mm = input("Wil je de hele uren van de morgen of middag zien? ").lower()

if mm == "morgen":
    for i in range(0,13):
        print(i,":00 AM")

elif mm == "middag":
    for i in range(0,13):
        print(i,":00 PM")