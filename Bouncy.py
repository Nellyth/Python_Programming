class Bouncy:

    def __init__(self):
        self._number = 100
        self.percentage = 0

    def bouncy(self):
        bouncy = 0
        percentage = self.percentage / 100

        while bouncy < self._number * percentage:
            self._number += 1
            if self.data():
                bouncy += 1
        return str(self._number)

    def data(self):
        test = 0
        test1 = 0
        crescent = -10
        decreasing = 10
        number = str(self._number)
        len_data = len(number)
        for i in number:
            value = int(i)
            if value >= crescent:
                crescent = value
                test += 1
            if value <= decreasing:
                decreasing = value
                test1 -= 1
        if not test == len_data and not test1 * -1 == len_data:
            return True

    def main(self, percentage: int):
        if percentage is None:
            return 'The value can not be entered can not be null'
        if not type(percentage) == int:
            return 'only whole values ​​are accepted.'
        if percentage > 100:
            return 'The value can not be greater than 100.'
        if percentage < 1:
            return 'the value can not be less than 1.'
        self.percentage = int(percentage)
        return self.bouncy()


data = Bouncy()
print(data.main(99))
