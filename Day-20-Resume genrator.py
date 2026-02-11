def get_skills():
    skills = []
    n = int(input("How many skills do you want to enter? "))
    for i in range(n):
        skill = input(f"Enter skill {i+1}: ")
        skills.append(skill)
    return skills
def generate_resume():
    print("Resume Generator\n")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    education = input("Enter your education: ")
    experience = input("Enter your experience: ")

    skills = get_skills()

    resume = f"""
	=========================
        RESUME
=========================
Name: {name}
Age: {age}
Email: {email}
Education:
{education}
Experience:
{experience}
Skills:
"""
    for skill in skills:
        resume += f"- {skill}\n"

    print("\n Your Resume:")
    print(resume)

    file = open("resume.txt", "w")
    file.write(resume)
    file.close()

    print("Resume saved as resume.txt")
generate_resume()
