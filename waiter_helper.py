# Starters
starters = ["nuggets", "ribs", "fish_fingers"]
# Main
mains = ["steak", "fish", "lamb"]
# Dessert
dessert = ["icecream", "cookie", "cake"]

print("Hi, how can I help? This is our menu: \n"
      + "Starters: \n" + str(starters)
      + "\nMains: \n" + str(mains)
      + "\nDesserts: \n" + str(dessert) + "\nWhat starter would you like?")

starter_input = input()
print("Ok, so: " + starter_input + ".\nWhat main course would you like?")

main_input = input()
print(main_input + " added, to the list. What dessert would you like?")

dessert_input = input()
print("Perfect. So here's your order:\n" + starter_input + "\n"
      + main_input + "\n"
      + dessert_input + "\nIs that correct?")
