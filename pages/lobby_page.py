import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class LobbyPage(Page):
    """
    Chat page
    """

    url = '/chat/lobby'

    def open_rooms_list(self):
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
        for i in self.context.driver.find_elements_by_css_selector('.aui-button-light '):
            if i.text == 'Rooms':
                i.click()

    def open_room_by_name(self,name):
        for i in self.context.driver.find_elements_by_css_selector('.hc-lobby-list-names span.groupchat'):
            if i.text == name:
                i.click()
                break
        try:
            self.context.wait.until(lambda driver: driver.find_element_by_class_name('hc-chat-msg'))
        except TimeoutException:
            pass

    def room_send_msg(self, msg):
        msg_field = self.context.driver.find_element_by_id('hc-message-input')
        if msg == '/clear':
            msg_field.send_keys('/clear')
            msg_field.send_keys(Keys.RETURN)
            self.context.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'hc-chat-msg')))
        else:
            self.context.wait.until(lambda driver: driver.find_element_by_id('hc-message-input'))
            msg_field.send_keys(msg+Keys.RETURN)

    def check_is_ping(self, msg):
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector('.msg-line.msg-line div.msg-line'))
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector('.notification.msg-line'))
        msgs = self.context.driver.find_elements_by_css_selector('.msg-line.msg-line div.msg-line')
        ment_names = msgs[len(msgs)-1].find_element_by_css_selector('span').text
        return msg == msgs[len(msgs)-1].text[len(ment_names)+1:]

    room_name = str(randint(1, 999))

    def create_room(self):
        self.find_btn().click()
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'create-room-name')))

    def find_btn(self):
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Create a room"]')))
        return self.context.driver.find_element_by_xpath('//span[text()="Create a room"]')

    def find_set_name(self):
        return self.context.driver.find_element_by_id('create-room-name')

    def set_name(self):
        self.find_set_name().send_keys(LobbyPage.room_name)
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Create room"]')))

    def find_create_btn(self):
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Create room"]')))
        return self.context.driver.find_element_by_xpath('//button[text()="Create room"]')

    def click_create_room(self):
        self.find_create_btn().click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="hc-glance clickable"]')))

    def find_add_member(self):
        return self.context.driver.find_element_by_xpath('//*[@class="hc-glance clickable"]')

    def click_add_member(self):
        import time
        time.sleep(3)
        self.context.driver.find_element_by_id('room-actions-btn').click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Invite People"]')))
        self.context.driver.find_element_by_xpath('//a[text()="Invite People"]').click()

    def send_invite(self):
        self.context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s2id_invite-users-people')))
        self.context.driver.find_element_by_css_selector('#s2id_invite-users-people').click()
        self.context.driver.find_element_by_xpath(
            '//div[contains(@class,"select2-drop")]//div[text()="ivan savarin test"]').click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Invite people"]')))

    def find_invite(self):
        return self.context.driver.find_element_by_xpath('//*[@id="invite-users-dialog"]/footer/div[1]/button[1]')

    def invite(self):
        self.find_invite().click()

    def accept_invite(self):
        from selenium.webdriver.common.keys import Keys
        try:
            room_xpath = '//div[contains(@class,"hc-lobby-panel-content")]//span[text()="'+LobbyPage.room_name+'"]'
            self.context.driver.find_element_by_xpath(room_xpath).click()
            self.context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="msg-line"]')))
        except:
            self.context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="msg-line"]')))

    def delete_room(self):
        try:
            room_xpath = '//div[contains(@class,"hc-lobby-panel-content")]//span[text()="'+LobbyPage.room_name+'"]'
            self.context.driver.find_element_by_xpath(room_xpath).click()
            self.context.driver.find_element_by_id('room-actions-btn').click()
            self.context.driver.find_element_by_css_selector('.delete-room-action').click()
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete room"]')))
            self.context.driver.find_element_by_xpath('//button[text()="Delete room"]').click()
        except:
            self.context.driver.find_element_by_id('room-actions-btn').click()
            self.context.driver.find_element_by_css_selector('.delete-room-action').click()
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete room"]')))
            self.context.driver.find_element_by_xpath('//button[text()="Delete room"]').click()

    def open_alias_room(self):
        self.find_alias_room().click()

    def find_alias_room(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        return self.context.driver.find_element_by_xpath("//a[@aria-label='Alias room']")

    def input_comands_in_field(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'hc-message-input')))
        self.find_input_field().send_keys('/clear')
        self.find_input_field().send_keys(Keys.ENTER)

        self.find_input_field().send_keys('/alias set @gtest @HenaYamkoviy')
        self.find_input_field().send_keys(Keys.ENTER)
        self.find_input_field().send_keys(Keys.ENTER)

    def find_input_field(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'hc-message-input')))
        return self.context.driver.find_element_by_id('hc-message-input')

    def find_input_alias(self):
        self.context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.notification.msg-line')))
        return self.context.driver.find_elements_by_css_selector('.notification.msg-line')

    def get_text_from_alias_bot(self):
        for n in self.find_input_alias():
            print(n.text)
            for word in n.text.split():
                if '@gtest' in word:
                    return True

    def chat_adding_alias(self):
        self.input_comands_in_field()
        return self.get_text_from_alias_bot()

    def random_click(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        self.find_element_for_random_click().click()

    def find_element_for_random_click(self):
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Filter']")))
        return self.context.driver.find_element_by_xpath("//input[@placeholder='Filter']")

    def open_alias_menu(self):
        self.find_plus_button().click()

    def click_for_focus_near_plus_button(self):
        self.context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#hc-message-input')))
        self.context.driver.find_element_by_css_selector('textarea#hc-message-input').click()

    def find_plus_button(self):
        self.click_for_focus_near_plus_button()
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.hc-dropdown>button#input_actions_dropdown-trigger')))
        return self.context.driver.find_element_by_css_selector('div.hc-dropdown>button#input_actions_dropdown-trigger')

    def open_menu(self):
        self.find_button_in_dropdown_menu().click()

    def find_button_in_dropdown_menu(self):
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, ('//a[@data-addon_key="hc-alias"]'))))
        return self.context.driver.find_element_by_xpath('//a[@data-addon_key="hc-alias"]')

    def focus_at_alias_config_window(self):
        time.sleep(3)
        return self.context.wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'hc-addon-iframe')))

    def open_config(self):
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div>div>.aui-button.aui-button-link')))
        self.context.driver.find_element_by_css_selector('div>div>.aui-button.aui-button-link').click()

    def put_data_into_the_frame(self):
            self.open_config()
            self.input_data_in_alias_form()
            self.input_data_in_alias_name_form()

    def input_data_in_alias_form(self):
        self.find_alias_form().send_keys("@test")

    def find_alias_form(self):
        self.context.wait.until(EC.presence_of_element_located((By.NAME, 'alias')))
        return self.context.driver.find_element_by_name('alias')

    def input_data_in_alias_name_form(self):
        self.find_form_name().send_keys('HenaYamkoviy')
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="HenaYamkoviy"]')))
        self.adding_data()

    def adding_data(self):
        self.find_form_name().send_keys(Keys.ARROW_DOWN)
        self.find_form_name().send_keys(Keys.ARROW_DOWN)
        self.find_form_name().send_keys(Keys.ENTER)
        self.find_form_name().send_keys(Keys.ENTER)

    def find_form_name(self):
        return self.context.driver.find_element(By.CSS_SELECTOR, 'div.Select-input>input')

    def find_added_element(self):
        self.context.wait.until(
            lambda driver: self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions'))
        table = self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions')

        result = False
        for element in table:
            if element.text == "@HenaYamkoviy":
                result = True
        return result

    def delete_ico(self):
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.aui-icon.aui-icon-small.aui-iconfont-delete.delete")))
        return self.context.driver.find_elements_by_css_selector('a.aui-icon.aui-icon-small.aui-iconfont-delete.delete')

    def click_delete_ico(self):
        for delete in self.delete_ico():
            delete.click()
