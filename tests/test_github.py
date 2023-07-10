import allure
from allure_commons.types import Severity
from selene import browser, have, be


@allure.tag("homework")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "webremake")
@allure.epic("QA.GURU course")
@allure.feature("Allure reports")
@allure.story("Allure with steps and decorator labels")
@allure.link("https://github.com", name="Testing")
def test_github_find_repo_issue_by_number_with_allure_dynamic_steps(browser_control):
    with allure.step("открываем https://github.com/"):
        browser.open('/')
    with allure.step("нажимаем на кнопку Search or jump to"):
        browser.element('.header-search-button').click()

    with allure.step("в строку поиска вводим `/webremake/wrm_selene_python_hw_7` и нажимаем Enter"):
        browser.element('#query-builder-test').type('webremake/wrm_selene_python_hw_7').press_enter()

    with allure.step("на открывшейся странице клакаем на ссылку c текстом `webremake/wrm_selene_python_hw_7`"):
        browser.element('[href="/webremake/wrm_selene_python_hw_7"]').should(be.clickable).click()

    with allure.step("кликаем на таб `Issues`"):
        browser.element('#issues-tab').should(be.clickable).click()

    with allure.step("проверяем что в списке есть issue с номером `#2"):
        # assert browser.elements('.opened-by').should(have.exact_texts(''))
        #assert browser.elements('[id^="issue_"][id$="_link"]').should(have.size_greater_than(3))
        assert browser.all('[id^="issue_"][id$="_link"]').second.should(have.text('tmp_path_factory()'))
