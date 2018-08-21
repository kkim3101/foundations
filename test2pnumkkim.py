import re
 def check_phone_num(string):
     s = re.search("\d{3}-\d{4}",string)

     if s:
         return True:
     else:
         return False:
