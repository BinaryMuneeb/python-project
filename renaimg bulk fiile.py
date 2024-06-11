import os
def main():


    i=0
    path="C:/python project/imge"
    for filename in os.listdir(path):
        my_newfile="imgage"+str(i)+".png"
        # my_source=path+  filename
        my_old_file=path+my_old_file 
        my_old_file=os.path.join(path, my_old_file)
        os.rename(my_old_file,my_newfile)
        i+=1
        
if __name__== '__main__':
    main()
# import os

# def main():

#     i = 0
#     path = "C:/python project/imge"
#     for filename in os.listdir(path):
#         new_file_name = "image" + str(i) + ".png"
#         old_file_name = os.path.join(path, filename)
#         os.rename(old_file_name, new_file_name)
#         i += 1

# if __name__ == "__main__":
#     main()
