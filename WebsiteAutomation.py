import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import threading
import tkinter as tk

# Global variables
paused = False
execution_event = threading.Event()  # Event to synchronize pause and resume

# Function to handle browser notifications
def handle_browser_notifications(drivers):
    try:
        WebDriverWait(drivers, 1).until(EC.alert_is_present())
        alert = drivers.switch_to.alert()
        alert.accept()
    except Exception:
        pass

# Function to pause or resume the program
def pause_resume_program():
    global paused
    if paused:
        
        paused = False
        pause_button.config(text="Pause")
        execution_event.set()  
    else:
        # If the program is running, pause execution
        paused = True
        pause_button.config(text="Start")
        

# Get the directory of the current script file
script_directory = os.path.dirname(__file__)

# Define the folder path where the report file should be saved
Report_folder = os.path.join(script_directory, "Report_folder")

# Ensure the folder exists, create it if it doesn't
if not os.path.exists(Report_folder):
    os.makedirs(Report_folder)

# Generate the current datetime string to include in the report file name
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the file path for the report file including the datetime
report_file = os.path.join(Report_folder, f"Report_{current_datetime}.html")

with open(report_file, "a") as f:

    f.write("<head><meta http-equiv='content-type' content='text/html; charset=UTF-8'' /><style>div{border:1px solid white;border-bottom:1px solid gray;padding:1px}a{text-decoration:none;color:white;}a.INFO{color:black}a.START,a.STOP{color:black;font-weight:bold;}div.INFO{background-color:white}div.SUCCESS{background-color:green;color:white}div.FAILURE,div.ERROR{background-color:red;color:white}a.CUSTOM, a.CUSTOM2, a.CUSTOM4{color:black}div.CUSTOM{background-color:yellow;}div.CUSTOM1{background-color:orange;}div.CUSTOM2{background-color:#EFEFEF;}div.CUSTOM3{background-color:green;}div.CUSTOM4{background-color:violet;}div.CUSTOM5{background-color:indigo;}a.SCRIPT{text-decoration:underline;}span.extra{color:#CCC;}div.SKIPPED{background-color:#eed;}a.SKIPPED{color:gray;}table{border-top:1px solid gray;border-right:1px solid gray;border-spacing:0px;border-collapse:collapse;}td{border-bottom:1px solid gray;border-left:1px solid gray;padding:5px;text-align:left;}td a.SCRIPT{float:left;}tr.FAILURE{background-color:red;color:white;}tr.SUCCESS{background-color:green;color:white;}tr.vc{background-color:#8A1805;color:white;}tr.vc2{background-color:#8C8E8E;color:white;}a{color:white;}table, th, td {border: 1px solid black;}</style><h1 style='font-family:verdana;font-size:25px;margin-top:16px;margin-left:5px;margin-bottom:25px;'class='heady'>Test Report</h1></head><body style='background-color:powderblue;'><table class='summary'><tr class='vc'><td>Sr. No.</td><td>Title_ID</td><td>Date and Time</td><td>Result</td></tr>")

        
        
# Function to log status and error messages to HTML file and update main row status
def log_status_to_html(status, main_row, main_title):
    if status == 'FAILURE':
        main_row['Status'] = 'FAILURE'
    else:
        main_row['Status'] = 'SUCCESS'

    # Get current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(report_file, "a") as f:
        f.write("<tr class='{}'>".format(status))
        f.write(f"<td>{main_title + 1}</td>")  
        f.write(f"<td>{main_row['Title/ID']}</td>")
        f.write(f"<td>{now}</td>")
        f.write(f'<td>{status}</td>') 
        f.write("</tr>")
        
        






