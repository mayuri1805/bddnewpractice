import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


@given(u'open CE browser')
def openbrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")


@when(u'Enter url')
def urlEnter(context):
    context.driver.get("https://demo.guru99.com/v3/")


@then(u'Check Guru99 Login Page')
def checkPage(context):
    """" Guru99 Bank Home Page """
    title = context.driver.title
    assert title == "Guru99 Bank Home Page"


@then(u'Check Guru99 Login Page "{un}"')
def step_impl(context, un):
    title = context.driver.title
    assert title == un


@when(u'Enter username and password')
def step_impl(context):
    context.driver.find_element(By.NAME, 'uid').send_keys('mngr485684')
    context.driver.find_element(By.NAME, 'password').send_keys('nuzYmah')


@when(u'Click on Login button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'btnLogin').click()


@then(u'Check Guru99 Home Page')
def step_impl(context):
    # /html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee
    # Welcome To Manager's Page of Guru99 Bank
    # dr = webdriver.Chrome(executable_path="")
    errmsg=context.driver.title
    assert errmsg.strip() == " Guru99 Bank Manager HomePage ".strip()
    # raise NotImplementedError(u'STEP: Then Check Guru99 Home Page')

# @when(u'Enter username '{un}' and password \'nuzYmah\'')
# def step_impl(context):

#

@when(u'Enter username "{un}" and password "{password}"')
def step_impl(context,un,password):
    context.driver.find_element(By.NAME, 'uid').send_keys(un)
    context.driver.find_element(By.NAME, 'password').send_keys(password)

# @then(u'Click on NewCustomer Link')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on NewCustomer Link')
#
#
# @then(u'Enter NewCustomer Details')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Enter NewCustomer Details')
#
#

#
#
# @then(u'Check Message')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Check Message')


@then(u'Click on EditCustomer Link')
def step_impl(context):

    context.driver.find_element(By.PARTIAL_LINK_TEXT,'Edit Customer').click()
    time.sleep(5)

@then(u'Enter Customer ID "{custid}"')
def step_impl(context,custid):

    context.driver.find_element(By.NAME,'cusid').send_keys(custid)


@then(u'Click on Submit Button')
def step_impl(context):
    # dr = webdriver.Chrome(executable_path="")
    context.driver.find_element(By.NAME,'AccSubmit').click()

@then(u'Check Edit Customer Page')
def step_impl(context):
    # create alert object
    alert = Alert(context.driver)

    # get alert text
    errmsg =alert.text

    # accept the alert
    alert.accept()
    time.sleep(5)
    assert errmsg == "You are not authorize to edit this customer!!"




# You are not authorize to edit this customer!!