import datetime, os

NAME = "Troy Kennedy"
USERNAME = "kenned927"
'''
!README!

Change USERNAME and NAME varables to what you need
Then run:
>>>py format.py

Enter the assignment number and amount of files

'''
#! Made by Troy Kennedy /// DRS4TAN


assignment = input("What is the assignment number? ")
numOfFiles = int(input("How many files are needed? "))
date = datetime.datetime.now()
dir = os.path.join(os.path.curdir, f"Assignment {assignment}")
os.mkdir(dir)
os.chdir(dir)

for i in range(numOfFiles):
    filename = f'assignment-{assignment}-{USERNAME}-{assignment}-{str(i+1)}.py'
    print(filename)
    assignmentFile = open(filename, "w")
    assignmentFile.write(f'# {NAME} \n')
    assignmentFile.write(f'# {str(date.month)}/{str(date.day)}/{str(date.year)} \n')
    assignmentFile.write(f'# Assignment {assignment}-{str(i+1)} \n')
    assignmentFile.close()

print("Finished 😀")
print("Made by Troy Kennedy aka DRS4TAN 2019")