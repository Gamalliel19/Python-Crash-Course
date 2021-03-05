# import datetime

# def get_event_date(event):
#     return event.date

# def current_users(events):
#     events.sort(key=get_event_date)
#     machines = {}
#     for event in events:
#         if event.machine not in machines:
#             machines[event.machine] = set()
#         if event.type == "login":
#             machines[event.machine].add(event.user)
#         elif event.type == "logout":
#             machines[event.machine].remove(event.user)
#         elif event.type == "logout" and event.user in machines[event.machine]:
#             machines[event.machine].remove(event.user)
#     return machines

# def generate_report(machines):
#     for machine, users in machines.items():
#         if len(users) > 0:
#             user_list = ", ".join(users)
#             print("{}: {}".format(machine, user_list))


# class Events:
#     def __init__(self, event_date, event_type, machine_name, user):
#         self.date = event_date
#         self.type = event_type
#         self.name = machine_name
#         self.user = user

# events = [
#     {'2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'},
#     {'2020-01-21 18:45:56', 'logout', 'webserver.local', 'jordan'},
#     {'2020-01-21 13:45:56', 'login', 'myworkstation.local', 'nadiem'},
#     {'2020-01-21 19:45:56', 'logout', 'mailserver.local', 'nadiem'},
#     {'2020-01-21 10:45:56', 'login', 'webserver.local', 'alam'},
#     {'2020-01-21 15:45:56', 'logout', 'myworkstation.local', 'alam'},
# ]

# users = current_users(events)
# print(users)

# generate_report(users)


# def max_number(number1, number2):
#     if number1 > number2:
#         return number1 
#     return number2
# print(max_number(1, 2))


# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)



# name = 'I will be a very successful person in bangkit and reached my dreams'
# print(name.upper())
# alphabet = []
# huruf = 'a'
# for i in range(0, 26): 
#     test_list.append(huruf) 
#     alpha = chr(ord(huruf) + 1) 

# print ("List after insertion : " + str(test_list))

# dicts = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdicts)


class Binatang:
    nama = ""
    suara = ""

serigala = Binatang()
serigala.nama = "Beruang"
serigala.suara = "AWOOOOOO"

print(serigala)