import time
class WordCount:
    data = ''
    count = 0

    def fileOpen(self, fname, mode):
        with open(fname, mode) as f:
            self.data = f.read()
    
    def countWord(self):
        lst_data = self.data.split(' ')
        for word in lst_data:
            self.count += 1
    
    def getData(self):
        print(f'-->{self.data}')

    def getCountWords(self):
        print(f'The total word count is :{self.count}')

if __name__ == "__main__":
    # Starting time of ex after input
    st = time.time()

    wc = WordCount()
    wc.fileOpen('data.txt', 'r')
    wc.countWord()
    wc.getCountWords()

    # ending time of ex
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print(f'Execution time: {elapsed_time} seconds')