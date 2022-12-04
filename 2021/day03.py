"""
What is the power consumption of the submarine?
"""
def gamma_rate(report):
    bits = report.replace(" ", "").split("\n")
    ordered = list(map("".join, zip(*bits)))
    return "".join("0" if o.count("0") >= len(bits) // 2 else "1" for o in ordered)


def epsilon_rate(gamma_rate):
    return "".join("1" if bit == "0" else "0" for bit in gamma_rate)


def power_cons(report):
    gamma = gamma_rate(report)
    eps = epsilon_rate(gamma)

    return int(gamma, 2) * int(eps, 2)


if __name__=="__main__":

    report = """00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010"""

    print(power_cons(report))
