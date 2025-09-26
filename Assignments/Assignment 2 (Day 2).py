print("==================== Certificate Eligibility Checker ==================")
days = int(input("Enter number of days you attended the training out of 5: "))
if days == 5:
    for i in range(1, 5 + 1):
        print(f"Day {i} Feedback:")
        asgn = input("Was Assignment Done? (Yes/No): ")
        attd = input("Was Attendance Given? (Yes/No): ")
        cam = input("Was Camera On? (Yes/No): ")
        print("---------------------------------------------------")
        if asgn == "Yes" and attd == "Yes" and cam == "Yes":
            if i == 5:
                print("You are eligible for the certificate...!")
                break
            else:
                continue
            
        else:
            print("You are not eligible for the certificate...!")
            break
elif days < 5:
    print("You are not eligible for the certificate...!")
else:
    print("Wrong Input Given...!")