import pandas as pd
import random

# Define options for each field
skills = [
    "Python", "Java", "C++", "SQL", "HTML/CSS", "JavaScript", "Django",
    "Machine Learning", "Data Analysis", "Mobile App Development",
    "React.js", "Angular", "Blockchain", "Cybersecurity", "Networking",
    "Statistics", "Artificial Intelligence", "Cloud Computing", "AWS",
    "Google Cloud Platform (GCP)", "DevOps", "Chemistry", "Physics",
    "R Programming", "Digital Marketing"
]

interests = [
    "Web Development", "Artificial Intelligence", "Data Analysis",
    "Mobile Application Development", "Software Design", "Gaming",
    "Research", "Teaching", "AR/VR Development", "Blockchain Technology",
    "Cybersecurity", "Digital Marketing", "Engineering", "Robotics",
    "Internet of Things (IoT)", "Data Engineering", "Big Data",
    "Creative Writing", "Entrepreneurship", "Cloud Infrastructure",
    "Finance", "Supply Chain", "Healthcare Innovation",
    "Environmental Science", "Aerospace Engineering"
]

education = [
    "B.Tech (Computer Science/IT)", "B.Sc (Computer Science/Mathematics/Physics)",
    "M.Sc (Data Science)", "MCA", "MBA", "B.Com", "BBA", "B.Sc (Chemistry)",
    "B.Tech (AI/ML)", "B.E (Mechanical Engineering)", "B.E (Civil Engineering)",
    "B.E (Electrical Engineering)", "B.E (Electronics and Communication Engineering)",
    "B.Sc (Biotechnology)", "M.Sc (Artificial Intelligence)", "M.Tech (Data Analytics)",
    "Diploma (Computer Science)", "Diploma (Mechanical Engineering)",
    "BCA (Bachelor of Computer Applications)", "B.Tech (Cybersecurity)",
    "M.Sc (Physics)", "Ph.D. (Computer Science)", "B.Des (Design)",
    "BFA (Fine Arts)", "M.Tech (Robotics)"
]

certifications = [
    "AWS Certified", "Python Certified", "Google Cloud Certified",
    "Data Science Specialist", "Full Stack Developer", "Microsoft Azure Certified",
    "Cisco Certified Network Associate (CCNA)", "Certified Ethical Hacker (CEH)",
    "CompTIA Security+", "PMP (Project Management Professional)",
    "ITIL Foundation", "Salesforce Certified", "Scrum Master Certified (CSM)",
    "Oracle Certified Java Developer", "Certified Kubernetes Administrator (CKA)",
    "Tableau Desktop Specialist", "Power BI Certification",
    "Machine Learning with TensorFlow", "Blockchain Developer Certification",
    "Adobe Certified Professional", "Digital Marketing Certification",
    "Financial Analyst Certification", "Six Sigma Green Belt",
    "Cybersecurity Essentials Certified", "R Programming Certified"
]

job_roles = [
    "Web Developer", "Data Scientist", "AI Engineer", "Software Engineer",
    "Mobile Developer", "Quality Assurance Engineer", "DevOps Engineer",
    "Cybersecurity Analyst", "Cloud Engineer", "Machine Learning Engineer",
    "UI/UX Designer", "Game Developer", "Blockchain Developer",
    "Research Scientist", "Network Engineer", "Product Manager",
    "Technical Writer", "Data Analyst", "Business Analyst",
    "Database Administrator", "Professor", "Entrepreneur", "Financial Analyst",
    "Robotics Engineer", "Aerospace Engineer"
]

experience_levels = ["Fresher", "0–2 Years", "3–5 Years", "5+ Years"]

# Function to generate random data
def generate_data(num_entries):
    data = []
    for i in range(num_entries):
        row = {
            "Name": f"User_{i+1}",
            "Email": f"user{i+1}@example.com",
            "Skills": ", ".join(random.sample(skills, random.randint(2, 5))),
            "Interests": ", ".join(random.sample(interests, random.randint(1, 3))),
            "Educational Background": random.choice(education),
            "Certifications": ", ".join(random.sample(certifications, random.randint(1, 2))),
            "Desired Job Role": random.choice(job_roles),
            "Current Job Role": random.choice(job_roles) if random.random() > 0.5 else "None",
            "Experience Level": random.choice(experience_levels)
        }
        data.append(row)
    return data

# Generate 100 synthetic entries
synthetic_data = generate_data(50000)

# Convert to DataFrame
df = pd.DataFrame(synthetic_data)

# Save to CSV
df.to_csv("synthetic_career_data.csv", index=False)

print("Synthetic dataset generated and saved as 'synthetic_career_data.csv'.")
