import ctypes
from selenium import webdriver
# from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.action_chains import ActionChains

path = r'O:\Олег\программирование\python\change_windows_wallpaper\2021-03-16_23-17-37.png'


def get_picture(f_id_and_gr_numb):
	opts = Options()
	opts.headless = True  # невидимость
	cap = DesiredCapabilities().FIREFOX
	cap["marionette"] = True  # optional
	assert opts.headless
	browser = webdriver.Firefox(capabilities=cap, executable_path=r"O:\Олег\программирование\python\change_windows_wallpaper\geckodriver.exe", options=opts)
	browser.set_window_size('1920', '1600')
	browser.get(("https://lk.gubkin.ru/schedule/#/activities/faculties?facultyId=" + f_id_and_gr_numb))
	time.sleep(5)
	browser.get_screenshot_as_file(f_id_and_gr_numb + '.png')
	path = os.path.abspath(os.getcwd()) + '\\' + f_id_and_gr_numb + '.png'
	browser.close()
	return path


if __name__ == '__main__':
	f_id_and_gr_numb = '21&groupId=7425'
	path = get_picture(f_id_and_gr_numb)
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
