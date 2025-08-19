'''
 open("file name.txt", "mode")
 
'''

# read mode to a file
file = open(r"C:\Users\hp\OneDrive\Desktop\Phyton\file_1.txt", "r") # read mode
content = file.read() # read the entire file
print(content)

file.close() # close the file after reading


# write mode to a file / overwrite the file
# if file does not exist, it will create a new file
files = open(r'C:\Users\hp\OneDrive\Desktop\Phyton\file_1.txt','w') # write mode
files.write('this is file handling very improtant topic in phyton used for save data, update data')
files.close() # close the file after writing

# with statement closes the file automatically

with open(r'C:\Users\hp\OneDrive\Desktop\Phyton\file_2.txt','w') as file:
    file.write('this is file handling very improtant topic in phyton used for save data, update data')

# append mode to a file / add data to the end of the file without overwriting
# if file does not exist, it will create a new file

with open(r'C:\Users\hp\OneDrive\Desktop\Phyton\file_2.txt','a') as file:
    content= input('Enter the content to append: ')
    file.write(content + '\n') # add new line after appending content