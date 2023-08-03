import openai
import pdfplumber
import docx2txt
import pathlib

openai.api_key = "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"

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


# {
#   "Personal & Contact Information": {
#     "Name": "Ankit Tanmay",
#     "Email": "ankittanmay@gmail.com",
#     "Phone No": "7903305762 (Home)",
#     "Address": "Bengaluru, Karnataka, India",
#     "Social Media Profiles": {
#       "LinkedIn": "www.linkedin.com/in/ankit-tanmay",
#       "GitHub": "",
#       "Facebook": "",
#       "Twitter": "",
#       "Instagram": "",
#       "YouTube": "",
#       "Kaggle": ""
#     }
#   },
#   "Summary": "Data scientist with two years of experience in providing data driven Machine Learning solutions to complex business problems in predictive and inquisitive R analytics domain to Fortune 500 Clients",
#   "Skills": {
#     "Primary Skills": "Python",
#     "Secondary Skills": "R, Excel",
#     "Technical Skills": "Data Handling & Modelling, Data Visualization, Data warehousing",
#     "Computer Skills": "Tableau, Power BI, Excel Dashboard",
#     "Soft skills": "",
#     "Communication Skills": "",
#     "Leadership Skills": "",
#     "Management Skills": "",
#     "Other Skills": ""
#   },
#   "Certifications": {
#     "Certified by": "",
#     "Certified in": "",
#     "Year": ""
#   },
#   "Experience": [
#     {
#       "Company": "Mu Sigma Inc.",
#       "Title": "Data Scientist",
#       "Timeline / Duration": "May 2017 - Present",
#       "Domain": "Bengaluru Area, India",
#       "Projects & Responsibilities": [
#         {
#           "Project": "Sourcing and Procurement Analytics",
#           "Responsibilities": "Quantified savings from removing intermediary suppliers, performed clustering on large items data set, used ensemble of tree-based prediction models, implemented the algorithm in parallel processing"
#         },
#         {
#           "Project": "Warranty Analytics",
#           "Responsibilities": "Forecast of warranty settlements, bill approval prediction using Survival analysis, industry benchmark of warranty recovery"
#         },
#         {
#           "Project": "Pricing Analytics",
#           "Responsibilities": "Price elasticity modeling of multiple SKUs"
#         },
#         {
#           "Project": "Social Media & Web Scraping projects",
#           "Responsibilities": "Automated Web scraping of 30+ websites, used Twitter, Facebook, Instagram and Yelp APIs for performing analysis"
#         }
#       ]
#     },
#     {
#       "Company": "ELM",
#       "Title": "Trainer for Machine Learning",
#       "Timeline / Duration": "December 2018 - March 2019 (4 months)",
#       "Domain": "Bengaluru Area, India",
#       "Projects & Responsibilities": [
#         {
#           "Project": "",
#           "Responsibilities": "Teaching postgraduate students machine learning with R, carrying out training programs for colleges"
#         }
#       ]
#     },
#     {
#       "Company": "Weawe.in",
#       "Title": "Co-Founder",
#       "Timeline / Duration": "August 2015 - May 2016 (10 months)",
#       "Domain": "New Delhi Area, India",
#       "Projects & Responsibilities": [
#         {
#           "Project": "",
#           "Responsibilities": "Conceptualized and executed a social eCommerce platform, marketed the Web app to multiple college students"
#         }
#       ]
#     }
#   ],
#   "Education": {
#     "Institution Name": "National Institute of Technology Jamshedpur",
#     "Graduation Date": "2013 - 2017",
#     "Field of Study/Major": "B. Tech EEE, Electrical and Electronics Engineering",
#     "GPA/Score": ""
#   }
# }

# {
#   "Personal & Contact Information": {
#     "Name": "Ankit Tanmay",
#     "Email": "ankittanmay@gmail.com",
#     "Phone No": "7903305762 (Home)",
#     "Address": "Bengaluru, Karnataka, India",
#     "Social Media Profiles": {
#       "LinkedIn": "www.linkedin.com/in/ankit-tanmay",
#       "Facebook": "",
#       "Twitter": "",
#       "Instagram": "",
#       "YouTube": "",
#       "Kaggle": ""
#     }
#   },
#   "Summary": "Data scientist with two years of experience in providing data driven Machine Learning solutions to complex business problems in predictive and inquisitive R analytics domain to Fortune 500 Clients",
#   "Top Skills": {
#     "Primary Skills": "Python",
#     "Secondary Skills": "R, Excel",
#     "Technical Skills": "Data Handling & Modelling, Data Visualization, Data warehousing",
#     "Soft skills": "Consulting approach to problem solving, Effective communication"
#   },
#   "Certifications": {
#     "Probability and Statistics for Business and Data Science": "",
#     "Honors-Awards": "Spot Award",
#     "Guest Speaker": "NIT Conclave' 15"
#   },
#   "Experience": [
#     {
#       "Company": "Mu Sigma Inc.",
#       "Title": "Data Scientist",
#       "Timeline / Duration": "May 2017 - Present",
#       "Location": "Bengaluru Area, India",
#       "Projects & Responsibilities": [
#         {
#           "Project": "Sourcing and Procurement Analytics",
#           "Responsibilities": [
#             "Quantified savings from removing intermediary suppliers for a leading US based retailer",
#             "Identified key metrics for clustering similar items and performed clustering on large items dataset",
#             "Used ensemble of tree-based prediction models to quantify cost advantage from change in the country of procurement",
#             "Implemented the algorithm in parallel processing to optimize code runtime"
#           ]
#         },
#         {
#           "Project": "Warranty Analytics",
#           "Responsibilities": [
#             "Forecasted warranty settlements made by suppliers to a leading OEM",
#             "Predicted the month of Bill Approval from suppliers of the OEM using Survival analysis",
#             "Benchmarked warranty recovery to help OEM prioritize internal business decisions"
#           ]
#         },
#         {
#           "Project": "Pricing Analytics",
#           "Responsibilities": [
#             "Modeled price elasticity of multiple SKUs for a leading retailer",
#             "Used semi-log price elasticity predictive model to govern price and sales for multiple SKUs"
#           ]
#         },
#         {
#           "Project": "Social Media & Web Scraping projects",
#           "Responsibilities": [
#             "Automated web scraping of 30+ websites for different ongoing projects",
#             "Used Twitter, Facebook, Instagram, and Yelp APIs for performing analysis on social media data",
#             "POC for any web scraping project and business development calls within the organization"
#           ]
#         }
#       ]
#     },
#     {
#       "Company": "ELM",
#       "Title": "Trainer for Machine Learning",
#       "Timeline / Duration": "December 2018 - March 2019 (4 months)",
#       "Location": "Bengaluru Area, India",
#       "Responsibilities": "Taught postgraduate students machine learning with R and conducted training programs for colleges with data science curriculum"
#     },
#     {
#       "Company": "Weawe.in",
#       "Title": "Co-Founder",
#       "Timeline / Duration": "August 2015 - May 2016 (10 months)",
#       "Location": "New Delhi Area, India",
#       "Responsibilities": "Conceptualized and executed a social eCommerce platform and marketed it to college students"
#     }
#   ],
#   "Education": {
#     "Institution Name": "National Institute of Technology Jamshedpur",
#     "Degree": "B. Tech EEE, Electrical and Electronics Engineering",
#     "Graduation Date": "(2013 - 2017)"
#   }
# }

