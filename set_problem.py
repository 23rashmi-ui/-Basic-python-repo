#Q1. Hospital Patient Management System
#A hospital maintains records of patients visiting its departments. The management wants to identify common patients and update department records.
#Given:
#general_patients = {101, 102, 103, 104, 105}
#cardiology_patients = {103, 104, 106, 107}
#Tasks:
#1.	Create two sets for the patient records.
general_patients = {101, 102, 103, 104, 105}
cardiology_patients = {103, 104, 106, 107}
#2.	Find patients visiting both departments.
patients_visiting_both_department = general_patients.intersection(cardiology_patients)
print(patients_visiting_both_department)
output: patients_visiting_both_department :{103, 104}
#3.	Find patients visiting only the general department.
patients_visiting_only_general_department = general_patients.difference(cardiology_patients)
print(patients_visiting_only_general_department)
output:patients_visiting_only_general_department:{101,102,105}
#4.	Find all unique patients visiting either department.
unique_patients_visiting =  general_patients.symmetric(cardiology_patients)
print(unique_patients_visiting)
output:unique_patients_visiting:{101,102,105,106,107}
#5.	Add two new patients, 108 and 109, to the cardiology department.
two_new_patients = cardiology_patients.update([108,109])
print(cardiology_patients)
output:cardiology_patients:{103, 104, 106, 107, 108, 109}
#6.	Display the updated cardiology patient records and total count.
update_cardiology = cardiology_patients
print(update_cardiology)
print(len(update_cardiology))
output:{103, 104, 106, 107, 108, 109}
6

#Q2. Employee Training Management System
#An organization conducts Python and Java training programs. The HR department wants to analyze employee participation.
#Given:
#python_training = {201, 202, 203, 204, 205}
#java_training = {203, 204, 206, 207}
#Tasks:
#1.	Create two sets representing employees attending Python and Java training.
python_training = {201, 202, 203, 204,205}
java_training = {203, 204, 206, 207}

#2.	Find employees attending both training programs.
attending_both = python_training.intersection(java_training)
print(attending_both)
output:{203, 204}
#3.	Find employees attending only Java training.
attending_only_java = java_training.difference(python_training)
print(attending_only_java)
output:{206, 207}
#4.	Find employees attending exactly one training program.
exactly_one_trainig = python_training.symmetric_difference(java_training)
print(exactly_one_training)
output:{201, 202, 205, 206, 207}
#5.	Check whether employee 208 is present in either training set.
employee = {208}
present_or_not = employee.issubset(python_training)
print(present_or_not)
present_or_not = employee.issubset(java_training)
print(present_or_not)
output:False
False

#6.	Add employee 208 to the Python training set.
python_training = python_training.add(208)
print(python_training)
