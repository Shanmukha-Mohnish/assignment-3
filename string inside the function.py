

def string_reverse(str):
    rstr=''
    index=len(str)
    while index>0:
        rstr+=str[index-1]
        index=index-1
    return rstr
String=input("enter the string: ")
print(string_reverse(String))







