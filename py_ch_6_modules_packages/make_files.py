# import os

# Directory: List of the folders you want to create
file_names = ["py_ch6_1_2_CustModule",
"py_ch6_1_3_ExtnModl",
"py_ch6_1_4_Eg_autopep8_ASCIart",
"py_ch6_1_5_about_name_"]



# Parent Directory path
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
# path = os.path.join(parent_dir, directory)
for i in range (0, len(file_names)):
    # path = "./"+directories[i]
    # Create the files
    try:
        # os.makedirs(path, exist_ok = True)
        f = open(f"{file_names[i]}.py", "w") # creates an empty 'py' 
        print(f"{file_names[i]}.py is created sucuessfully")
    except:
        print("files '%s' can not be created" % file_names[i])

# run windows cmd/terminal inside the working directory
# python make_files.py

''' CustModule
ExtnModl
Eg_autopep8_ASCIart
about_name_ '''