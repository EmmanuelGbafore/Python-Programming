# File Handling Assignment
with open ("my_file.txt", "w")  as file:     # Create a new text file
  
  # Write at least three lines consisting strings and numbers
  file.write("Name: Emmanuel Gbafore\n")
  file.write("Age: 31\n")
  file.write("Gender: Male\n")

# File Reading and Display
with open ("my_file.txt", "r") as file:
  content= file.read()
  print("Contents of my_file.text: ")
  print(content)

# Open script in append mode and add three additional lines
with open ("my_file.txt", "a")  as file:      # Open in append mode
# Append three additional lines
  file.write("School: PLP Academy \n")
  file.write("Location: Nairobi \n")
  file.write("Cohort: Four\n")

# Error handling using try, except and finally
try: 
  with open("my_file.txt", "r") as file:
   content=file.read()
   print(content)

except FileNotFoundError:
  print("Error file not found!") 

except PermissionError:
  print("Error: Permission denied!")

except Exception as e:
  print("An unexpected error occured!", e)

finally: 
 print("Error handling completed! ")
