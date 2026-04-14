height = 5

for i in range(1, height + 1):
    # leading spaces
    for j in range(height - i):
        print("  ", end="")
    
    # spaces between stars
    for k in range(i):
        print("* ", end="") # used two spaces for allignment
    
    print()  # move to next line