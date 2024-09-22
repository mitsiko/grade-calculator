# app.py

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
