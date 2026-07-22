print("Enter the marks obtained in 4 subjects:")
math=int(input("math:"))
english=int(input("english:"))
science=int(input("science:"))
history=int(input("history:"))

sum=math+science+english+history
print("sum of math, english,science,history= '",sum)
perc=(sum/400)*100
print("percentage mark=", perc)
