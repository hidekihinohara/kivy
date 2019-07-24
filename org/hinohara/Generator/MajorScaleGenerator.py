from org.hinohara.Generator.Generator import Generator

class MajorScaleGenerator(Generator):

    #コンストラクタ：インスタンス変数の初期化
    def __init__(self):
        #super().__init__(Generator)
        self.input = ""
        self.output = ""
    #キーに合致するメジャースケールの生成

    def set(self,instr):
        self.input = instr

    def get(self):
            gen = Generator()
            gen.set(self.input)
            out = gen.get()
            self.output=out[0]
            notes=out[1]
            key_index_notes=out[2]
            # 指定したキーの順に並べ替えをする

            i = key_index_notes
            # 2*7の2次元配列の作成
            notes_sort = [[0 for i in range(2)] for i in range(7)]
            while i < len(notes):
                notes_sort[i][0] = i - key_index_notes
                notes_sort[i][1] = notes[i]
                i += 1
            j = 0
            while j < key_index_notes:
                notes_sort[j][0] = j + 7 - key_index_notes
                notes_sort[j][1] = notes[j]
                j += 1
            #print("\nスケール音:")
            self.output +="\nflat scale note:\n"
            notes_sort.sort(key=lambda x: x[0])
            for index, item in notes_sort:
                #print(item, end=" ")
                self.output += item+"\n"
            return self.output

