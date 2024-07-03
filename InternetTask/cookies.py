from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def set_cookie(driver, name, value):
    print(f"Setting cookie '{name}' to '{value}'...")
    driver.add_cookie({"name": name, "value": value})


def get_cookie(driver, name):
    cookie = driver.get_cookie(name)
    if cookie:
        print(f"The value for cookie '{name}' is now '{cookie['value']}'!")
        return cookie['value']
    else:
        print(f"No cookie found with the name '{name}'!")
        return None


def delete_cookie(driver, name):
    print(f"Deleting cookie '{name}'...")
    driver.delete_cookie(name)


def test():
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")

        cookie_name = "key"
        cookie_value = "value"

        get_cookie(driver, cookie_name)
        print()
        set_cookie(driver, cookie_name, cookie_value)
        print()
        get_cookie(driver, cookie_name)
        print()
        delete_cookie(driver, cookie_name)
        print()
        get_cookie(driver, cookie_name)

    finally:
        driver.quit()


if __name__ == '__main__':
    test()
