# --------------------------------------------------------------
#  Gradebook – simplified input (no loops)
# --------------------------------------------------------------

def letter_grade(avg: float) -> str:
    """Map a numeric average to its letter grade."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def main():
    # 1. Student name (single line)
    name = input().strip()                     # e.g.  Jeremiah

    # 2. Five grades on ONE line, separated by spaces
    #    input().split() gives a list of the five strings,
    #    map() converts each to a float.
    grades = list(map(float, input().strip().split()))   # no loop in our code

    # 3. Compute the average
    avg = sum(grades) / 5                         # sum() works on the list

    # 4. Determine the letter grade
    letter = letter_grade(avg)

    # 5. Output exactly as required
    print(name)                                 # student name
    print(f"Average: {avg:.1f}")                # one decimal place
    print(f"Letter Grade: {letter}")            # A/B/C/D/F


if __name__ == "__main__":
    main()