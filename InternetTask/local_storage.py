from selenium import webdriver


def set_value(driver, key, value):
    print(f"Setting '{key}' to '{value}'...")
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")


def get_value(driver, key):
    value = driver.execute_script(f"return window.localStorage.getItem('{key}');")
    print(f"The value for '{key}' is now '{value}'!")
    return value


def remove_value(driver, key):
    print(f"Removing '{key}'...")
    driver.execute_script(f"window.localStorage.removeItem('{key}')")


def test():
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")

        key = "key"
        value = "value"

        get_value(driver, key)
        print()
        set_value(driver, key, value)
        print()
        get_value(driver, key)
        print()
        remove_value(driver, key)
        print()
        get_value(driver, key)

    finally:
        driver.quit()


if __name__ == '__main__':
    test()

