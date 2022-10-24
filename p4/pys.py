import unittest
class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(find("in9.txt"),2)
def find(file):
    fin = open(file,"r")

    s = fin.readline().split()
    length = int(s[0])
    queries = int(s[1])

    array = []
    for i in range(length):
        number = int(fin.readline())
        array.append(number)
    sums = []
    cursum = 0
    for i in array:
        cursum += i
        sums.append(cursum)
    for i in range(queries):
        interval = fin.readline().split()
        number2 = int(interval[1])
        number = int(interval[0])
        answer=0
        if number == 0:
            answer = sums[number2]-0
        else:
            answer = sums[number2]-sums[number-1]
      
def find2(file):
    fin = open(file,"r")

    s = fin.readline().split()
    length = int(s[0])
    queries = 2000

    array = []
    for i in range(length):
        number = int(fin.readline())
        array.append(number)

    for i in range(queries):
        interval = fin.readline().split()
        number2 = int(interval[1])
        number = int(interval[0])
        answer=0
        for i in range(number,number2+1):
            answer += array[i]


unittest.main()
