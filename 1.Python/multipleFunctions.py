class MultipleFunctions:
    def ageCategory():
            if(age<18):
                print("Children")
                cate="Children"
            elif(age<35):
                print("Adult")
                cate="Adult"
            elif(age<59):
                print("Citizen")
                cate="Citizen"
            else:
                print("Senior Citizen")
                cate="Senior Citizen"
            return cate
            age=int(input("Enter the age:"))
    def oddEven():
            num=int(input("Enter the number:"))
            if((num%2)==0):
                print("Even number")
                message="Even number"
            else:
                print("Odd number")
                message="Odd number"
            return message
    def BMI():
            index=int(input("Enter the BMI Index:"))
            print("Enter the BMI Index:",index)
            if(index<18):
                print("Under weight")
            elif(index<24):
                print("Normal")
            elif(index<33):
                print("Overweight")
            else:
                print("Very Overweight")