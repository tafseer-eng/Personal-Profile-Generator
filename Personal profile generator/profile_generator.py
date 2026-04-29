#PERSONAL PROFILE GENERATOR


#Taking user input;
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
skills = input("Enter your skills (comma separated): ")


#Processing skills into a list
skills_list = [skills.strip() for skills in skills.split(",")]


#Generating profile
profile = f"""Personal Profile:
-----------------
Name: {name}
Age: {age}
City: {city}
Skills: {', '.join(skills_list)}""" 
print(profile)