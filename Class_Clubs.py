print("Class Clubs")

math_class = set(["Aaron", "Lisa", "Devin", "Martha"])
sci_class = set(["Harry", "Devin", "Janice", "Aaron"])

print(f"The following students are members of both Math and Science clubs: ")
for name in math_class.intersection(sci_class):
    print(name)
print()


print(f"The following students are only members of the Math club:")
for name in math_class.difference(sci_class):
        print(name)
print()
print(f"The following students are only members of the Science club:")
for name in sci_class.difference(math_class):
        print(name)
print()
Total = len(math_class.difference(sci_class)) + len(sci_class.difference(math_class))

print(f"Here is the total number of unique students across both clubs: {Total}")
