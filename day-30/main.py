# # FileNotFound
# try:
#     # This line of code can cause an error
#     file = open("a_file.txt")
#     a_dicionary = {"key": "value"}
#     print(a_dicionary["key"])
# # if there was an exception, do something different
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
#
# # This line execute when the thing that you're trying all succeeds in try block
# else:
#     content = file.read()
#     print(content)
#
# # Run no matter what happens
# finally:
#     raise TypeError("This is an error that i made up.")
# # KeyError
# # a_dicitionary = {"key": "value"}
# value = a_dicitionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)