Feature: five finger Login
  Background: To verify Login Page with parameters
    Given : open CE browser
    When : Enter url
    Then : Enter username  and password
    And : Click on Login button


    Scenario: To add class
      Given : click on the class icon
      Then : click on the name text box and write class name
      Then : click on the save button

    Scenario: To add subject
      Given : click on the subject icon
      Then : click on the name text box and write subject name
      And : click on the save button

    Scenario: To add bookseries
      Given : click on the book series icon
      Then : click on the subject text box and select the subject
      Then : click on the name text box and write the book series name
      Then : click on the save button

    Scenario: To add chapter
      Given : click on the chapter icon
      Then : click on the name text box and write chapter name
      Then : click on the subject text box and select subject name
      Then : click on the bookseries text box and select bookseries
      Then : click on the classid textbox and select classid






