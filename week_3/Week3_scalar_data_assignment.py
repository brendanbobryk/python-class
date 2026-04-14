# gathers all user input required
name = str(input("Enter your full name: "))
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
courses = int(input("How many courses are you taking? "))
full_time_input = str(input("Are you a full-time student? (yes/no): "))

is_full_time = full_time_input.lower() == "yes" # determines full-time status
credits = courses * 3 # calculates credits based on courses
deans_list = gpa >= 3.5 # determines dean's list eligibility

# prints results for the student summary
print("--------------------\nStudent Summary\n--------------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Full-Time Student: {is_full_time}")
print(f"Dean's List Eligible: {deans_list}")

# prints results for the variable types
# (using the type() function was a requirement)
print("\n--------------------\nVariable Types\n--------------------")
print("name: ", type(name))
print("age: ", type(age))
print("gpa: ", type(gpa))
print("is_full_time: ", type(is_full_time))
print("deans_list: ", type(deans_list))