from selene import browser, have, be, command, query
from selenium.webdriver import Keys
import os


def test_student_registration_form():
    # Open page using base URL https://demoqa.com/automation-practice-form/
    browser.open('/')

    # Check we are on the correct page by text 'Student Registration Form'
    browser.element('[class=practice-form-wrapper] h5').should(have.exact_text('Student Registration Form'))

    # Remove advertising banner
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    # Scroll browser window to the end of the page
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # Fill in form elements
    browser.element('#firstName').should(be.blank).type('Jon')
    browser.element('#lastName').should(be.blank).type('Dir')
    browser.element('[for=gender-radio-1]').should(be.clickable).click()
    browser.element('[placeholder="Mobile Number"]').should(be.blank).type('5296846163')
    browser.element('#userEmail').should(be.blank).type('jondir@example.com')
    browser.element('#dateOfBirthInput').send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01 May 2000',
        Keys.ENTER
    )
    # Type 'com' to see dropdown menu
    browser.element('#subjectsInput').should(be.blank).type('com')

    # Click on "Computer Science" element in dropdown menu
    browser.all('.subjects-auto-complete__menu-list>.subjects-auto-complete__option').element_by\
        (have.exact_text('Computer Science')).click()

    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()

    browser.element('#uploadPicture').send_keys(os.getcwd() + r'\gl.jpg')
    browser.element('#currentAddress').should(be.blank).type\
        ('This is\nmy current\naddress\nin New York\n USA')

    browser.element('#react-select-3-input').send_keys("a")
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()

    browser.element('#react-select-4-input').send_keys("a")
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').click()



