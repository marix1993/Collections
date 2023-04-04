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
