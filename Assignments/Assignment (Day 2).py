print("==================== Roadmap Provider Project ==================")
exp = input("Enter your experience as Fresher or Experienced: ")
if exp == "Fresher":
    print("You are eligible for following jobs: /n1. Web Developer /n2. Application Developer /3. Machine Learning, Artificial Intelligence, Data Science")
    opt = int(input("Enter your option: "))
    if opt == 1:
        print("You need to learn: \n1. HTML \n2. CSS \n3. JavaScript \n4. Python \n5. Django")
    elif opt == 2:
        print("You need to learn: \nJava + DSA + Build Projects")
    elif opt == 3:
        print("You need to learn: \n1. Python \n2. R \n3. SQL \n4. Mathematics")
    else:
        print("Invalid option selected...!")
elif exp == "Experienced":
    print("You are eligible for following jobs: \n1. Data Analytics \n2. Cloud Computing \n3. Front End Developer")
    opt = int(input("Enter your option: "))
    if opt == 1:
        print("You need to learn: \n1. Python \n2. Excel \n3. Power BI")
    elif opt == 2:
        print("You need to learn: \n1. DevOps \n2. Python for Automation \n3. Cloud Basics (AWS/Azure/GCP)")
    elif opt == 3:
        print("You need to learn: \n1. Python \n2. Django for Backend")
    else:
        print("Invalid option selected...!")
else:
    print("Invalid Input Given...!")


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