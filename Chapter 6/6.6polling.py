favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['sarah', 'bob', 'adam']

for name in names:
    if name in favourite_languages.keys():
        print(name + ", thanks for responding.")
    else:
        print(name + ", welcome to take the poll.")
