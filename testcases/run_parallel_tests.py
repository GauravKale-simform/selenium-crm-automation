# This is the code to generate the logs for the test cases while running the docker.
# import sys
# import os
# from multiprocessing import Process
# from utilities.logger import logGen
# import subprocess
# logger = logGen.logger()
# test_cases = [
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "chrome",
#      "http://172.20.0.2:5555"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "firefox",
#      "http://172.20.0.3:5555"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "edge",
#      "http://172.20.0.4:5555"),
# ]
#
# hub_url = "http://172.16.5.179:4444/wd/hub"
#
# def run_test(test_case, browser, node_url):
#     logger.info(f"Starting test: {test_case} on browser: {browser} at node: {node_url}")
#     result = subprocess.run(
#         f"pytest -n 3 {test_case} --browser={browser} --hub_url={hub_url} --node_url={node_url}",
#         shell=True,
#         capture_output=True,
#         text=True
#     )
#     if result.returncode == 0:
#         logger.info(f"Test Passed: {test_case} on browser: {browser}")
#     else:
#         logger.error(f"Test Failed: {test_case} on browser: {browser}\n{result.stderr}")
#
# if __name__ == "__main__":
#     processes = []
#     for test_case, browser, node_url in test_cases:
#         process = Process(target=run_test, args=(test_case, browser, node_url))
#         processes.append(process)
#         process.start()
#     for process in processes:
#         process.join()

#executing test cases simultaneously on each browser at the same time
import os
from multiprocessing import Process

test_cases = [
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_001_verify_correct_url.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_001_verify_correct_url.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_001_verify_correct_url.py", "edge", "http://172.20.0.4:5555"),

    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_002_login.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_002_login.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_002_login.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "edge", "http://172.20.0.4:5555"),
    #
    ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_004_add_new_contact.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_004_add_new_contact.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_004_add_new_contact.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_005_add_new_calender.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_006_add_new_deals.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_006_add_new_deals.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_006_add_new_deals.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_007_add_new_tasks.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_007_add_new_tasks.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_007_add_new_tasks.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_008_add_new_cases.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_008_add_new_cases.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_008_add_new_cases.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_009_add_new_calls.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_009_add_new_calls.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_009_add_new_calls.py", "edge", "http://172.20.0.4:5555"),
    #
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_010_add_new_document.py", "chrome", "http://172.20.0.2:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_010_add_new_document.py", "firefox", "http://172.20.0.3:5555"),
    # ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_010_add_new_document.py", "edge", "http://172.20.0.4:5555"),
]

hub_url = "http://172.16.5.179:4444/wd/hub"

def run_test(test_case, browser, node_url):
    os.system(f"pytest -n 3 {test_case} --browser={browser} --hub_url={hub_url} --node_url={node_url}")

if __name__ == "__main__":
    processes = []
    for test_case, browser, node_url in test_cases:
        process = Process(target=run_test, args=(test_case, browser, node_url))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

#for docker executing test cases one by one

# import os
#
# test_cases = [
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "chrome", "http://172.20.0.2:5555"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "firefox","http://172.20.0.3:5555"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "edge","http://172.20.0.4:5555"),
#
# ]
# hub_url = "http://172.16.5.179:4444/wd/hub"
#
#
# for test_case, browser, node_url in test_cases:
#     os.system(f"pytest -n 3 {test_case} --browser={browser} --hub_url={hub_url} --node_url={node_url} &")



# import os
#
# test_cases = [
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_001_verify_correct_url.py", "edge", "http://172.17.80.1:5557"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_002_login.py", "edge", "http://172.17.80.1:5557"),
#     ("C://Users//gaurav//Desktop//Automation//CRM_Project//testcases//test_003_add_new_company.py", "edge", "http://172.17.80.1:5557"),
# ]
# hub_url = "http://172.16.5.179:4444/wd/hub"
#
#
# for test_case, browser, node_url in test_cases:
#     os.system(f"pytest {test_case} --browser={browser} --hub_url={hub_url} --node_url={node_url} &")



# import os
#
# test_cases = [
#     ("test_001_verify_correct_url.py", "chrome", "http://172.16.4.144:5555"),
#     ("test_002_login.py", "chrome", "http://172.16.4.144:5555"),
#     ("test_003_add_new_company.py", "chrome", "http://172.16.4.144:5555"),
#
#     ("test_001_verify_correct_url.py", "firefox", "http://172.16.6.102:5556"),
#     ("test_002_login.py", "firefox", "http://172.16.6.102:5556"),
#     ("test_003_add_new_company.py", "firefox", "http://172.16.6.102:5556"),
#
#     ("test_001_verify_correct_url.py", "edge", "http://172.17.80.1:5557"),
#     ("test_002_login.py", "edge", "http://172.17.80.1:5557"),
#     ("test_003_add_new_company.py", "edge", "http://172.17.80.1:5557"),
# ]
# hub_url = "http://172.16.5.179:4444/wd/hub"
#
#
# for test_case, browser, node_url in test_cases:
#     os.system(f"pytest -n 3 {test_case} --browser={browser} --hub_url={hub_url} --node_url={node_url} &")


# import os
#
# test_cases = [
#     ("test_001_verify_correct_url.py", "firefox"),
#     ("test_001_verify_correct_url.py", "chrome"),
#     ("test_001_verify_correct_url.py","edge"),
#
#     ("test_002_login.py", "firefox"),
#     ("test_002_login.py", "chrome"),
#     ("test_002_login.py", "edge"),
#
#     ("test_003_add_new_company.py", "firefox"),
#     ("test_003_add_new_company.py", "chrome"),
#     ("test_003_add_new_company.py", "edge")
# ]
#
# hub_url = "http://172.16.5.179:4444/wd/hub"
#
# # Run tests in parallel
# for test_case, browser in test_cases:
#     os.system(f"pytest -n 3 {test_case} --browser={browser} --hub_url={hub_url} &")
