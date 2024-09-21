from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

def calculate_grades(prelim):
    """
    Calculate required grades based on the given prelim score.
    
    This function determines the grades needed for passing the course
    and potentially making the Dean's list.
    
    Parameters:
    prelim (float): The student's preliminary grade (0-100)
    
    Returns:
    dict: A dictionary containing calculated grades and status information
    """
    
    # Define grade weights and thresholds
    prelim_weight = 0.2   # Prelim accounts for 20% of final grade
    midterm_weight = 0.3  # Midterm accounts for 30% of final grade
    final_weight = 0.5    # Final exam accounts for 50% of final grade
    passing_grade = 75    # Minimum grade required to pass the course
    deans_list_grade = 90 # Minimum grade required for Dean's list

    # Calculate required midterm grade for passing
    required_midterm = (passing_grade - (prelim * prelim_weight)) / (midterm_weight + final_weight)
    
    # Calculate required final grade for passing
    required_final = (passing_grade - (prelim * prelim_weight) - (required_midterm * midterm_weight)) / final_weight

    # Check if it's possible to pass the course
    can_pass = 0 <= required_midterm <= 100 and 0 <= required_final <= 100

    # Calculate grades needed for Dean's list
    deans_midterm = (deans_list_grade - (prelim * prelim_weight)) / (midterm_weight + final_weight)
    deans_final = (deans_list_grade - (prelim * prelim_weight) - (deans_midterm * midterm_weight)) / final_weight

    # Check if achieving Dean's list is possible
    deans_list_possible = deans_midterm <= 100 and deans_final <= 100

    # Return a dictionary with all calculated values
    return {
        "prelim": prelim,
        "required_midterm": round(required_midterm, 2),
        "required_final": round(required_final, 2),
        "can_pass": can_pass,
        "deans_midterm": round(deans_midterm, 2),
        "deans_final": round(deans_final, 2),
        "deans_list_possible": deans_list_possible
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle requests to the main page of the web application.
    
    This function processes both GET and POST requests:
    - GET: Display the initial form
    - POST: Process the submitted form and display results
    
    Returns:
    str: Rendered HTML template with form and/or results
    """
    
    result = None  # Will store calculation results
    error = None   # Will store any error messages

    if request.method == 'POST':
        try:
            # Attempt to get and validate the prelim grade from the form
            prelim = float(request.form['prelim'])
            if 0 <= prelim <= 100:
                # If valid, calculate and store the results
                result = calculate_grades(prelim)
            else:
                # If out of range, set an error message
                error = "Prelim grade must be between 0 and 100"
        except ValueError:
            # If input can't be converted to float, set an error message
            error = "Invalid input. Please enter a number."

    # Render the template with the form, results (if any), and errors (if any)
    return send_from_directory('', 'index.html')

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)