import PythonModules.pdfEdit as pEdit 
import PythonModules.cvBuilder as cvB

import tkinter as tk

filePath ="CVs"

pdfs = pEdit.find_pdfs(filePath)
pdfl=[]
for pdf in pdfs:
    pdfl.append(pEdit.read_file(filePath+"/"+pdf))

txt= cvB.rephrase(cvB.combine((pdfl)))

keys="""You have experience with technical / team leadership of small to medium sized Agile development teams
You have backend development experience with strong Python and Django skills
You have architecture and design skills, including DRY principles
You have a good knowledge of Computer Science fundamentals such as OOP, Data Structures, Design Patterns and software engineering best practices
You're collaborative with great communication skills, happy to lead projects and mentor others"""


print(cvB.compose(txt,cvB.part.Personal,cvB.analyse_keys(keys)))
