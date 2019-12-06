def calculate_orbits(filename='data/day06.txt'):
    with open(filename) as f:
        orbit_map = dict(reversed(line.strip().split(")")) for line in f)

    def count_orbits(orbit, k=None):
        orbits = [orbit[0]]
        if orbit_map.has_key(orbit[1]):
            orbits.extend(
                    count_orbits(
                        (orbit[1], orbit_map[orbit[1]]),
                        k if k else orbit[0]
                        )
                    )
        return orbits

    return {orbit[0]: count_orbits(orbit) for orbit in orbit_map.items()}

if __name__ == '__main__':

    orbits = calculate_orbits()

    print(sum([len(o) for o in orbits.values()]))
    print(len(set(orbits['YOU']) ^ set(orbits['SAN'])) - 2)
