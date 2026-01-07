
#extend ()extend method
num =[1,2,3,4]
num2 =[5,8,9,7,"abcd"]
num.extend(num2)
print(num)

# insert() insert method 
num.insert(2,22)
print(num)


# remove() remove first occurance of value , we have specified

num1= [1,4,2,4,2,3,4]
num1.remove(2)
print(num1)

#pop will remove last element even we dont specify it . If we specify than it will delete indexvalue

no=["apple",1,4,5,5,7]
no.pop()
print(no)


#clear() method remove empty list

no1=[4,7,8,9,10]
no.clear()
print(no)





#index()  method will give index valur of first occurance
no2 = [1,7,7,8,5,9,6]
print(no2.index(7))


#count() method  will count the element of list 
count1=[1,1,1,1,1,1,1,2,3,5,4]
print(count1.count(1))



#sort() sorting elements in asc or desc order
val=[4,9,8,7,0,4,8,9]
val.sort()
print(val)


  # tuples  are used to collection of the data
numbers = (7,9,4,5,2,3)
print(numbers)
numbers[2] = 10

print(numbers)