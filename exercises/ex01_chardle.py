"""Example 1 - Chardle"""

__author__ = "730602160"

"""Step 1/4"""
keyword: str = input("Enter a 5-character word: ")
if len(keyword) != 5:
   print("Error: Word must contain 5 characters")
   quit()
keyletter: str = input("Enter a single character: ")
if len(keyletter) != 1:
   print("Error: Character must be a single character.")
   quit()
print("Searching for " + keyletter + " in " + keyword)
"""Step 2"""
if keyletter == keyword[0]:
   print(str(keyletter) + " found at index " + str( "0"))
if keyletter == keyword[1]:
   print(str(keyletter) + " found at index " + str( "1"))
if keyletter == keyword[2]:
   print(str(keyletter) + " found at index " + str( "2"))   
if keyletter == keyword[3]:
   print(str(keyletter) + " found at index " + str( "3")) 
if keyletter == keyword[4]:
   print(str(keyletter) + " found at index " + str( "4"))
"""Step 3"""
matchcount: int = 0
if keyletter == keyword[0]:
   matchcount = matchcount + 1
if keyletter == keyword[1]:
   matchcount = matchcount + 1
if keyletter == keyword[2]:
   matchcount = matchcount + 1
if keyletter == keyword[3]:
   matchcount = matchcount + 1
if keyletter == keyword[4]:
   matchcount = matchcount + 1               
if matchcount == 0:
   print("No instances of " + str(keyletter) + " found in " + str(keyword))
if matchcount == 1:   
   print(str(matchcount) + " instance of " + str(keyletter) + " found in " + str(keyword))
if matchcount > 1:   
   print(str(matchcount) + " instances of " + str(keyletter) + " found in " + str(keyword))