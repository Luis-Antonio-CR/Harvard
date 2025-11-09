people = [
    {"name": "Asta", "squad": "Black Bulls"},
    {"name": "Yuno", "squad": "Golden Dawn"},
    {"name": "Noelle", "squad": "Black Bulls"},
    {"name": "Mimosa", "squad": "Golden Dawn"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)