from org.hinohara.Generator.Generator import Generator

class MinorScaleGenerator():
    def __init__(self):
        self.input = ""
        self.output = ""
    #キーに合致するマイナースケールの生成

    def set(self,instr):
        self.input = instr

    def get(self):
        gen = Generator()
        gen.set(self.input)
        out = gen.get()
        self.output = out[0]
        notes = out[1]
        key_index_notes = out[2]

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

        notes_sort.sort(key=lambda x: x[0])

        notes_sort_minor = [[0 for i in range(2)] for i in range(7)]
        i = 5
        # 2*7の2次元配列の作成
        while i < len(notes_sort_minor):
            notes_sort_minor[i][0] = i - 5
            notes_sort_minor[i][1] = notes_sort[i][1]
            i += 1
        j = 0
        while j < 5:
            notes_sort_minor[j][0] = j +2
            notes_sort_minor[j][1] = notes_sort[j][1]
            j += 1
        self.output += "\nscale note:\n"
        notes_sort_minor.sort(key=lambda x: x[0])
        for index, item in notes_sort_minor:
            self.output +=item + "\n"
        return self.output
