# Travel Itinerary Program

destinations = []

print("Please enter your 5 travel destinations:")

# Input 5 destinations
for i in range(1, 6):
    place = input("Destination " + str(i) + ": ")
    destinations.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(str(i + 1) + ". " + destinations[i])

print("\nLet's update your 2nd and 5th destinations.")

# Update 2nd destination
new_second = input("Enter a new destination for #2: ")
destinations[1] = new_second

# Update 5th destination
new_fifth = input("Enter a new destination for #5: ")
destinations[4] = new_fifth

print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(str(i + 1) + ". " + destinations[i])
