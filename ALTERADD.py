#Chef has 2 numbers A and B (A<B).
#
#Chef will perform some operations on A.
#
#In the ith operation:
#
#Chef will add 1 to A if i is odd.
#Chef will add 2 to A if i is even.
#Chef can stop at any instant. Can Chef make A equal to B?
#
#Input Format
#The first line contains a single integer T — the number of test cases. Then the test cases follow.
#The first and only line of each test case contains two space separated integers A and B.
#Output Format
#For each test case, output YES if Chef can make A and B equal, NO otherwise.
#
#Note that the checker is case-insensitive. So, YES, Yes, yEs are all considered same.
#
#Constraints
#1≤T≤1000
#1≤A<B≤109
#Sample Input 1 
#4
#1 2
#3 6
#4 9
#10 20
#Sample Output 1 
#YES
#YES
#NO
#YES
#Explanation
#Test case 1: Chef may perform one operation to make A equal to B: 1−→+12
#Test case 2: 3-->+1−→4-->+2−→6
#Test case 3: It can be shown that it is impossible to make A and B equal.
#
#Test case 4: 10-->+1−→11-->+2−→13-->+1−→14-->+2−→16-->+1−→17-->+2−→19-->+1−→20


t=int(input())
while(t):
    a,b=map(int,input().split())
    m=b-a
    if(m%3==0 or m%3==1):
       print("YES")
    else:
        print("NO")
    t-=1
