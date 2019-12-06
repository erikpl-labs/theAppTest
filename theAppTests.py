from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TheAppTests():
    def test(self):

        # 1. Launch the web browser and navigate to http://www.slimmtech.com/ta.index.php and login
        browser = webdriver.Chrome()
        print("Chrome web browser has successfully opened.")
        browser.get("https://slimmtech.com/ta/index.php")
        print("Successfully navigated to https://slimmtech.com/ta/index.php")
        assert "the-app - Login" == browser.find_element(By.ID, "pHeading").text
        browser.find_element(By.ID, "edtLogin").send_keys("test")
        browser.find_element(By.ID, "edtPassword").send_keys("test")
        browser.find_element(By.ID, "btnLogin").click()
        print("You are on the Home Page and have successfully logged in.")

        # 2. Enter values in the form fields and click the submit button.
        assert "the-app - Welcomes Test User" == browser.find_element(By.ID, "pHeading").text
        browser.find_element(By.ID, "edtFirstName").send_keys("Erik")
        browser.find_element(By.ID, "edtLastName").send_keys("Burton")
        browser.find_element(By.ID, "edtEmail").send_keys("eb@email.com")
        browser.find_element(By.ID, "taProfound").send_keys("Change your thoughts and you change your world.")
        browser.find_element(By.ID, "chkTesting").click()
        browser.find_element(By.ID, "rblack").click()
        Select(browser.find_element(By.ID, "lstFavCar")).select_by_visible_text('Car')
        browser.find_element(By.ID, "btnSubmit").click()
        print("You have successfully populated the form, submitted the data and are now on the Results Page")

        # 3. Validate Results
        assert "the-app - Results" == browser.find_element(By.ID, "pHeading").text
        assert "Erik" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[1]/td").text
        assert "Burton" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[2]/td").text
        assert "eb@email.com" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[3]/td").text
        assert "Change your thoughts and you change your world." == browser.find_element_by_xpath(
            "//*[@id='tblResults']/tbody/tr[4]/td").text
        assert "Yes" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[5]/td").text
        assert "black" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[6]/td").text
        assert "Car" == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[7]/td").text
        assert "No upload." == browser.find_element_by_xpath("//*[@id='tblResults']/tbody/tr[8]/td").text
        print("Successfully validated the form fields")

        # 4.  Navigate to the Admin Page
        browser.find_element(By.LINK_TEXT, "Admin").click()
        assert "the-app - Admin" == browser.find_element(By.ID, "pHeading").text
        print("You have successfully navigated to the Admin Page")

        # 5. Navigate to the FAQ Page
        browser.find_element(By.LINK_TEXT, "FAQ").click()
        assert "the-app - FAQ" == browser.find_element(By.ID, "pHeading").text
        print("You have successfully navigated to the FAQ Page")

        # 6. Navigate to the JS Popups Page
        browser.find_element(By.LINK_TEXT, "JS Popups").click()
        assert "the-app - JS Popups" == browser.find_element(By.ID, "pHeading").text
        print("You have successfully navigated to the JS Popups Page")

        # 7. Interact with the JS Popup Alert
        browser.find_element(By.ID, "confirm_id").click()
        # Switch to control the Alert window
        obj = browser.switch_to.alert
        # Retrieve the message on the Alert window
        msg = obj.text
        print("You have interacted with a Popup Alert that shows the following message: "+ msg)
        # Use the accept() method to accept the alert
        obj.accept()
        print("You have clicked on the OK Button in the Alert Window.")

        # 8. Click the Logout link to logout
        browser.find_element(By.LINK_TEXT, "Logout").click()
        assert "the-app - Logout" == browser.find_element(By.ID, "pHeading").text
        print("You have successfully Logged out!")

        # 9. Close the browser
        browser.close()
        print("The browser has successfully closed")

logIn = TheAppTests()
logIn.test()