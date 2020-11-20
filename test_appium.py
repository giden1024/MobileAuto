# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["platformVersion"] = "9.0"
caps["deviceName"] = "xiaomi"
caps["appPackage"] = "com.chinaredstar.shop.uat"
caps["appActivity"] = "com.chinaredstar.shop.ui.login.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("android:id/button1")
el1.click()
el2 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/guid_enter")
el2.click()
el3 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tv_dialog_cancelbtn")
el3.click()
el4 = driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"中式\"]/android.widget.TextView")
el4.click()
el5 = driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"欧式\"]/android.widget.TextView")
el5.click()
el6 = driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"分类分1123241414\"]/android.widget.TextView")
el6.click()
el7 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/banner_image")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[1]")
el8.click()
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[1]")
el9.click()
el11 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/login_phone_et")
el11.click()
el11.send_keys("17610235900")
el12 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/login_btn")
el12.click()
el13 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tip_dtn")
el13.click()
el15 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/ll_code")
el15.click()
el17 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/ll_code")
el17.click()
el19 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/code_view_1")
el19.clear()
el20 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/ll_code")
el20.click()
el21 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el21.send_keys("1")
el22 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el22.clear()
el23 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el23.clear()
el24 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el24.send_keys("5")
el25 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el25.send_keys("1")
el25.send_keys("3")
el25.send_keys("4")
el26 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el26.send_keys("2")
el27 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/vc_back_iv")
el27.click()
el28 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tv_dialog_surebtn")
el28.click()
el29 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/login_btn")
el29.click()
el30 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tip_dtn")
el30.click()
el32 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el32.send_keys("5")
el32.send_keys("59847")
el33 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el33.clear()
el34 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/vc_view")
el34.clear()
el35 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/vc_back_iv")
el35.click()
el36 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tv_dialog_surebtn")
el36.click()
el37 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/login_btn")
el37.click()
el38 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/tip_dtn")
el38.click()
el39 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/et_code")
el39.send_keys("8")
el39.send_keys("0")
el39.send_keys("8")
el39.send_keys("8")
el39.send_keys("2")
el39.send_keys("5")
el40 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]")
el40.click()
el41 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/foundation_bar_tv_back")
el41.click()
el42 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/my_goods_num_ll")
el42.click()
el43 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/collection_list")
el43.click()
el44 = driver.find_element_by_accessibility_id("店铺")
el44.click()
el45 = driver.find_element_by_id("com.chinaredstar.shop.uat:id/foundation_bar_tv_back")
el45.click()
el46 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]")
el46.click()

driver.quit()