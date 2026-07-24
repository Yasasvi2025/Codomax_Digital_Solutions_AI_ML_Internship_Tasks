import os
import shutil

def organize_project_workspace():
    print("==================================================")
    print("     CODOMAX WORKSPACE STRUCTURING UTILITY       ")
    print("==================================================")
    print("Initializing repository optimization protocols...\n")

    # Step 1: Create professional project directories
    directories = ["data", "notebooks", "src", "reports", "screenshots"]
    for folder in directories:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created directory: /{folder}")

    print("\n--------------------------------------------------")
    print("Scanning and migrating assets dynamically...")
    print("--------------------------------------------------")

    files_in_root = os.listdir('.')

    # Step 2: Dynamically catch files to organize into directories
    for file in files_in_root:

        # Move Datasets
        if "task-5" in file.lower() and file.endswith(".csv"):
            shutil.copy2(file, "data/student_records_cleaned.csv")
            print(f"📦 Migrated Data: {file} -> data/student_records_cleaned.csv")
        elif file.endswith(".csv") and "student_scores" in file.lower():
            shutil.copy2(file, f"data/{file}")
            print(f"📦 Migrated Data: {file} -> data/{file}")

        # Move Prediction App Script (Task 11)
        elif file.endswith(".py") and ("11" in file or "prediction" in file.lower()) and "organizer" not in file.lower():
            shutil.copy2(file, "src/prediction_inference_app.py")
            print(f"📦 Migrated App Script: {file} -> src/prediction_inference_app.py")

        # Move all Notebooks (Tasks 1 through 10)
        elif file.endswith(".ipynb"):
            clean_name = file.lower().replace(" ", "").replace("_", "").replace("-", "")

            # Check task10 FIRST so "task1" condition doesn't snag "task10"
            if "task10" in clean_name:
                shutil.copy2(file, "notebooks/Task-10_Model_Evaluation.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-10_Model_Evaluation.ipynb")
            elif "task1" in clean_name:
                shutil.copy2(file, "notebooks/Task-1_Setup.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-1_Setup.ipynb")
            elif "task2" in clean_name:
                shutil.copy2(file, "notebooks/Task-2_Python_Basics.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-2_Python_Basics.ipynb")
            elif "task3" in clean_name:
                shutil.copy2(file, "notebooks/Task-3_NumPy_Basics.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-3_NumPy_Basics.ipynb")
            elif "task4" in clean_name:
                shutil.copy2(file, "notebooks/Task-4_Pandas_Basics.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-4_Pandas_Basics.ipynb")
            elif "task5" in clean_name:
                shutil.copy2(file, "notebooks/Task-5_Data_Cleaning.ipynb")
                print(f"📦 Migrated Notebook: {file} -> notebooks/Task-5_Data_Cleaning.ipynb")
            elif "task6" in clean_name:
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

        # Move PDF/HTML Reports
        elif file.endswith(".pdf") or file.endswith(".html"):
            if any(num in file for num in ["9", "10", "11", "12", "13"]):
                shutil.copy2(file, f"reports/{file}")
                print(f"📦 Migrated Report: {file} -> reports/{file}")

        # Move Output Screenshots
        elif file.endswith(".png"):
            shutil.copy2(file, f"screenshots/{file}")
            print(f"📦 Migrated Screenshot: {file} -> screenshots/{file}")

    print("\n==================================================")
    print("🚀 WORKSPACE OPTIMIZATION COMPLETE!")
    print("All folders populated successfully.")
    print("==================================================")

if __name__ == "__main__":
    organize_project_workspace()