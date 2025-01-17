try:
    file = open("a_file.txt")
    a_dictionary= {"Key":"Value"}
    print(a_dictionary)
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made uo.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")