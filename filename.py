#Python program to accept a filename from the user and print the extention of that.
f =input("Input the Filename: ")
fname = f.split(".")
print ("The extension of the file is : " +(fname[-1]))
