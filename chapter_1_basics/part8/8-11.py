magicians = ['alice', 'bob', 'carol', 'dave']
after_great = []


def make_great(magicians):
    while magicians:
        current_magician = magicians.pop()
        print('Great ' + current_magician.title())
        after_great.append(current_magician)


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


make_great(magicians[:])
show_magicians(magicians)
show_magicians(after_great)
