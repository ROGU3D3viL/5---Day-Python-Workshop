print("==================== Certificate Eligibility Checker ==================")
days = int(input("Enter number of days you attended the training: "))
if days == 5:
    for i in range(1, 5):
        print(f"Day {i} Feedback:")
        asgn = input("Was Assignment Done? (Yes/No): ")
        attd = input("Was Attendance Given? (Yes/No): ")
        cam = input("Was Camera On? (Yes/No): ")
        if asgn == "Yes" and attd == "Yes" and cam == "Yes":
            continue
        else:
            print("You are not eligible for the certificate...!")
            break
else:
    print("You are not eligible for the certificate...!")