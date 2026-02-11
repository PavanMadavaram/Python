# Day 8 Helper Functions
def create_resume(name, age, city, skills):
    return {
        "name": name,
        "age": age,
        "city": city,
        "skills": skills
    }

def print_resume(resume):
    print(f"👨‍💼 {resume['name']}")
    print(f"📍 {resume['city']}, Age {resume['age']}")
    print("🛠️  Skills:", ", ".join(resume['skills']))

# Demo for IT job
resume = create_resume("Pavan", 24, "Hyderabad", ["Python", "Tableau"])
print_resume(resume)
print("Resume helper ready!")
