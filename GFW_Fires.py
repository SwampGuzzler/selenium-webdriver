import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
def find_and_act(selector,actionname,driver,actions):
    elem = driver.find_element_by_css_selector(selector)
    getattr(actions,actionname)(elem)
    return elem
class GFWFiresTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    def test_title(self):
        self.driver.get('http://fires.globalforestwatch.org/#v=map&x=115&y=0&l=5&lyrs=Active_Fires')
        self.assertEqual(
            self.driver.title,
            'Global Forest Watch Fires')
        self.assertEqual(
            self.driver.current_url,
            'http://fires.globalforestwatch.org/#v=map&x=-122.33&y=47.61&l=11&lyrs=Active_Fires&dirty=true')
    def test_clickies(self):
        self.driver.get('http://fires.globalforestwatch.org/#v=map&x=115&y=0&l=5&lyrs=Active_Fires')

        falerts_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "report-link"))
        )
        # falerts_button = wait.until(EC.element_to_be_clickable((By.ID,'report-link')))

        # falerts_button = self.driver.find_element_by_css_selector('#report-link')
        actions = ActionChains(self.driver)
        actions.click(falerts_button)
        find_and_act("#legend-widget-title",'click',self.driver,actions)
 
        find_and_act('#report-options-close','click',self.driver,actions)
        # run_analysis_button = self.driver.find_element_by_css_selector('#report-launch')
        # actions.click(run_analysis_button)
        forest_use_button = self.driver.find_element_by_css_selector('#forest-use-panel_button_title')
        actions.click(forest_use_button)
 
        find_and_act("#oil-palm-checkbox",'click',self.driver,actions)
 
        accordians = self.driver.find_elements_by_css_selector('.dijitAccordionTitle')
 
        for i in range(0,2):
            find_and_act('.esriSimpleSliderIncrementButton','click',self.driver,actions)

        # find_and_act("#esri-geocoder-widget",'click',self.driver,actions)
        geocoder = self.driver.find_element_by_css_selector('#esri-geocoder-widget_input')
        find_and_act('#esri-geocoder-widget_input','click',self.driver,actions)
        geocoder.send_keys('Seattle, WA')
        
        self.driver.implicitly_wait(1)
        geocoder.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(3)
        # self.assertEqual(
        #     self.driver.current_url,
        #     'http://fires.globalforestwatch.org/#v=map&x=-122.33&y=47.61&l=11&lyrs=Active_Fires&dirty=true')

        # driver.current_url
        # self.assertTrue(geocoder.is_selected())

        actions.perform()
        print("done")
    @classmethod
    def tearDownClass(cls):
        # cls.driver.implicitly_wait(20)
 
        # cls.driver.quit()
        return
 
unittest.main()