# Function to execute main program
def main_execution(drivers):
    global paused
    while True:
        if not paused:
            main_status_dict = {}  # Dictionary to store the status of each main title
            for main_title in range(last_row_main):
                print("main", main.loc[main_title])
                main_row = main.loc[main_title]
                if paused:
                    execution_event.clear()  # Clear the event to pause execution
                    execution_event.wait()  # Wait until the event is set to resume
                if main.iloc[main_title]["Skip"] == "Yes":
                    continue
                main_status = 'SUCCESS'  # Assume success initially
                for web_title in range(last_row_web):
                    try:
                        if paused:
                            execution_event.clear()  
                            execution_event.wait()  
                        if main.loc[main_title, "Title/ID"] == web.loc[web_title, "Title/ID"]:
                            xpath = web.loc[web_title, "Xpath"]
                            driver_index = web.loc[web_title, "Driver"]  # Get the index of the driver
                            current_driver = drivers[int(driver_index)]
                            
                            if web.loc[web_title, "Function"] == "get":
                                current_driver.get(xpath)
                                handle_browser_notifications(current_driver)
                                time.sleep(web.loc[web_title]["Sleep"])
                            
                            elif web.loc[web_title, "Function"] == "Find_send":
                                value = web.loc[web_title]["Value"]
                                if isinstance(value, pd.Timestamp):
                                    value = value.strftime('%Y-%m-%d')
                                current_driver.find_element("xpath", xpath).send_keys(value)
                                time.sleep(web.loc[web_title]["Sleep"])
                            elif web.loc[web_title, "Function"] == "verify_true":
                                current_driver.find_element("xpath", xpath)
                            elif web.loc[web_title, "Function"] == "verify_false":
                                element_found = False  # Flag to track if the element is found
                                try:
                                    current_driver.find_element("xpath", xpath)
                                    # If element is found, set the flag to True and break out of the loop
                                    element_found = True
                                    break
                                except Exception:
                                    # If element is not found, continue to the next iteration
                                    pass
                                if element_found:
                                    raise Exception("Unexpectedly found element")
                            elif web.loc[web_title, "Function"] == "click":
                                current_driver.find_element("xpath", xpath).click()
                                time.sleep(web.loc[web_title]["Sleep"])
                                
                            elif web.loc[web_title, "Function"] == "scroll":
                                current_driver.execute_script("window.scrollBy(0, 100);")
                                time.sleep(web.loc[web_title]["Sleep"])
                                    
                            else:
                                web.loc[web_title, "Function"] == "wait_until"
                                timeout = 180
                                # Wait until the element is present on the webpage
                                WebDriverWait(current_driver, timeout).until(EC.invisibility_of_element_located(("xpath", xpath)))
                            print("web", web.loc[web_title], "True")
                    except Exception as e:
                        print(f"Error occurred in main_title: {main.loc[main_title]}, web_title: {web.loc[web_title]}", e)
                        main_status = 'FAILURE'
                
                # Store the status for the current main title in the dictionary
                main_status_dict[main_title] = main_status

                # Log status for main_title only if it hasn't been logged before
                if 'Status' not in main_row or main_status != main_row['Status']:
                    log_status_to_html(main_status, main_row, main_title)
                    
                main.loc[main_title, 'Status'] = main_status
            
            with open(report_file, "a") as f:
                f.write("</table></body>")
        else:
            # If paused, wait for the event to resume execution
            execution_event.wait()
            execution_event.clear()  

# Read data from Excel file
sample = pd.read_excel("TestCases.xlsx", sheet_name=['Main', 'Web'])
main = sample["Main"]
web = sample["Web"]

last_row_main = len(main)
last_row_web = len(web)

# Enable all browser notifications
options = Options()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

# Create WebDriver for main browser window
drivers = [webdriver.Chrome(options=options) for _ in range(4)]

# Start the execution thread
execution_thread = threading.Thread(target=main_execution, args=(drivers,))
execution_thread.start()

execution_event.set()



# Create a Tkinter window
root = tk.Tk()
root.title("Pause/Start Button")

# Create a button for pausing/resuming the program
pause_button = tk.Button(root, text="Pause", command=pause_resume_program)
pause_button.pack()

# Set the event to indicate that the program is ready to execute
execution_event.set()

# Start the Tkinter event loop
root.mainloop()