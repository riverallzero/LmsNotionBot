import telegram
from telegram.ext import Updater, MessageHandler
from telegram.ext import Filters
import lecfinder
from selenium import webdriver
import time


class NotionTelegramBot:
    def __init__(self):
        self.lf = lecfinder.LecFinder()

        token = '5513740361:AAHKlEFGN8ySC7dLpkThZF4-XjnOjus-mSQ'
        self.telegramid = '텔레그램 채팅 아이디'
        self.bot = telegram.Bot(token=token)

        updater = Updater(token=token, use_context=True)
        self.dispatcher = updater.dispatcher
        updater.start_polling()


    def handler(self, update, context):
        user_text = update.message.text
        if user_text == "할일":
            self.bot.send_message(chat_id=self.telegramid, text='로딩중∙∙∙')
            driver = webdriver.Chrome(r'chromedriver.exe 저장 위치')
            url = 'https://ieilms.jbnu.ac.kr/'
            driver.get(url)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="id"]').send_keys(self.lf.lms_id)
            driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(self.lf.lms_pw)

            loginbtn = driver.find_element_by_xpath('//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input')
            loginbtn.click()
            time.sleep(2)

            report1 = self.lf.report1_result(driver)
            report2 = self.lf.report2_result(driver)
            video1 = self.lf.video1_result(driver)
            video2 = self.lf.video2_result(driver)
            quiz1 = self.lf.quiz1_result(driver)
            quiz2 = self.lf.quiz2_result(driver)

            if report1 and report2 == '레포트는 없습니다.':
                self.bot.send_message(chat_id=self.telegramid, text='[레포트] 완료')
            else:
                if report1 != '레포트는 없습니다.':
                    self.send_telegram_msg(report1)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec1))
                if report2 != '레포트는 없습니다.':
                    self.send_telegram_msg(report2)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec2))

            if quiz1 and quiz2 == '퀴즈는 없습니다.':
                self.bot.send_message(chat_id=self.telegramid, text='[퀴즈] 완료')
            else:
                if quiz1 != '퀴즈는 없습니다.':
                    self.send_telegram_msg(quiz1)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec1))
                if quiz2 != '퀴즈는 없습니다.':
                    self.send_telegram_msg(quiz2)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec2))


            if video1 and video2 == '영상은 없습니다.':
                self.bot.send_message(chat_id=self.telegramid, text='[강의 영상] 완료')
            else:
                if video1 != '영상은 없습니다.':
                    self.send_telegram_msg(video1)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec1))
                if video2 != '영상은 없습니다.':
                    self.send_telegram_msg(video2)
                    self.bot.send_message(chat_id=self.telegramid, text='-> https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.lf.groupid_lec2))

            logout = driver.find_element_by_xpath('//*[@id="centerTop"]/div[2]/ul/li/div/a[4]')
            logout.click()
            time.sleep(2)


    def send_telegram_msg(self, report2):
        if isinstance(report2, list):
            for video_report in report2:
                self.bot.send_message(chat_id=self.telegramid, text='[기한: {}]\n{}'.format(video_report[1], video_report[0]))
        else:
            self.bot.send_message(chat_id=self.telegramid, text='{}'.format(report2))


def main():
    notionbot = NotionTelegramBot()
    echo_handler = MessageHandler(Filters.text, notionbot.handler)
    notionbot.dispatcher.add_handler(echo_handler)


if __name__ == '__main__':
    main()
