import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def initialize_trained_model():
    """Loads the core student dataset and reconstructs the trained regression parameters."""
    try:
        # Load your curated baseline dataset
        df = pd.read_csv("task-5_data_cleaning.csv")
        df = df.drop_duplicates()
        df['Attendance_Pct'] = df['Attendance_Pct'].fillna(df['Attendance_Pct'].mean())
        df['Midterm_Score'] = df['Midterm_Score'].fillna(df['Midterm_Score'].mean())
        
        # Isolate historical data arrays
        X = df[['Midterm_Score']]
        y = df['Final_Score']
        
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.33, random_state=42)
        
        # Instantiate and optimize estimator weights
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    except FileNotFoundError:
        print("\n[Error]: 'task-5_data_cleaning.csv' could not be found.")
        print("Please ensure your dataset is placed in the same execution directory.")
        return None

def launch_prediction_app():
    print("==================================================")
    print("      CODOMAX STUDENT SCORE PREDICTION APP        ")
    print("==================================================")
    print("Loading predictive algorithm components...")
    
    regressor = initialize_trained_model()
    if regressor is None:
        return
        
    print("System Initialization Complete! ✓\n")
    print("Welcome! This system calculates a student's expected Final Score")
    print("by utilizing historical weights trained against Midterm performance.")
    print("--------------------------------------------------")
    
    while True:
        user_input = input("\nEnter Midterm Score (or type 'exit' to close the app): ").strip()
        
        if user_input.lower() == 'exit':
            print("\nExiting Score Prediction Interface. Happy Engineering!")
            break
            
        try:
            # Parse user input to a scalar floating-point value
            score_val = float(user_input)
            
            # Constraint safety boundary check
            if score_val < 0 or score_val > 100:
                print("[Invalid Range]: Please enter a normalized grade score between 0 and 100.")
                continue
                
            # Restructure user input as a validated Pandas Dataframe to match training columns
            input_df = pd.DataFrame([[score_val]], columns=['Midterm_Score'])
            
            # Run forward inference pass
            predicted_final = regressor.predict(input_df)[0]
            
            # Clip predictions to human-grade scale limits (0-100)
            final_bounded = max(0.0, min(100.0, predicted_final))
            
            print(f"🔮 Predicted Final Exam Score: {final_bounded:.2f} / 100")
            print("--------------------------------------------------")
            
        except ValueError:
            print("[Syntax Error]: Please provide a valid numeric value or type 'exit'.")

if __name__ == "__main__":
    launch_prediction_app()