famous_person = '  albert einstein     '
message = famous_person + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
message = famous_person.lower() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
message = famous_person.upper() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
message = famous_person.title() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
message = famous_person.title().lstrip() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
message = famous_person.title().rstrip() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
message = famous_person.title().strip() + ' ' + 'once said, "A person who never made a \n\tmistake never tried anything new."'
print(message)
