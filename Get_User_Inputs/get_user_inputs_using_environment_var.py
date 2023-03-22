import os

def get_x():
    return os.getenv("X")
 
def get_y():
    return os.getenv("Y")
  
def get_z():
    return os.getenv("Z")

def get_job_name():
    return os.getenv("JOB_NAME")

def get_workspace():
    return os.getenv("WORKSPACE")
    
def display_user_inputs():
    print("Displaying the user selected parameter values:")
    print("X:\t", get_x())
    print("Y:\t", get_y())
    print("Z:\t", get_z())

if __name__ == "__main__":
    # The execution of the script begins from here.
    display_user_inputs()
