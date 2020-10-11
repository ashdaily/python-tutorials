string1 = "abc[]&&('&('&1234"

# print(string1)

long_string = """abcdedfghijklmabcdedfghi
jklmabcdedfghijklmabcdedfghijklmabcde
dfghijklmabcdedfghijklmabcdedfghijklma
bcdedfghijklmabcdedfghijklmabcdedfghij
klmabcdedfghijklmabcdedfghijklmabcdedf
ghijklmabcdedfghijklmabcdedfghijklmab
cdedfghijklm"""

print(long_string)

long_string = ("abcdedfghijklmabcdedfghijklmabcdedfg"
            "hijklmabcdedfghijklmabcdedfghijklma"
            "bcdedfghijklmabcdedfghijklmabcdedfgh"
            "ijklmabcdedfghijklmabcdedfghijklmabcde"
            "dfghijklmabcdedfghijklmabcdedfghijklm"
            "abcdedfghijklmabcdedfghijklmabcdedfghijklm")

print(long_string)


# strings are iterable
name = "jklmabcdedfghijklmabcde"
for i in name:
    print(i)

# you can use indexing / slicing on strings
name[0] # will give you first char of the name variable
name[-1] # will give you last char of the name variable
name[0:5] # give you name char from 0th index to 4th index

len(name) # gives you length of string (len can also be used on list)


name = " abdce    "
name.strip() # will remove spaces from left and right only not from middle
name.lstrip()
name.rstrip()


name = "tShauryat"
name.strip("t")
name.lstrip("t")


name.lower() # Shaurya become shaurya
name.upper() # Shaurya become SHAURYA

"s" in name # give you boolean checking "s" in name, gives true if "s exists in name
"s" not in name 


first_name = "Rishab"
last_name = "Yadav"

#concatenation (fancy name for adding two strings)
first_name + last_name
first_name + " " + last_name


# string formatting
name = "Amit"

greeting = f"Hello {name}"
"I want {} pieces of item {} for {} dollars.".format(2, "bread", 10)
















