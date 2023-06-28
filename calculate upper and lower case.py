def string_test(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
    print("No. of upper case characters: ",upper_case)
    print("No. of lower case characters: ",lower_case)
String=input("enter the string: ")   
string_test(String)    
  







