"""
Calculate the horizontal position and depth you would have after following
the planned course. What do you get if you multiply your final horizontal
position by your final depth?
"""

def course_stats(course):
    steps = course.replace("  ", "").split("\n")
    pos = 0
    depth = 0

    for step in steps:
        move = int(step.split()[1])
        if step.startswith("f"):
            pos += move
        if step.startswith("d"):
            depth += move
        if step.startswith("u"):
            depth -= move
    return pos, depth


def multiply_stats(course):
    pos, depth = course_stats(course)
    return pos * depth


if __name__=="__main__":

    course = """forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2"""

    print(course_stats(course))
    print(multiply_stats(course))
