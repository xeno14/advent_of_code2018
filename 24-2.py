import re
import pprint
from typing import List


class Group:

    def __init__(self, units: int, hp: int, power: int, attr: str, init: int, weak: list, immune: list):
        self.units = units
        self.hp = hp
        self.attr = attr
        self.power = power
        self.weak = weak
        self.immune = immune
        self.init = init

    def __str__(self):
        return r"{} units each with {} hit points (weak {}; immune {}) with an attack that does {} {} damage at initiative {}".format(
            self.units, self.hp, self.weak, self.immune, self.power, self.attr, self.init
        )

    def __repr__(self):
        return str(self)

    def effective_power(self):
        return self.units * self.power


def parse_line(line: str) -> Group:
    pattern = r"(\d+) units each with (\d+) hit points \((.+)\) with an attack that does (\d+) (.+) damage at initiative (\d+)"
    matched = re.search(pattern, line)
    if matched is None:
        pattern = r"(\d+) units each with (\d+) hit points with an attack that does (\d+) (.+) damage at initiative (\d+)"
        matched = re.search(pattern, line)
        (units, hp, power, attr, init) = matched.groups()
        weak_immune = ""
    else:
        (units, hp, weak_immune, power, attr, init) = matched.groups()
    # print(matched.groups())

    immune = []
    weak = []
    if weak_immune != "":
        for x in weak_immune.split(";"):
            x = x.strip()
            if x.startswith("immune to "):
                immune = [
                    i.strip() for i in x[len("immune to "):].split(",")
                ]
            elif x.startswith("weak to"):
                weak = [
                    i.strip() for i in x[len("weak to "):].split(",")
                ]
    g = Group(units=int(units), hp=int(hp), power=int(power), attr=attr, init=int(init), weak=weak, immune=immune)
    return g


def parse_file(filename):
    with open(filename) as f:
        txt = f.read()

    immune_txt, infection_txt = [x.strip() for x in txt.split("\n\n")]

    immunes = [
        parse_line(line) for line in immune_txt.split("\n")[1:]
    ]
    infections = [
        parse_line(line) for line in infection_txt.split("\n")[1:]
    ]
    return immunes, infections


def calc_damage(attacker: Group, defender: Group) -> int:
    if attacker.attr in defender.immune:
        factor = 0
    elif attacker.attr in defender.weak:
        factor = 2
    else:
        factor = 1
    return attacker.effective_power() * factor


def select_targets(attackers: List[Group], defenders: List[Group]):
    targets = dict()

    attacker_indices = [(a.effective_power(), a.init, i) for i, a in enumerate(attackers)]
    attacker_indices = sorted(attacker_indices, key=lambda x: tuple(x[:-1]), reverse=True)

    seen = set()
    for _, _, i in attacker_indices:
        damages = [(calc_damage(attackers[i], d), d.effective_power(), d.init, j)
                   for j, d in enumerate(defenders)]
        damages = sorted(damages, reverse=True, key=lambda x: tuple(x[:-1]))
        # print("damages", damages)
        for damage, _, _, j in damages:
            if damage == 0:
                continue
            if j not in seen:
                targets[i] = j
                seen.add(j)
                break
    return targets


def attack_order(immunes: List[Group], infections: List[Group]):
    order = [("immune", i, g.init) for i, g in enumerate(immunes)]\
            + [("infection", i, g.init) for i, g in enumerate(infections)]
    order = sorted(order, key=lambda x: x[-1], reverse=True)
    order = [(tag, i) for tag, i, _ in order]  # remove init
    return order


def combat(immunes: List[Group], infections: List[Group]):
    immune_to_infection = select_targets(immunes, infections)
    infection_to_immune = select_targets(infections, immunes)
    order = attack_order(immunes, infections)

    for tag, idx in order:
        if tag == "immune":
            if idx not in immune_to_infection:
                continue
            attacker = immunes[idx]
            target_idx = immune_to_infection[idx]
            defender = infections[target_idx]
        else:
            if idx not in infection_to_immune:
                continue
            attacker = infections[idx]
            target_idx = infection_to_immune[idx]
            defender = immunes[target_idx]

        damage = calc_damage(attacker, defender)
        kills = min(damage // defender.hp, defender.units)
        # print("{} {} -> {} damages {} kills {}".format(tag, idx+1, target_idx+1, damage, kills))
        # print(tag, idx+1, attacker.effective_power(), attacker.units, attacker.power)

        defender.units -= kills

    # remove dead group
    immunes = [g for g in immunes if g.units > 0]
    infections = [g for g in infections if g.units > 0]
    return immunes, infections


def total_units(l: List[Group]):
    return sum([x.units for x in l])


def simulate(filename, boost):
    immunes, infections = parse_file(filename)

    for i in range(len(immunes)):
        immunes[i].power += boost

    while len(immunes) > 0 and len(infections) > 0:
        nim = total_units(immunes)
        nin = total_units(infections)

        immunes, infections = combat(immunes, infections)

        # abort infinite loop
        if nim == total_units(immunes) and nin == total_units(infections):
            return [], []

    return immunes, infections


def main():
    filename = "input/24.txt"

    boost = 0
    while True:
        print(boost)
        immunes, infections = simulate(filename, boost)
        if len(immunes) > 0:
            break
        boost += 1

    print("immune", total_units(immunes))
    print("infections", total_units(infections))


if __name__ == '__main__':
    main()