import time

class TestLandingPage:
    def test_landing_on_correct_url(self, setup):
        current_url = setup.current_url
        expected_url = "https://ui.cogmento.com/"
        if current_url == expected_url:
            print("Landed on the correct URL")
            setup.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//url_success.png")
            assert True
        else:
            print(f"Error: Landed on {current_url} instead of {expected_url}")
            setup.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//url_fail.png")
            assert False,f"Test failed: Landed on {current_url} instead of {expected_url}"

    def test_landing_on_incorrect_url(self, setup_incorrect_url):
            setup1 = setup_incorrect_url
            current_url = setup1.current_url
            expected_url = "https://ui.cogmento.com/"
            time.sleep(10)
            if current_url != expected_url:
                print(f"Correctly did not land on {expected_url}. Current URL: {current_url}")
                setup1.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//url_negative_fail.png")
                assert True
            else:
                print(f"Unexpected: Landed on {current_url}, but expected to not land on {expected_url}")
                setup1.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots//url_negative_success.png")
                assert False, f"Test failed: Landed on {current_url} when it should not have."
