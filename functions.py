def sum_and_greet(*numbers,**student):
   multi=1
   for nums in numbers:
       multi*=nums
       print(multi)
   print(f"Hello {student}")   