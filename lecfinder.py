import pandas as pd


class LecFinder:
    def __init__(self):
        self.groupid_lec1 = 강의 group_id(5자리수)
        self.groupid_lec2 = 강의 group_id(5자리수)

        self.lms_id = 'LMS 로그인 아이디'
        self.lms_pw = 'LMS 로그인 비밀번호'

    def lec1_report(self, driver):
        driver.get('https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.groupid_lec1))

        # 레포트 개수
        elements = driver.find_elements_by_css_selector('#borderBox > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 레포트 리스트
            title = []
            date = []
            submit = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                submitresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[4]'.format(i)).text
                submit.append(str(submitresult))

            df = pd.DataFrame({'과제제목': title,
                               '제출기간': date,
                               '제출여부': submit})
            return df
        else:
            return '레포트는 없습니다.'


    def lec2_report(self, driver):
        driver.get('https://ieilms.jbnu.ac.kr/paper/paperList.jsp?group_id={}'.format(self.groupid_lec2))

        # 레포트 개수
        elements = driver.find_elements_by_css_selector('#borderBox > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 레포트 리스트
            title = []
            date = []
            submit = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                submitresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[4]'.format(i)).text
                submit.append(str(submitresult))

            df = pd.DataFrame({'과제제목': title,
                               '제출기간': date,
                               '제출여부': submit})
            return df
        else:
            return '레포트는 없습니다.'


    def lec1_video(self, driver):
        driver.get(
            'https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp?group_id={}'.format(self.groupid_lec1))

        # 비디오 개수
        elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 비디오 리스트
            title = []
            date = []
            attendence = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                attendenceresult = driver.find_element_by_xpath(
                    '//*[@id="dataBox"]/table/tbody/tr[{}]/td[6]'.format(i)).text
                attendence.append(str(attendenceresult))

            ds = pd.DataFrame({'강의제목': title,
                               '인정기간': date,
                               '출석여부': attendence})

            return ds

        else:
            return '강의는 없습니다.'


    def lec2_video(self, driver):
        driver.get('https://ieilms.jbnu.ac.kr/attend/videoDataViewAttendListStudent.jsp?group_id={}'.format(self.groupid_lec2))

        # 비디오 개수
        elements = driver.find_elements_by_css_selector('#dataBox > table > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 비디오 리스트
            title = []
            date = []
            attendence = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="dataBox"]/table/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                attendenceresult = driver.find_element_by_xpath(
                    '//*[@id="dataBox"]/table/tbody/tr[{}]/td[6]'.format(i)).text
                attendence.append(str(attendenceresult))

            ds = pd.DataFrame({'강의제목': title,
                               '인정기간': date,
                               '출석여부': attendence})

            return ds

        else:
            return '강의는 없습니다.'


    def lec1_quiz(self, driver):
        driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id={}'.format(self.groupid_lec1))

        # 퀴즈 개수
        elements = driver.find_elements_by_css_selector('#borderBox > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 퀴즈 리스트
            title = []
            date = []
            submit = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                submitresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[4]'.format(i)).text
                submit.append(str(submitresult))

            dc = pd.DataFrame({'퀴즈제목': title,
                               '기간': date,
                               '제출여부': submit})

            return dc
        else:
            return '퀴즈는 없습니다.'


    def lec2_quiz(self, driver):
        driver.get('https://ieilms.jbnu.ac.kr/quiz/quizList.jsp?group_id={}'.format(self.groupid_lec2))

        # 퀴즈 개수
        elements = driver.find_elements_by_css_selector('#borderBox > tbody > tr')
        elementcount = len(elements)
        if elementcount >= 1:
            # 퀴즈 리스트
            title = []
            date = []
            submit = []
            for i in range(1, elementcount + 1):
                titleresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[2]'.format(i)).text
                title.append(str(titleresult))
                dateresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[3]'.format(i)).text
                date.append(str(dateresult))
                submitresult = driver.find_element_by_xpath('//*[@id="borderBox"]/tbody/tr[{}]/td[4]'.format(i)).text
                submit.append(str(submitresult))

            dc = pd.DataFrame({'퀴즈제목': title,
                               '기간': date,
                               '제출여부': submit})

            return dc
        else:
            return '퀴즈는 없습니다.'


    def report1_result(self, driver):
        df = self.lec1_report(driver)
        if isinstance(df, str):
            return '레포트는 없습니다.'
        else:
            count = len(df['과제제목'])
            count_correct = []
            for s in range(count):
                if df['제출여부'][s] == '미제출':
                    count_correct.append(df['과제제목'][s] + df['제출기간'].str[24:29][s])
            if len(count_correct) >= 1:
                return count_correct
            return '레포트는 없습니다.'


    def report2_result(self, driver):
        df = self.lec2_report(driver)
        if isinstance(df, str):
            return '레포트는 없습니다.'
        else:
            count = len(df['과제제목'])
            count_correct = []
            for s in range(count):
                if df['제출여부'][s] == '미제출':
                    count_correct.append(df['과제제목'][s] + df['제출기간'].str[24:29][s])
            if len(count_correct) >= 1:
                return count_correct
            return '레포트는 없습니다.'


    def video1_result(self, driver):
        ds = self.lec1_video(driver)
        if isinstance(ds, str):
            return '영상은 없습니다.'
        else:
            count = len(ds['강의제목'])
            count_correct = []
            for s in range(count):
                if ds['출석여부'][s] == '결석':
                    count_correct.append((ds['강의제목'][s] + ' 강의', ds['인정기간'].str[24:29][s]))
            if len(count_correct) >= 1:
                return count_correct
            return '영상은 없습니다.'


    def video2_result(self, driver):
        ds = self.lec2_video(driver)
        if isinstance(ds, str):
            return '영상은 없습니다.'
        else:
            count = len(ds['강의제목'])
            count_correct = []
            for s in range(count):
                if ds['출석여부'][s] == '결석':
                    count_correct.append((ds['강의제목'][s] + ' 강의', ds['인정기간'].str[24:29][s]))
            if len(count_correct) >= 1:
                return count_correct
            return '영상은 없습니다.'


    def quiz1_result(self, driver):
        dc = self.lec1_quiz(driver)
        if isinstance(dc, str):
            return '퀴즈는 없습니다.'
        else:
            count = len(dc['퀴즈제목'])
            count_correct = []
            for s in range(count):
                if dc['제출여부'][s] == '미제출':
                    count_correct.append(dc['퀴즈제목'][s] + dc['기간'].str[24:29][s])
            if len(count_correct) >= 1:
                return count_correct
            return '퀴즈는 없습니다.'


    def quiz2_result(self, driver):
        dc = self.lec2_quiz(driver)
        if isinstance(dc, str):
            return '퀴즈는 없습니다.'
        else:
            count = len(dc['퀴즈제목'])
            count_correct = []
            for s in range(count):
                if dc['제출여부'][s] == '미제출':
                    count_correct.append(dc['퀴즈제목'][s] + dc['기간'].str[24:29][s])
            if len(count_correct) >= 1:
                return count_correct
            return '퀴즈는 없습니다.'
