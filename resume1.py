import openai
import pdfplumber
import docx2txt
import pathlib

openai.api_key = "YOUR_API_KEY"

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        pages = []
        for page in pdf.pages:
            text = page.extract_text()
            pages.append(text)
    return pages

def process_resume(file_path):
    file_extension = pathlib.Path(file_path).suffix.lower()
    if file_extension == '.pdf':
        document = extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        document = docx2txt.process(file_path)
    elif file_extension == '.txt':
         with open(file_path, 'r') as file:
             document = file.read()
    else:
        raise ValueError("Unsupported file format.")

    messages = [
        {"role": "system", "content": "You are a hiring manager."},
        {"role": "user", "content": f'the goal is to divide a resume which is "{document}" so that the details are concise and with relevant information in a few words in json format to save the time it takes to read a resume.'
                                    'Take the data from "{document}", and divide the data based on the attributes.specify if the details are true or false'
                                    'divide it based on:'
                                    '[Personal & Contact Information'	
                                    'Name – First, Last -Full name	Email (if multiple emails)	Phone No (if multiple phone no)	Profile Picture	,Address,Location,Gender & Date of Birth (DOB),Marital status,Social Media Profiles:LinkedIn,GitHub,Facebook,Twitter,Instagram,YouTube,Kaggle,Assessment, Hackathons, Competitive Coding Platforms,Others,'	
                                    'Summary or Profile Summary or Career Summary,Career Objective,Education,All educational qualifications	,Institution Name,Graduation Date,Field of Study/Major,GPA/Score,Certifications ,Certified by,Certified in,Year	,Internship	,Internship At,Others,Role and Responsibility,Year-From and To,'	
                                    'Skills	,Primary Skills	,Secondary Skills,Technical Skills,Computer Skills,Soft skills,Communication Skills,Accent Skills,Leadership Skills,Management Skills,Other Skills,Experience,List of Companies,Title,Timeline /Duration in Each Company,Domain,Projects,Skills,Location,Web Link,Reported To,Total Exp.Internationals Experience,Entrepreneurship or Startup Experience,Cross-culture Experience,'	
                                    'Domain/Industry Expertise,Patents,White Paper,Relevant Coursework,Other Assessments/Competition Scores etc.,Publications,Training,Conferences,HR Requirements,Testimonials,References- Referrers name, relationship, Contact number, Email ID,Salary History - Current CTC and Expected CTC,Career Break,Work Authorization,Language (Read / Write / Spoken),Culture Fit,Others,Extra-Curricular Activities,Hobbies,Preferred Industry,Preferred Companies	,Notice period,'
                                    'Additional,Security Clearances,Military Experience,Volunteer Experience,Professional Development,Referral Source,Drivers License,Awards or Honors,Professional Memberships,Accomplishments,Associations,Mentorship,Political Affiliations,Government Service,Coaching Certified,Preference – service/product, location, salary, etc.	]' 
                                    'give every single detail a json output.classify based on all the details given above,do not miss a single detail even if its empty.only specify the titles and a few words about things like projects and responsibilities'                     
                                    'Also make sure that the output is spaced out and there is necessary gaps between lines to improve readability'
                                    'and make sure the lines are with proper indentation and alignment'
                                    
                                    
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        max_tokens=8192,
        n=1,
        temperature=0.1,
        stop=None,
    )

    json_output = response.choices[0].message.content
    return json_output

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    output = process_resume(file_path)
    print(output)


