"""
Created on Sun Feb  4 08:23:49 2024

@author: mosope
"""

class PatientInformationSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, gender, diagnosis):
        self.patients[patient_id] = {
            'name': name,
            'age': age,
            'gender': gender,
            'diagnosis': diagnosis
        }
        print(f"Patient {name} added successfully.")

    def update_patient(self, patient_id, field, new_value):
        if patient_id in self.patients:
            if field in self.patients[patient_id]:
                self.patients[patient_id][field] = new_value
                print(f"Patient {self.patients[patient_id]['name']}'s {field} updated to {new_value}.")
            else:
                print(f"Invalid field: {field}.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def search_patient(self, name):
        results = [patient for patient_id, patient in self.patients.items() if patient['name'].lower() == name.lower()]
        return results

def main():
    patient_system = PatientInformationSystem()

    while True:
        print("\nPatient Information System Menu:")
        print("1. Add Patient")
        print("2. Update Patient Information")
        print("3. Search Patient")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            diagnosis = input("Enter Patient Diagnosis: ")
            patient_system.add_patient(patient_id, name, age, gender, diagnosis)
        elif choice == "2":
            patient_id = input("Enter Patient ID to update: ")
            field = input("Enter the field to update (name/age/gender/diagnosis): ")
            new_value = input(f"Enter the new value for {field}: ")
            patient_system.update_patient(patient_id, field, new_value)
        elif choice == "3":
            search_name = input("Enter the name of the patient to search: ")
            results = patient_system.search_patient(search_name)
            if results:
                print("Search Results:")
                for result in results:
                    print(result)
            else:
                print("No matching patients found.")
        elif choice == "4":
            print("Exiting Patient Information System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
