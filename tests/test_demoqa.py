from selene import browser, have, be
from selenium.webdriver import Keys
import os


def test_student_registration_form():
    # Open page using base URL https://demoqa.com
    browser.open('/automation-practice-form')

    # Check we are on the correct page by text 'Student Registration Form'
    browser.element('[class=practice-form-wrapper] h5').should(have.exact_text('Student Registration Form'))

    # Remove advertising banners
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    # Scroll browser window to the end of the page
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # section FILL IN FORM ELEMENTS

    # field Name
    browser.element('#firstName').should(be.blank).type('Jon')
    browser.element('#lastName').should(be.blank).type('Dir')

    # field Email
    browser.element('#userEmail').should(be.blank).type('jondir@example.com')

    # field Gender
    browser.element('[for=gender-radio-1]').should(be.clickable).click()

    # field Mobile
    browser.element('[placeholder="Mobile Number"]').should(be.blank).type('5296846163')

    # field Date of Birth
    browser.element('#dateOfBirthInput').send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01 May 2000',
        Keys.ENTER
    )
    # field Subject
    # Type 'com' to see dropdown menu
    browser.element('#subjectsInput').should(be.blank).type('com')

    # Click on "Computer Science" element in dropdown menu
    browser.all('.subjects-auto-complete__menu-list>.subjects-auto-complete__option').element_by\
        (have.exact_text('Computer Science')).click()

    # field Hobbies
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()

    # field Picture
    browser.element('#uploadPicture').send_keys(os.getcwd() + r'\gl.jpg')

    # field Current Address
    browser.element('#currentAddress').should(be.blank).type\
        ('This is\nmy current\naddress\nin New York\n USA')

    # field State
    browser.element('#react-select-3-input').send_keys("a")
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()

    # field City
    browser.element('#react-select-4-input').send_keys("a")
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Karnal')).click()
    # end section

    # submit form
    browser.element('#submit').click()

    # section CHECK IFRAME TABLE
    # check table header has two columns
    browser.all('.table thead>tr>th').should(have.size(2))

    # check table header cells have correct text
    browser.all('.table thead>tr>th').should(have.exact_texts('Label', 'Values'))

    # check table body has ten columns
    browser.all('.table tbody>tr').should(have.size(10))

    # check table cells in column Value have values entered into the form in the previous steps
    browser.all('.table tbody>tr>td').even.should(have.exact_texts(
        'Jon Dir', 'jondir@example.com', 'Male', '5296846163', '01 May,2000', 'Computer Science',
        'Reading', 'gl.jpg', 'This is my current address in New York USA', 'Haryana Karnal'))
    # end section

    # close iframe table
    browser.element('#closeLargeModal').should(be.clickable).click()
