# Millionaire
- Millionaire list
```
millionaire_list = ["yacht", "house", "plane", "bugatti", "football club"]

print(millionaire_list)
print(type(millionaire_list))
print(millionaire_list[0])
print(millionaire_list[1])
print(millionaire_list[-1])

millionaire_list[0] = "Ferrari"
millionaire_list[2] = "helicopter"
print(millionaire_list)

millionaire_list.append("school")
print(millionaire_list)

millionaire_list.remove("bugatti")
print(millionaire_list)

millionaire_list.pop()
print(millionaire_list)
```
# Waiter_helper

-  Starters
```
starters = ["nuggets", "ribs", "fish_fingers"]
```
- Main
```
mains = ["steak", "fish", "lamb"]
```
-  Dessert
```
dessert = ["icecream", "cookie", "cake"]
```
- Print
```
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
```
# Hero story

- Story
```
story_1 = {
    "start": "Beginning of a Hero Story.",
    "middle": "Heroes actions and tasks.",
    "end": "Happy ending."
}
```
- Print
```
print(story_1)
print((type(story_1)))
print(story_1.keys())
print(story_1.values())

print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

story_1.update({
    "hero": "yourSuperHero"
})
print(story_1)
```
