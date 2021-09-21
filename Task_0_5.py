def triangle_area(a,b,c):
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
  return area

output = triangle_area(23,30,10)
print(str(output) + " m^2")
