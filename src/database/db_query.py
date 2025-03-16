import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from spellchecker import SpellChecker
import os
from dotenv import load_dotenv
import google.generativeai as genai
import glob

load_dotenv()

class DB_Query:
  def __init__(self):
    self.model = SentenceTransformer("all-MiniLM-L6-v2")
    self.embedding_dim = 384
    self.index_id = faiss.read_index("R-squared/faiss_index.bin")
    self.speller = SpellChecker()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    self.gen_model = genai.GenerativeModel("gemini-2.0-flash")

  def search_faiss(self, query_text, top_k=3):
    """Searches FAISS for similar documents and returns detailed results."""
    query_embedding = self.model.encode([query_text]).astype("float32")

    distances, indices = self.index_id.search(query_embedding, top_k)
    
    f = ""
    j = 0
    for i in glob.glob("R-squared/output_text/*/*.txt"):
      if j == indices[0][0]:
        with open(i,"r",encoding='utf-8') as file:
          f = file.read()
          print(f)
      j += 1
    response = self.gen_model.generate_content(f"Provided a case file report, which is publicly available. Correct the spelling only if there is a mistake and report the file as such. No extra content generation is allowed. Don't add any extra line from your intelligence. Don't add like, File corrected:, Correctly spelled: or any as such Case file report: {f}")
    
    return response.text

# Example Query
# query = """
#    IN THE COURT OF THE JUDICIAL I CLASS MAGISTRATE-V,
# (SPECIAL COURT FOR MARK LIST CASES), THIRUVANANTHAPURAM.
# Present:- Smt. Aswathy.S, Judicial First Class Magistrate-V,
# ‘Thiruvananthapuram.

# Friday the 22 day of November, 2024/ Ist Agrahayana, 1946,

# CC. 1694/2018

# Complainant State represented by the Sub Inspector of Police, Railway Police
# Station, Thiruvananthapuram in Crime No. 210/2016.

# (By Assistant Public Prosecutor Gr-I, Sri. Kiran Ravi)

# Accused : Dhanam, aged 63 years, S/o. Karuppayya, Door No. 29/160,
# Market Road, Kulachal, Kanyakumari District, Tamil Nadu
# State.

# (By Advocate Sri, T1.Unniraja)

# Charge + Offence punishable under section 354 of Indian Penal Code,
# 1860.

# Plea + Not guilty

# Finding : Not guilty

# Sentence : Accused is found not guilty of offence punishable under section

# 354 of Indian Penal Code, 1860 and he is acquitted of the said
# offences under section 248(1) Code of Criminal Procedure,
# 1973. His bail bond stand cancelled and he is set at liberty.

# Description of accused
# Name | Father'sname Age Residence Taluk
# Dhanam —Karuppayya 63 Kulachal Kanyakumari
# Date of
# Occurrence | Report of Apprehension, Period of ___-Released | Commence
# Complaint of accused detention on bail ment of
# undergone during wial
# investigation
# inquiry or trial
# for the purpose

# of S. 428 CrP.C

# 21.02.2016 02.04,2016 21.02.2016 21.02.2016~ 23.03.2016 24.11.2022
# 23.03.2016
#  20fS

# ‘Commencement of Close of trial ‘Sentence or order Explanation for
# evidence delay ___|
# 19.11.2024 20.11.2024 22.11.2024 No delay J

# This case having been finally heard on today the court on the same day delivered the
# following :-

# JUDGMENT

# 1. Accused stands trial for offence punishable under section 354 of Indian Penal

# Code, 1860.

# 2. The prosecution case in brief is as follows :- On 21.02.2016, at 18.30 hours,

# at the general compartment of Sabari Express, when the train was about to
# reach at Varkala, the accused with an intention to outrage the modesty of CW1,
# touched on her private parts and showed obscene words against her. Thus
# accused has committed offence punishable under section 354 of Indian Penal

# Code, 1860.

# 3. Final report was filed by the Sub Inspector of police, Railway police station,
# ‘Thiruvananthapuram before the Hon'ble Chief Judicial Magistrate Court,
# Thiruvananthapuram and the case was taken on file as C.C. 763/2016.
# Cognizance was taken for the offences punishable w/ss. 294(b) and 354 of
# Indian Penal Code, 1860 against the accused. Thereafter, it was transferred to
# this court, in pursuance of the order of the Hon'ble Chief Judicial Magistrate,

# ‘Thiruvananthapuram, the case was refiled as CC. 1694/2018.
#  30fS
# 4. On appearance of the accused, he was enlarged on bail on 23.03.2016...

# Copies of all relevant prosecution records were furnished to him under section
# 207 Code of Criminal Procedure, 1973. Since ingredients of offence
# 1ws.294(b) were not attracted after hearing prosecution and counsel for accused
# charge for the offence u/s. 294(b) was not framed and charge framed for
# offence ws. 354 of Indian Penal Code, 1860 read over and explained to the

# accused to which he pleaded not guilty and claimed to be tried.

# 5. On the side of prosecution, PW1 was examined . As the material witnesses
# failed to support the prosecution case, the leamed Assistant Public Prosecutor
# ‘gave up the CW2 to CW4. In the absence of any incriminating circumstances
# against the accused questioning of the accused under section 313(1)(b) Code
# of Criminal Procedure, 1973 was dispensed with. Accused was called upon to
# adduce evidence but no defence evidence was adduced from the side of the

# accused,

# 6. Heard both sides and perued records.

# 7. The following points_have arisen for determination:

# (1) Whether on 21.02.2016, at 18.30 hours, the accused with an intention to
# outrage the modesty of PW, touched on her private parts at the general
# compartment of Sabari Express and thereby committed an offence

# punishable under section 354 of Indian Penal Code, 1860?
#  4ofS
# (2) If the accused is found guilty? What is the order as to sentence?

# 8. Point No,

# fo avoid repetition and for brevity, point number are considered
# together. Prosecution case is that accused has committed offence punishable
# under section 354 of Indian Penal Code, 1860. PWi deposed that she has no

# grievance against the accused person. Furthermore she denied her statement

# before the police. According to her the accused not assaulted.

# 9, The leamed Assistant Public Prosecutor had given up other witnesses and he is,
# justified in doing so as the material witness did not support the case of
# prosecution, Having considered evidence on record, this court is of the view
# that prosecution has failed to prove the guilt of accused. For the said reason

# these points are found against the prosecution.

# 10. Point No. 2 :- Upon the finding in point no. 1, the accused is found not guilty
# of offence punishable under section 354 of Indian Penal Code, 1860 and he is
# acquitted of the said offences under section 248(1) Code of Criminal

# Procedure, 1973. His bail bond stand cancelled and he is set at

# No material objects produced in this case.

# Dictated to the Confidential Assistant, transcribed and typed by her, corrected by me
# ‘and pronounced in the open court on this the 22” day of November, 2024,

# Sd/-
# Judicial I Class Magistrate-V,
# ‘Thiruvananthapuram,
#  SofS

# APPENDIX
# Witnesses for prosecution:=
# PW 2 XXXX
# Exhibits for prosecution:- NIL,
# Material objects marked NIL
# Witmesses & Exhibits for defence: NIL
# Sd/-
# Judicial | Class Magistrate-V,

# ‘Thiruvananthapuram,
# /rrue copy/!
# """

# db = DB_Query()
# res = db.search_faiss(query,1)
# print(res)
