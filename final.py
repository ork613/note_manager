user_name = input("имя пользователя")
print("имя пользователя:", user_name)
title = input("заголовок заметки")
print("заголовок заметки:", title)
content = input("описание заметки")
print("описание заметки:", content)
status = input("статус заметки")
print("статус заметки:", status)
temp_created_date = input("день-месяц-год")
print("Дата создания:", temp_created_date)
temp_issue_date = input("день-месяц-год")
print("Дата изменения:", temp_issue_date)

title1 = input("заголовок заметки1")
print("заголовок заметки1:", title1)
content1 = input("описание заметки1")
print("описание заметки1:", content1)
status1 = input("статус заметки1")
print("статус заметки1:", status1)
title2 = input("заголовок заметки2")
print("заголовок заметки2:", title2)
content2 = input("описание заметки2")
print("описание заметки2:", content2)
status2 = input("статус заметки2")
print("статус заметки2:", status2)
title3 = input("заголовок заметки3")
print("заголовок заметки3:", title3)
content3 = input("описание заметки3")
print("описание заметки3:", content3)
status3 = input("статус заметки3")
print("статус заметки3:", status3)

note = {"имя пользователя": user_name,
        "заголовок заметки": title ,
        "описание заметки": content,
        "статус заметки": status,
        "Дата создания": temp_created_date,
        "Дата изменения": temp_issue_date,
        "заголовок заметки1": title1,
        "заголовок заметки2": title2,
        "заголовок заметки3": title3
}
print(note)