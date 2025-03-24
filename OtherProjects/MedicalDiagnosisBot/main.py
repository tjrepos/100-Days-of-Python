# This is a diagnosis bot for dehydration


diag_ga = ""
diag_eyes = "not assessed"
diag_skin = "not assessed"
diag_final = ""
patient_full_name = ""
patient_data = [
    "Michael Bennet: Diagnosis - Severe Dehydration, Appearance - Irritable/Lethargic, Eyes - Not Assessed,  Skin Pinch - Slow",
"Sally Jones: Diagnosis - No Dehydration, Appearance - Normal, Eyes -  Normal/Slightly Sunken,  Skin Pinch: Not Assessed",
"Brenda Carmichael: Diagnosis - Some Dehydration, Appearance - Normal, Eyes -  Not Assessed,  Skin Pinch: Normal",
]


def retrieve_records():
    print("""
Current patient records:
""")
    for patient in patient_data:
        print(patient)
    print("\n")
    main_menu()

def store_diagnosis():
    global diag_ga, diag_final, diag_skin, diag_eyes, patient_full_name
    print("""
Storing diagnosis...
""")
    diag_store = (f"{patient_full_name}: Diagnosis - {diag_final}, Appearance - {diag_ga}, Eyes - {diag_eyes}, Skin Pinch - {diag_skin}")
    patient_data.append(diag_store)
    main_menu()


def final_diagnosis():
    global diag_ga, diag_final, diag_skin, diag_eyes
    print("""
Thank you for completing the diagnosis.
""")
    match diag_ga:
        case "normal":
            print(f"""Based upon your assessments, {patient_full_name} has {diag_final}
The patient's general appearance was assessed as {diag_ga}
The patient's eyes were assessed as appearing {diag_eyes}
The response to a skin pinch was {diag_skin}""")
            store_diagnosis()
        case "irritable/lethargic":
            print(f"""Based upon your assessments, {patient_full_name} has {diag_final}
The paitent's general appearance was assessed as {diag_ga}
The the response to a skin pinch was assessed as {diag_skin}
The appearance of the patient's eyes was {diag_eyes}""")
            store_diagnosis()
        case _:
            print("Error in diagnosis. Please enter the assessment data again...")
            general_appearance()


def eye_appearance():
    global diag_ga, diag_final, diag_eyes
    print("""Please assess the appearance of the patient's eyes.
    1 - Normal or slightly sunken
    2 - Very sunken
    q - Return to main menu""")
    patient_eye_appearance = input ("Please input an option:")
    match patient_eye_appearance:
        case "1":
            print("""Thank you. You have assessed the patient's eyes as appearing normal or slightly sunken
            Loading final diagnosis...""")
            diag_eyes = "normal"
            diag_final = ("no dehyrdration")
            final_diagnosis()
        case "2":
            print("""Thank you. You have assessed the patient's eyes as appearing very sunken
            Loading final diagnosis...""")
            diag_eyes = "very sunken"
            diag_final = ("severe dehyrdration")
            final_diagnosis()
        case "q":
            print("Returning to the main menu...")
            main_menu()
        case _:
            print("Invalid input. Please try again!")
            eye_appearance()

def skin_appearance():
    global diag_ga, diag_final, diag_skin
    print("""Please assess the response of the patient's skin to a pinch test.
        1 - Skin pinch normal
        2 - Skin pinch slow
        q - Return to main menu""")
    patient_skin_appearance = input("Please input an option:")
    match patient_skin_appearance:
        case "1":
            print("""Thank you. You have assessed the patient's skin response as normal.
Loading final diagnosis...""")
            diag_skin = "normal"
            diag_final = ("some dehyrdration")
            final_diagnosis()
        case "2":
            print("""Thank you. You have assessed the patient's skin response as slow.

Loading final diagnosis...
""")
            diag_skin = "slow"
            diag_final = ("severe dehyrdration")
            final_diagnosis()
        case "q":
            print("Returning to the main menu...")
            main_menu()
        case _:
            print("Invalid input. Please try again!")
            eye_appearance()

def general_appearance():
    global diag_ga
    print("""Please assess the general demeanour of the patient
    1 - for Normal Appearance
    2 - for Irritable or Lethargic
    q - Return to main menu""")
    patient_general_appearance = input("Please input an option:")
    match patient_general_appearance:
        case "1":
            print("""Thank you. You have assessed the patient's appearance as normal.

Loading eye appearance diagnosis...
""")
            diag_ga = "normal"
            eye_appearance()
        case "2":
            print("""Thank you. You have assessed the patient's appearance as irritable or lethargic.
Loading skin appearance diagnosis...
""")
            diag_ga = "irritable/lethargic"
            skin_appearance()
        case "q":
            print("Returning to the main menu...")
            main_menu()
        case _:
            print("Invalid input. Please try again!")
            general_appearance()


def correct_patient_name(first_name, last_name):
    global patient_full_name
    full_name = (f"{first_name} {last_name}")
    print(f"""You have entered {full_name}
Is this correct??""")
    correct_name = input("Enter y to proceed,n to re-enter patient name or q to return to the main menu:")
    match correct_name:
        case "y":
            print(f"""Thank you for confirming the patient's name is {full_name}
Loading diagnosis procedure...""")
            patient_full_name = full_name
            general_appearance()
        case "n":
            diagnosis()
        case "q":
            main_menu()
        case _:
            print("Invalid response. Please try again!")
            correct_patient_name(first_name, last_name)


def diagnosis():
    print("""
Thankyou for choosing to complete a diagnosis.
""")
    patient_first_name = input("Please input the patient's first name:")
    patient_last_name = input("Please input the patient's last name:")
    correct_patient_name(first_name=patient_first_name, last_name=patient_last_name)


def main_menu ():
    print("""Welcome to the medical diagnosis bot!!
    
    1 - Conduct a diagnosis
    2 - View previous diagnosis records
    q - Quit the diagnosis bot
    """)
    main_prompt = input("Please enter an option:")
    match main_prompt:
        case "1":
            print("Loading the diagnosis menu...")
            diagnosis()
        case "2":
            print("Loading patient records...")
            retrieve_records()
        case "q":
            print("""
Thank you for using the medical diagnosis bot.

Now exiting the application...
""")
            exit()
        case _:
            print("""
That is not a valid entry. Please enter a choice from the menu
""")
            main_menu()

main_menu()

