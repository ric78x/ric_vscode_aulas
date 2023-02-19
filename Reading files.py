employee_file = open("employees2.txt", "r")
print(employee_file.read(),"\n")
employee_file.close()

employee_file = open("employees2.txt", "r")
print(employee_file.readable(),"\n")
employee_file.close()

employee_file = open("employees2.txt", "r")
print(employee_file.readlines()[1],"\n")
employee_file.close()

employee_file = open("employees2.txt", "r")
print(employee_file.readline(),"\n")
employee_file.close()

employee_file = open("employees2.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

employee_file = open("employees2.txt", "r")
print(employee_file.readlines())
employee_file.close()

employee_file = open("employees2.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


# r for ready
# w for write
# a for append
# r+ ready and write