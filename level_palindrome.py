
def findLevel(data):
    length_data=len(data)
    level_cnt=0
    if length_data==0:
        return level_cnt
    #if length_data==1:

    ele_front=0
    ele_end=length_data-1

    while ele_front<=ele_end:
        if not(data[ele_front]==data[ele_end]):
            break
        level_cnt+=1
        ele_front+=1
        ele_end-=1
    return level_cnt

if __name__=="__main__":
    string_data=input()
    level_mark="Palindrome is up to {} levels"
    #level_mark+=str(findLevel(string_data))+" levels"
    #Palindrome is up to 5 levels
    print(level_mark.format(str(findLevel(string_data))))
