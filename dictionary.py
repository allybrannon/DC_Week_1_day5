# fruits_and_colors = {
#     "orange": "orange",
#     "apple": "red or green",
#     "lemon": "yellow"
# }

# print(fruits_and_colors)

# ally = {
#     "hands": 2,
#     "feet": 2,
#     "arms": 2,
#     "fingers": ["5 left", "5 right"]
# }

# print(ally["fingers"])
# print(ally["fingers"][0])

# hands = ally["fingers"]
# print(hands)

fruits_and_colors = {
    "orange": "orange",
    "apple": "red or green",
    "lemon": "yellow",
    "tomatoes": {
        "fruits": ["some say yes", "some say no"],
        "vegetable": ["others say yes", "others say no"]
    }
}

big_red = fruits_and_colors["tomatoes"]
print(big_red)
big_red["Old 'Mater"] = "more tomatoes"
print(big_red)
# fruits_and_colors["tomatoes"]["People"] = ["Ally", "Alexis", "Watson"]

# loops through and prints keys of dictionary
# for key in fruits_and_colors:
#     print(fruits_and_colors[key])
# print(key)

# print(fruits_and_colors)
# fruits_and_colors["apple"] = "eaten"
# print(fruits_and_colors)

# del fruits_and_colors["tomatoes"]

# print(fruits_and_colors)

# check to see if an item is in the dictionary
# if "orange" in fruits_and_colors:
#     print("Yes!")
# else:
#     print("No oranges!")

# if "cherry" in fruits_and_colors:
#     print("Yes!")
# else:
#     print("No cherries!")
