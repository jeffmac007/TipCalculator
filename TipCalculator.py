# TipCalculator.py - Beginner functions + math

def tip_amount(bill, percent):
    return bill * (percent / 100)


def total_with_tip(bill, percent):
    return bill + tip_amount(bill, percent)


def per_person(total, people):
    if people <= 0:
        raise ValueError("People must be at least 1.")
    return total / people


def read_float(prompt):
    while True:
        raw = input(prompt).strip().replace("$", "")
        try:
            value = float(raw)
            if value < 0:
                print("Enter a number that is 0 or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("Please enter a whole number of 1 or more.")


def play():
    print("Tip Calculator\n")
    bill = read_float("Bill amount: $")
    percent = read_float("Tip percent (e.g. 18): ")
    people = read_int("Split between how many people? ")

    tip = tip_amount(bill, percent)
    total = total_with_tip(bill, percent)
    share = per_person(total, people)

    print("\n--- Results ---")
    print(f"Tip:   ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Each:  ${share:.2f}")


def main():
    while True:
        play()
        again = input("\nCalculate another? (y/n): ").strip().lower()
        if again != "y":
            print("Done — thanks!")
            break
        print()
    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
