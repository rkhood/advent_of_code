def read_masses(filename='data/day01.txt'):
    with open(filename) as f:
        masses = f.read().strip().split('\n')
    return masses


def fuel_required_by_mass(mass):
    return (mass // 3) - 2


def fuel_required_by_fuel(mass):
    fuel = fuel_required_by_mass(mass)
    if fuel <= 0:
        return 0
    return fuel + fuel_required_by_fuel(fuel)


if __name__ == '__main__':

    fuel_req_by_mass = sum(fuel_required_by_mass(int(mass)) for mass in read_masses())
    fuel_req_by_fuel = sum(fuel_required_by_fuel(int(mass)) for mass in read_masses())


