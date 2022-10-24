import unittest
class TestPower(unittest.TestCase):
    def test_power_int(self):
        self.assertEqual(find("in9.txt"),22)

        #self.assertEqual(find2("in9.txt"),22)



def find(file):
    fin = open(file,"r")

    word = fin.readline()
    occurence = {}
    for i in word:
        if i not in occurence:
            occurence[i] = 1
        else:
            occurence[i] += 1

    ans = 0
    for i in occurence:
        if occurence[i] == 1:
            ans += 1

    return ans
def find2(file):
    dictionary = {}
    fin = open(file,"r")
    word = fin.readline()
    numberwords = 0
    for i in word:
        if i not in dictionary:
            cnt = 0
            dictionary[i] = 1
            for j in word:
                if j == i:
                    cnt += 1
                if cnt == 2:
                    numberwords += 1
                    break
    return numberwords
            
                    
fin = open("in9.txt","r")
fout = open("out9.txt","w")
word = fin.readline()
occurence = {}
for i in word:
    if i not in occurence:
        occurence[i] = 1
    else:
        occurence[i] += 1

ans = 0
for i in occurence:
    if occurence[i] == 1:
        ans += 1
fout.write(str(ans))
fout.close()

