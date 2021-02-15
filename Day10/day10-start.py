def format_name(f_name, l_name):
    full_name = " ".join([f_name, l_name])
    return full_name.title()


f_name = input("Please introduce your first name: ").lower()
l_name = input("Please introduce your last name: ").lower()
print(format_name(f_name, l_name))
