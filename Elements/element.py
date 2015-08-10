class BasePageElement(object):

    def __set__(self, obj, value):
        print("Set value by", self.locator[0],":",self.locator[1])
        obj.driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        print("Geting value by", self.locator[0],":",self.locator[1])
        return obj.driver.find_element(*self.locator).get_attribute("value")