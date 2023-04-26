import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from fivefingurepom import *

@given(u': open CE browser')
def openbrowser (context):
    context.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")


@when(u': Enter url')

def urlEnter (context):
    context.driver.get("http://mitintech.com/admin/login/?next=/admin/")
    context.driver.maximize_window()
    time.sleep(2)


@then(u': Enter username  and password')

def step_impl (context):
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    context.driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(2)

@then(u': Click on Login button')
def step_impl (context):
    context.driver.find_element(By.XPATH,'//input[@type="submit"]').click()
    time.sleep(2)

# @then(u'new page shouid be displayed')
# def step_impl(context):
#     title = context.driver.title
#     assert title  == "Five Fingers Admin | Five Fingers admin site"


@given(u': click on the class icon')
def step_impl(context):
    # context.driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/td/a').click()
    context.driver.find_element(By.XPATH,'//a[@href="/admin/master/tblclass/add/"]').click()

# @given(u': click on the class icon')
# def step_impl(context):
#     context.driver.title


@then(u': click on the name text box and write class name')
def step_impl(context):
    context.driver.find_element(By.NAME,'name').send_keys(classname)


@then(u': click on the save button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//input[@value="Save"]').click()


@given(u': click on the subject icon')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//a[@href="/admin/master/tblbookseries/add/"]').click()



@then(u': click on the name text box and write subject name')
def step_impl(context):
    context.driver.find_element(By.NAME,'name').send_keys(subjectname)





@given(u': click on the book series icon')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//a[@href="/admin/master/tblbookseries/add/"]').click()


@then(u': click on the subject text box and select the subject')
def step_impl(context):
    context.driver.find_element(By.NAME,'subject').click()


@then(u': click on the name text box and write the book series name')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME,'vTextField').send_keys(bookseries)


@given(u': click on the chapter icon')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//a[@href="/admin/master/tblchapter/add/"]').click()


@then(u': click on the name text box and write chapter name')
def step_impl(context):
    context.driver.find_element(By.NAME,'name').send_keys(chaptername)


@then(u': click on the subject text box and select subject name')
def step_impl(context):
    context.driver.find_element(By.NAME,'subject').click()


@then(u': click on the bookseries text box and select bookseries')
def step_impl(context):
    context.driver.find_element(By.NAME,'bookseries').click()


@then(u': click on the classid textbox and select classid')
def step_impl(context):
    context.driver.find_element(By.NAME,'classid').click()














