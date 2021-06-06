initial_total = float(input("Total bill amount? "))
quality_of_service = input("Was service good, fair or bad? ")
split = int(input("Split how many ways? "))
if quality_of_service == "good":
    good_tip = initial_total * .20
    total_amount = initial_total + good_tip
    total_after_split = total_amount / split
    print("Tip amount: $%.2f" % good_tip)
    print("Total amount: $%.2f" % total_amount)
    if split > 1:
        print("Amount per person: $%.2f" % total_after_split)
elif quality_of_service == "fair":
    fair_tip = initial_total * .15
    total_amount = initial_total + fair_tip
    total_after_split = total_amount / split
    print("Tip amount: $%.2f" % fair_tip)
    print("Total amount: $%.2f" % total_amount)
    if split > 1:
        print("Amount per person: $%.2f" % total_after_split)
elif quality_of_service == "bad":
    bad_tip = initial_total * .10
    total_amount = initial_total + bad_tip
    total_after_split = total_amount / split
    print("Tip amount: $%.2f" % bad_tip)
    print("Total amount: $%.2f" % total_amount)
    if split > 1:
        print("Amount per person: $%.2f" % total_after_split)