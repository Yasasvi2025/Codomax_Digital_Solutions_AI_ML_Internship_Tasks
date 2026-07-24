import os
import shutil

def organize_project_workspace():
    print("==================================================")
    print("     CODOMAX WORKSPACE STRUCTURING UTILITY       ")
    print("==================================================")
    print("Initializing repository optimization protocols...\n")

    # Step 1: Create the professional project directories
    directories = ["data", "notebooks", "src", "reports"]
    for folder in directories:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created directory: /{folder}")
            
    print("\n--------------------------------------------------")
    print("Scanning and migrating assets dynamically...")
    print("--------------------------------------------------")

    # Get a list of all files in the current root folder
    files_in_root = os.listdir('.')

    # Step 2: Dynamically catch files to prevent empty folders from typos
    for file in files_in_root:
        
        # Move the Dataset
        if "task-5" in file.lower() and file.endswith(".csv"):
            shutil.copy2(file, "data/student_records_cleaned.csv")
            print(f"📦 Migrated Data: {file} -> data/student_records_cleaned.csv")

        # Move the Prediction App Script (Day 11)
        elif file.endswith(".py") and ("11" in file or "prediction" in file.lower()) and "organizer" not in file.lower():
            shutil.copy2(file, "src/prediction_inference_app.py")
            print(f"📦 Migrated App Script: {file} -> src/prediction_inference_app.py")

        # Move all Notebooks (Day 6 to Day 10)
        elif file.endswith(".ipynb"):
            clean_name = file.lower().replace(" ", "").replace("_", "").replace("-", "")
            
            if "task6" in clean_name:
                shutil.copy2(file, "notebooks/Task-6_Data_Visualization.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-6_Data_Visualization.ipynb")
            elif "task7" in clean_name:
                shutil.copy2(file, "notebooks/Task-7_Machine_Learning_Basics.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-7_Machine_Learning_Basics.ipynb")
            elif "task8" in clean_name:
                shutil.copy2(file, "notebooks/Task-8_Build_Model.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-8_Build_Model.ipynb")
            elif "task9" in clean_name:
                shutil.copy2(file, "notebooks/Task-9_Predict_Model.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-9_Predict_Model.ipynb")
            elif "task10" in clean_name:
                shutil.copy2(file, "notebooks/Task-10_Model_Evaluation.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-10_Model_Evaluation.ipynb")

        # Move PDF/HTML Reports
        elif file.endswith(".pdf") or file.endswith(".html"):
            if any(num in file for num in ["9", "10", "11", "12"]):
                shutil.copy2(file, f"reports/{file}")
                print(f"📦 Migrated Report: {file} -> reports/{file}")

    print("\n==================================================")
    print("🚀 WORKSPACE OPTIMIZATION COMPLETE!")
    print("All folders populated successfully.")
    print("==================================================")

if __name__ == "__main__":
    organize_project_workspace()