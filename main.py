import time
from multiprocessing import Pool
from random import randint

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options

from settings import (DOMAIN, DRIVER)

# Disable images
options = Options()
images = 'profile.managed_default_content_settings.images'
options.add_experimental_option("prefs",
                                {
                                    images: 2
                                })
data = []


def create_driver():
    try:
        driver = webdriver.Chrome(DRIVER,
                                  chrome_options=options)
    except Exception:
        print('Something went wrong')
    else:
        return driver


def get_all_sections(driver):
    section = []
    for a in driver.find_elements_by_class_name('BrowseSection-submeta'):
        section.append({
            'name': a.text,
            'link': a.get_attribute('href')
        })
    return section


def next_question(driver):
    if driver.find_element_by_id('inputText1').is_displayed():
        driver.find_element_by_id('inputText1').send_keys('45101')
        time.sleep(randint(2, 5))
    buttons = (driver.find_elements_by_css_selector
               ('.Button.NavigationFooter-button'))
    for i in buttons:
        try:
            i.click()
        except ElementNotVisibleException:
            continue
        else:
            return


def get_questions(section_link, driver):
    driver.get(section_link)
    time.sleep(randint(2, 5))
    question_plus_answers = []
    while True:
        time.sleep(randint(2, 5))
        checkbox_items = [item for item in
                          driver.find_elements_by_class_name(
                              'InputCheckbox-label-inner') if
                          not item.text == '']
        question = [question.text for question in
                    driver.find_elements_by_class_name('H4-R') if not
                    question.text == '']
        checkbox = [item.text for item in
                    driver.find_elements_by_class_name(
                        'InputCheckbox-label-inner') if not item.text == '']
        question_plus_answers.append({
            'question': question,
            'checkbox_items': checkbox
        })
        time.sleep(randint(2, 5))
        checkbox_items[0].click()
        time.sleep(randint(2, 5))
        next_question(driver)
        time.sleep(randint(2, 5))
        if (driver.find_element_by_css_selector(
                '.InputContainer-isStandalone').is_displayed()):
            return question_plus_answers


def get_save(section):
    driver = create_driver()
    questions = get_questions(section['link'], driver)  # url to section
    data = {
        'name': section['name'],
        'link': section['link'],
        'questions_and_checkbox_items': []
    }
    for question in questions:
        data['questions_and_checkbox_items'].append({
            'question': question['question'],
            'checkbox_items': question['checkbox_items']
        })
    with open('result.txt', 'a') as doc:
        doc.write(str(data) + '\n')
    time.sleep(randint(2, 5))
    driver.close()


def main():
    driver = create_driver()
    driver.get(DOMAIN)
    sections = get_all_sections(driver)
    driver.close()
    with Pool(10) as pool:
        pool.map(get_save, sections)


if __name__ == '__main__':
    main()
