from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def jkdk_other(userid,psw):
    try:
        # 这部分用来设置运行时不显示浏览器窗口
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # 创建Chrome对象并传入设置信息.
        driver = webdriver.Chrome(options=chrome_options)
        # 操作这个对象.
        driver.get('https://stu.eurasia.edu/yqsb/p/index.html#/stu/login')
        time.sleep(1)
    
        ## 登录
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div[2]/div/input").send_keys(userid) #填入账号
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[2]/div/input").send_keys(psw) #填入密码
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/button").click()
        # 稍作等待
        time.sleep(10)
        ## 进入打卡界面
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div[2]").click()
        time.sleep(1)
        #填写温度
        driver.find_element_by_xpath('//*[@id=\"app\"]/div/div[15]/div/div[2]/div/input').send_keys("36")
        #身体情况
        for n in range(2,8):
            body='//*[@id=\"app\"]/div/div[17]/div['+str(n)+']/div[2]/div/div/div/div/div[2]/div/i'
            driver.find_element_by_xpath(body).click()
            time.sleep(1)
        #提交
        dian='//*[@id=\"app\"]/div/div[23]/button'
        driver.find_element_by_xpath(dian).click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/button[2]").click()
        time.sleep(1)
        driver.quit()  # 关闭浏览器
        print(userid, "已完成今日打卡")
    except:
        driver.quit()  # 关闭浏览器
        print(userid ,"今日已打卡")


def jkdk_4(userid,psw):
    # 这部分用来设置运行时不显示浏览器窗口
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # 创建Chrome对象并传入设置信息.
    driver = webdriver.Chrome(options=chrome_options)
    # 操作这个对象.
    driver.get('https://stu.eurasia.edu/yqsb/p/index.html#/stu/login')
    time.sleep(1)
    ## 登录
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div[2]/div/input").send_keys(userid) #填入账号
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[2]/div/input").send_keys(psw) #填入密码
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/button").click()
    time.sleep(5)
    ## 进入打卡界面
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[1]/div[1]").click()
    time.sleep(1)
    #风险等级
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[14]/div/div[2]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[38]/button[1]").click()
    time.sleep(1)
    #填写温度
    driver.find_element_by_xpath('//*[@id=\"app\"]/div/div[16]/div/div[2]/div/input').send_keys("36")
    time.sleep(1)
    #是否在陕西
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[27]/div[2]/div/div/div/div/div[1]/div/i").click()
    time.sleep(1)
    #提交
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[37]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/button[2]").click()
    time.sleep(1)
    driver.quit()  # 关闭浏览器
    print(userid ,"已完成今日打卡")
    
with open("user.txt", "r") as f:
    lines=[]
    grade=[]
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        userid= line.split(',')[0]
        psw=line.split(',')[1]
        grade = int(line.split(',')[2])
        if grade == 4:
            jkdk_4(userid,psw)
        else:
            jkdk_other(userid,psw)