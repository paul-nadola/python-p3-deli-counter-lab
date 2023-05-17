katz_deli = ["Paul", "Jack"]

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            line_status += f" {i}. {person}"
        print(line_status)
# print(line(katz_deli))
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print(serving)
        print(f"Currently serving {serving}.")

print(now_serving(katz_deli))
print(katz_deli)