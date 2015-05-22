#number of characters of numbers from one to one thousand
#i solved the problem using another method, but this one in the forums was more effective

digits = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"
,7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"
,12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen"
,16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"
,20:"twenty",30:"thirty",40:"forty",50:"fifty"
,60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

for i in range(1,1000):
    if(not i in digits.keys()):
        if(i<100):
            digits[i]=digits[i/10*10]+digits[i%10]

        else:
            digits[i]=digits[i/100]+"hundred"
            if(i%100):
                digits[i]+="and"+digits[i%100]
digits[1000]="onethousand"
total=0;

for i in digits.values():
    total+=len(i)
print total