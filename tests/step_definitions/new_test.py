# import time
#
# from selenium import webdriver
#
#
# service=webdriver.EdgeService("C:\\Users\\pradeep_kumar_sharma\\PycharmProjects\\Testing\\browsers\\msedgedriver.exe")
# driver = webdriver.Edge(service=service)
#
#
# driver.maximize_window()
# driver.get("https://artoftesting.com/samplesiteforselenium")
#
#
# print("Completed")
# driver.quit()



file_path = 'test_automation_practice_steps.py'

with open(file_path, 'rb') as file:
    content = file.read()

clean_content = content.replace(b'\x00', b'')

with open(file_path, 'wb') as file:
    file.write(clean_content)