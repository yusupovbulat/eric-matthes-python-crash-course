def make_great(magician):
    print('Great ' + magician.title())


def show_magicians(magicians):
    for magician in magicians:
        make_great(magician)
magicians = ['alice', 'bob', 'carol', 'dave']
show_magicians(magicians)
