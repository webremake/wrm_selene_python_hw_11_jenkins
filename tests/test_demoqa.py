from selene import browser, have, be
from selenium.webdriver import Keys
import os

# BDD = Given, When, Then
"""
Given (дано) — ситуация выглядит вот так: есть какое-то состояние до того, как пользователь вошел в сценарий.
When (когда) — что-то происходит: пользователь совершает какие-то действия.
Then (тогда) — теперь ситуация выглядит по-другому: система реагирует на пользовательские действия.
"""


def test_student_registration_form(browser_control):
    # GIVEN
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper h5').should(have.exact_text('Student Registration Form'))

    """
    # browser.execute_script('document.querySelector("#fixedban").remove()')
    """
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    '''
    # удалять элемент дизайна каким является футер плохо, лучше сделать клик ч-з JS 
    browser.element('footer').execute_script('element.remove()')
    '''


    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')


    # WHEN
    browser.element('#firstName').should(be.blank).type('Jon')
    browser.element('#lastName').should(be.blank).type('Dir')

    browser.element('#userEmail').should(be.blank).type('jondir@example.com')

    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()

    browser.element('#userNumber').should(be.blank).type('5296846163')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1957')
    browser.element(f'.react-datepicker__day--0{12}').click()

    '''
    # если хотим проверить работает ли авто дополнение
    browser.all('.subjects-auto-complete__menu-list>.subjects-auto-complete__option').element_by\
        (have.exact_text('Computer Science')).click()
    '''
    browser.element('#subjectsInput').type('Commerce').press_enter()

    # field Hobbies
    # browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Reading')).should(be.clickable).click()

    # field Picture
    browser.element('#uploadPicture').send_keys(os.getcwd() + r'\gl.jpg')

    # field Current Address
    browser.element('#currentAddress').should(be.blank).with_(set_value_by_js=True).set_value\
        ('This is\nmy current\naddress\nin New York\n USA')

    # field State
    browser.element('#react-select-3-input').send_keys("a")
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()

    # field City
    browser.element('#react-select-4-input').send_keys("a")
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Karnal')).click()
    # end section

    # submit form
    browser.element('#submit').with_(click_by_js=True).click()

    # THEN
    # section CHECK IFRAME TABLE
    # check table header has two columns
    browser.all('.table thead>tr>th').should(have.size(2))

    # check table header cells have correct text
    browser.all('.table thead>tr>th').should(have.exact_texts('Label', 'Values'))

    # check table body has ten columns
    browser.all('.table tbody>tr').should(have.size(10))

    # check table cells in column Value have values entered into the form in the previous steps
    browser.all('.table tbody>tr>td').even.should(have.exact_texts(
        'Jon Dir', 'jondir@example.com', 'Male', '5296846163', '12 May,1957', 'Commerce',
        'Reading', 'gl.jpg', 'This is my current address in New York USA', 'Haryana Karnal'))
    # end section

    # close iframe table
    browser.element('#closeLargeModal').should(be.clickable).click()