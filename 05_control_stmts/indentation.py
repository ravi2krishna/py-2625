# Indentation Rules 

# -> When To Use Space ? -> When We Write Block Of Code (:)

# -> When Not To Use Space ? -> Single Statement 

# -> How Many Spaces To Use ? -> At least one, but recommended is 4 spaces i.e tab 

print("Hello") # When Not To Use Space ? -> Single Statement 

#  print("Hi") # IndentationError: unexpected indent

# When To Use Space ? -> When We Write Block Of Code (:)
# class Student: # IndentationError: expected an indented block after class definition on line 14
# student_id = 101
# student_name = "Ravi"
# student_email = "ravi@gmail.com"

# When To Use Space ? -> When We Write Block Of Code (:)
# -> How Many Spaces To Use -> at least one 
class Student: 
 student_id = 101
 student_name = "Ravi"
 student_email = "ravi@gmail.com"

class Student: 
  student_id = 101
  student_name = "Ravi"
  student_email = "ravi@gmail.com"

class Student: 
          student_id = 101
          student_name = "Ravi"
          student_email = "ravi@gmail.com"
          
# class Student: 
#   student_id = 101
#    student_name = "Ravi" # IndentationError: unexpected indent
#     student_email = "ravi@gmail.com"

class Student: 
   student_id = 101
   student_name = "Ravi" # IndentationError: unexpected indent
   student_email = "ravi@gmail.com"
   
