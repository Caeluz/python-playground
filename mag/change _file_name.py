import os
import glob

# file_names = [
# "Citizen's Viewing via QR (4)",
# "Citizen's Viewing via QR (3)",
# "Citizen's Viewing via QR (2)",
# "Citizen's Viewing via QR",
# "Uploaded Files Index",
# "Upload Files Modal",
# "Consultation Upload Files",
# "Doctor's Consultation Form (8)",
# "Doctor's Consultation Form (7)",
# "Doctor's Consultation Form (6)",
# "Doctor's Consultation Form (5)",
# "Doctor's Consultation Form (4)",
# "Doctor's Consultation Form (3)",
# "Doctor's Consultation Form (2)",
# "Doctor's Consultation Form",
# "Doctor's Consultation Form Full",
# "Patient's Info Consultation (2)",
# "Patient's Info Consultation",
# "Doctor's Consultations Index (2)",
# "Doctor's Consultations Index",
# "Dialysis Hospital Service (2)",
# "Dialysis Hospital Service",
# "Consultation Hospital Service",
# "Add Medical Service",
# "Citizen's Hospital Services Index (3)",
# "Citizen's Hospital Services Index (2)",
# "Citizen's Hospital Services Index ",
# "Submit Register",
# "Register (11)",
# "Register (10)",
# "Register (9)",
# "Register (8)",
# "Register (7)",
# "Register (6)",
# "Register (5)",
# "Register (4)",
# "Register (3)",
# "Register (2)",
# "Register",
# "Citizen's Options (3)",
# "Citizen's Options (2)",
# "Citizen's Options",
# "Citizen Registrant's Index (2)",
# "Citizen Registrant's Index",
# ]   

# reversed_file_names = file_names[::-1]

# print(reversed_file_names, end="")
file_names = [   
    'Register (1)', 
    'Register (2)', 
    'Register (3)', 
    'Register (4)', 
    'Register (5)', 
    'Register (6)', 
    'Register (7)', 
    'Register (8)',
    'Submit Register',
    "Citizen Registrant's Index", 
    "Citizen's Options", 
    "Click Icon",
    "Citizen's Info (1)",
    "Citizen's Info (2)",
    "Citizen's Info (3)",
    "Citizen's Info - Vaccination Button",
    "Citizen's Info - Vaccination Modal",
    "Man Icon",
    "Citizen's Info - Uploading Files Button",
    "Citizen's Info - Picture",
    "Citizen's Info - Signature (1)",
    "Citizen's Info - Signature (2)",
    "Citizen's Info - Delete Button (1)",
    "Citizen's Info - Delete Button (2)",
    "Citizen's Info - Biometrics (1)",
    "Citizen's Info - Biometrics (2)",
    "Citizen's Info - Print Card Button (Unclickable)",
    "Citizen's Info - Print Card Button (Clickable)",
    "Citizen's Info - Card (Front)",
    "Citizen's Info - Card (Back)",
    "Citizen's Info via QR (1)",
    "Citizen's Info via QR (2)",
    "Citizen's Info via QR (3)",
    "Citizen's Info via QR (4)",
    "Citizen's Hospital Services Index (1)",
    "Citizen's Hospital Services Index (2)",
    'Add Medical Service',
    'Consultation Hospital Service',
    'Dialysis Hospital Service (1)', 
    'Dialysis Hospital Service (2)', 
    "Doctor's Consultations Index (1)",
    "Doctor's Consultations Index (2)",
    "Patient's Info Consultation (1)",
    "Patient's Info Consultation (2)",
    "Doctor's Consultation Form (1)",
    "Doctor's Consultation Form (2)",
    "Doctor's Consultation Form (3)",
    "Doctor's Consultation Form (4)",
    "Doctor's Consultation Form (5)",
    "Doctor's Consultation Form (6)",
    "Doctor's Consultation Form (7)",
    'Consultation Upload Files',
    'Upload Files Modal', 
    'Uploaded Files Index', 
]
# file_name = [
#     "image (1)",
#     "image (2)",
#     "image (3)",
#     "image (4)",
#     "image (5)",
#     "image (6)",
#     "image (7)",
#     "image (8)",
#     "image (9)",
#     "image (10)",
#     "image (11)",
#     "image (12)",
#     "image (13)",
#     "image (14)",
#     "image (15)",
#     "image (16)",
#     "image (17)",
#     "image (18)",
#     "image (19)",
#     "image (20)",
#     "image (21)",
#     "image (22)",
#     "image (23)",
#     "image (24)",
#     "image (25)",
#     "image (26)",
#     "image (27)",
#     "image (28)",
#     "image (29)",
#     "image (30)",
#     "image (31)",
#     "image (32)",
#     "image (33)",
#     "image (34)",
#     "image (35)",
#     "image (36)",
#     "image (37)",
#     "image (38)",
#     "image (39)",
#     "image (40)",
#     "image (41)",
#     "image (42)",
#     "image (43)",
#     "image (44)",
# ]

#C:\Users\ADMIN\Documents\lgu\System

directory = r'C:\Users\ADMIN\Documents\lgu\System\New folder - Copy'

# Get a list of all PNG files in the folder
png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]

# Check if the number of new names matches the number of PNG files
if len(png_files) != len(file_names):
    print("Number of new names does not match the number of PNG files.")
    print(len(png_files), len(file_names))
else:
    # Sort files numerically using a custom key
    sorted_png_files = sorted(png_files, key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Iterate over the sorted PNG files and rename them
    for i in range(len(sorted_png_files)):
        old_name = os.path.join(directory, sorted_png_files[i])
        new_name = os.path.join(directory, f"{file_names[i]}.png")
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} to {new_name}")

print("File renaming completed.")
