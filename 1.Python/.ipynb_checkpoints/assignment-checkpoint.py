class Assignment:
    def subfields():
        subfields1 = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for field in subfields1:
            print(field)

    def oddEven():
        num = int(input("Enter a number: "))
        print("Enter a number:", num)
        if (num % 2) == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")

    def eligible():
        gender = input("Your Gender: ")
        print("Your Gender:", gender)
        age = int(input("Your Age: "))
        print("Your Age:", age)
        if gender.lower() == "male" and age >= 21:
            print("ELIGIBLE")
        elif gender.lower() == "female" and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        s1 = int(input("Subject1 = "))
        print("Subject1 =", s1)
        s2 = int(input("Subject2 = "))
        print("Subject2 =", s2)
        s3 = int(input("Subject3 = "))
        print("Subject3 =", s3)
        s4 = int(input("Subject4 = "))
        print("Subject4 =", s4)
        s5 = int(input("Subject5 = "))
        print("Subject5 =", s5)

        total = s1 + s2 + s3 + s4 + s5
        print("Total =", total)

        percent = (total / 500) * 100
        print("Percentage =", percent)

    def triangle():
        height = int(input("Height: "))
        print("Height:", height)
        breadth = int(input("Breadth: "))
        print("Breadth:", breadth)

        print("Area formula: (Height * Breadth)/2")
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

        height1 = int(input("Height1: "))
        print("Height1:", height1)
        height2 = int(input("Height2: "))
        print("Height2:", height2)
        breadth = int(input("Breadth: "))
        print("Breadth:", breadth)

        print("Perimeter formula: Height1 + Height2 + Breadth")
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle:", perimeter)
