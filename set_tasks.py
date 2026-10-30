# Задание1
rooms=[205,310,205,412,310,205]
room=set(rooms)
print("Задание 1:")
print(len(room))
print(sorted(room))
print(rooms)
# Задание 2
skills={"python","git"}
skills.add("sql")
skills.add("git")
skills.update(["json","sql"])
skills.discard("java")
skills.remove("git")
print("\nЗадание 2:")
print(skills)
# Задание 3
python_club={"Айдар","Алина","Данияр"}
testing_club={"Алина","Данияр","Мадина"}
print("\nЗадание 3:")
print(sorted(python_club | testing_club))
print(sorted(python_club & testing_club))
print(sorted(python_club - testing_club))
print(sorted(testing_club - python_club))
print(sorted(python_club ^ testing_club))
# Задание 4
def unique_cities(cities):
    result=set()
    for city in cities:
        city=city.strip().casefold()
        if city!="":
            result.add(city)
    return result
print("\nЗадание 4:")
print(sorted(unique_cities(["Алматы", "алматы","Астана",""," "],)))
# Задание 5
def attendance(roster,present):
    roster_set=set(roster)
    present_set=set(present)
    attended=roster_set & present_set
    absent=roster_set - present_set
    guest=present_set - roster_set
    return {"attended": attended, "absent": absent, "guest": guest}
result=attendance(["Айдар","Алина","Данияр","Мадина"],
                  ["Алина","Данияр","Данияр","Ерлан"])
print("\nЗадание 5:")
print("Пришли:", result["attended"])
print("Отсутствуют:", result["absent"])
print("Гости:", result["guest"])
# Задание 6
def compare_checks(before,after):
    before_set=set(before)
    after_set=set(after)
    added=after_set - before_set
    removed=before_set - after_set
    common=before_set & after_set
    return {"added": added, "removed": removed, "common": common}
result=compare_checks(["login","profile","logout","login"],
                      ["login","profile","search","search"])
print("\nЗадание 6:")
print("Добавлены:", result["added"])
print("Удалены:", result["removed"])
print("Общие:", result["common"])
# Задание 7
def can_run(required,available):
    return required.issubset(available)
print("\nЗадание 7:")
required={"python","git"}
available={"python","git","json"}
print(can_run(required,available))
print(can_run({"python","git"},{"python"}))
print(can_run(set(), set()))
print(can_run(set(), {"python","git"}))
# Задание 8
def duplicate_ids(ids):
    seen=set()
    repeated=set()
    for id in ids:
        if id in seen:
            repeated.add(id)
        seen.add(id)
    return repeated
print("\nЗадание 8")
print(duplicate_ids([1,4,1,7,4,4,9]))
print(duplicate_ids([]))
print(duplicate_ids([5]))
print(duplicate_ids([5,5,5]))
# Задание 9
def unique_in_order(values):
    seen=set()
    result=[]
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result
print("\nЗадание 9")
print(unique_in_order(["git","python","git","json","python"]))
print(unique_in_order([]))
print(unique_in_order(["git","git"]))