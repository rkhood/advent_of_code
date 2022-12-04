"""
Count the number of times a depth measurement increases
"""

def num_increases(report):
    depths = report.split()
    return sum(d2 > d1 for d1, d2 in zip(depths, depths[1:]))


if __name__=="__main__":

    report = """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
    """

    print(num_increases(report))
