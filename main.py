from func import read_file, get_driver_score, active_system, add_regular_race, add_sprint_race
from Race import Race

list_of_all_races = read_file()

while True:
    add_new_race = input("do you want to add new race?")
    if add_new_race == "yes":
        what_race = input("what kind of race? ragil or sprint?")
        if what_race == Race.RAGIL:
            add_regular_race(list_of_all_races)
            continue
        elif what_race == Race.SPRINT:
            add_sprint_race(list_of_all_races)
            continue
        else:
            print("you have to enter ragil or sprint. let's try again")
    elif add_new_race == "no":
        break
    else:
        print("you have two options: yes or no. let's try again")
        continue

print("driver standing:")
get_driver_score(list_of_all_races)
active_system(list_of_all_races)

# while True:
#     add_new_race = input("do you want to add new race?")
#     if add_new_race == "yes":
#         add_race(list_of_all_races)
#         continue
#     elif add_new_race == "no":
#         break
#     else:
#         print("you have two options: yes or no. let's try again")
#         continue



# def first_time_read_drivers_data():
#     all_races = read_race()
#     main_drivers_class = DriverList()
#     main_drivers_class.my_drivers_list = all_races
#     save(main_drivers_class, "races.data")
#
# #starting program - reading from file
# main_drivers_class = load("races.data")
# for race in main_drivers_class.my_drivers_list:
#     print(race)
#
# def first_time_read_teams_data():
#     all_races = read_race()
#     main_teams_class = TeamList()
#     main_teams_class.my_teams_list = all_races
#     save(main_teams_class, "races.data")
#
# #starting program - reading from file
# main_teams_class = load("races.data")
# for race in main_teams_class.my_teams_list:
#     print(race)