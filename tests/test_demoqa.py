from selene import browser, have


def test_student_registration_form():
    browser.open('/')

    browser.element('[class=practice-form-wrapper] h5').should(have.exact_text('Student Registration Form'))

    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

