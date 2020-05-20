"""
Hey I am Rohan Kulkarni.
Hope this code helps you. Have FUN!!
"""
fact_list=[]
#refactor=10**9+7

#Function here will generate and update the fact_list with factorials
def fact(num):
    global fact_list,refactor
    
    #if request factorial result is already generated and present in the fact_list
    #then simply retrive and return.
    if len(fact_list)>=num:
        print(fact_list[num-1])
        return
    
    #compute and store new factorial results in fact_list
    for index in range(len(fact_list),num):
        fact_list.append([])
        
        #you may want to refactor the result as it may lead to large numbers
        fact_list[index]=(fact_list[index-1]*(index+1))#%refactor
    print(fact_list[num-1])

# the below line represents fact_list[0]=1 and initilizes the global list
fact_list.append(1)

#executation of T test cases
t=int(input())
while t>0:
    t-=1
    num=int(input())
    fact(num)
