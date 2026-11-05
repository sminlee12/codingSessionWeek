def is_passing(score):
    if (score>=60):
        return True
    else:
        return False

number =int(input("Type any number"))
isOversixty = is_passing(number)

print(str(isOversixty))