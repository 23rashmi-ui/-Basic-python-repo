#Q8. Hospital Patient Management System
#A hospital maintains records of patients visiting its departments. The management wants to identify common patients and update department records.
#Given:
#general_patients = {101, 102, 103, 104, 105}
#cardiology_patients = {103, 104, 106, 107}
#Tasks:
#1.	Create two sets for the patient records.
general_patients = {101, 102, 103, 104, 105}
cardiology_patients = {103, 104, 106, 107}
#2.	Find patients visiting both departments.
patients visiting both_department = general_patients.intersection(cardiology_patients)
print(patients visiting both_department)
output: patients visiting both_department
#3.	Find patients visiting only the general department.
#4.	Find all unique patients visiting either department.
#5.	Add two new patients, 108 and 109, to the cardiology department.
#6.	Display the updated cardiology patient records and total count.
