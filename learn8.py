"""
def describe_pet(pet_name, animal_type='dog'):

    print("\nI have a " + animal_type + ".")

    print("My " + animal_type + "‘s name is " + pet_name.title() + ".")


# describe_pet(pet_name='willie', animal_type='cat')

describe_pet(pet_name='willie')
"""


'''
def make_shirt(size, chara):

    print(f"Your shirt's size is {size}")

    print(f"There is {chara} on your shirt")


make_shirt('180', 'Nike')
'''

'''
def get_formatted_name(first_name, last_name):

    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
'''

'''
def build_person(first_name, last_name):

    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
'''

'''
def city_country(capital, country):

    cap_coun = capital + "," + country
    return cap_coun.title()


cap = city_country('beijing', 'china')
print(cap)
'''


def make_album(name, album, album_num=''):

    if album_num:
        mk_al = {'name': name, 'album': album, 'album_num': album_num}
    else:
        mk_al = {'name': name, 'album': album}
    return mk_al


'''
mk_als1 = make_album('shizhewen1', 'nihao1',3)
mk_als2 = make_album('shizhewen2', 'nihao2')
mk_als3 = make_album('shizhewen3', 'nihao3')
print(mk_als1, mk_als2, mk_als3)
'''

while True:
    print(f"Please input the Informations:")
    print(f"Press 'q' to quit!")

    s_name = input("Singer name:")
    if s_name == 'q':
        break

    album_name = input("Album:")
    if album_name == 'q':
        break

    mk_als = make_album(s_name, album_name)
    print(mk_als)
