import replit;
import math;

fileName = "input.txt";

def get_fuel(mass):
  print("mass: " + str(mass));
  needed_fuel = math.floor(mass/3) - 2;
  if needed_fuel <= 0:
    print("needs: 0")
    return 0;
  else:
    print("needs: " + str(needed_fuel));
    return needed_fuel + get_fuel(needed_fuel);

replit.clear();

masses = list();
in_file = open(fileName);
for line in in_file:
  masses.append(int(line));

total = 0;
for mass in masses:
  fuel = get_fuel(mass);
  total += fuel;

print("Total: " + str(total));

