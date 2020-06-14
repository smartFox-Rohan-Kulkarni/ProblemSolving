from difflib import SequenceMatcher

def common(s1, s2):
    t_s1=""
    t_s2=""
    for ele in s1:
        if ele in s2:
            t_s1+=ele
    for ele in s2:
        if ele in s1:
            t_s2+=ele
    return t_s1,t_s2

def findSub(s1, s2):
    s1,s2=common(s1, s2)
    print(s1, s2)
    pat = SequenceMatcher(None, s2, s1).find_longest_match(0, len(s2), 0, len(s1))
    res=s1[pat.b: pat.b + pat.size]
    return (len(res), res)

if __name__=="__main__":
    string_1=input()
    string_2=input()
    output= "Larger Common Substring length is {} and substring is '{}'"
    res=findSub(string_1, string_2)

    print(output.format(res[0], res[1]))
