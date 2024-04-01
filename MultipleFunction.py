class MultiFunction():
    def AISubfields(): 
        list=["Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        for list1 in list:
            print(list1)

    def OddEven():    
        Num=int(input("Enter the Number:"))
        if(Num%2==0):
            print(Num,"is Even Number")
        else:
            print(Num,"is Odd Number")

    def EligibilityforMarriage():
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:"))
        if (gender=="male" and age>21):
            print("Eligible")
        elif(gender=="female" and age>18):
            print("Eligible")
        else:
            print("Not Eligible")

    def Percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        percentage=Total/500*100
        per=print("Percentage:",round(percentage,2))
        return per

    def Triangle():
        Height=float(input("Height:"))
        Breadth=float(input("Breath:"))
        Area=Height*Breadth/2
        print("Area of Triangle:",Area)
        Height1=float(input("Height1:"))   
        Height2=float(input("Height2:"))
        Breadth=float(input("Breath:"))
        perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle:",perimeter)





