from org.hinohara.Generator.Generator import Generator

class ChordScaleGenerator():
    def __init__(self):
        self.input = ""
        self.output = ""

    def set(self,instr):
        self.input = instr

    def get(self):
        gen = Generator()
        gen.set(self.input)
        out = gen.get()
        self.output = out[0]
        notes = out[1]
        key_index_notes = out[2]

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
        self.output +="chord scale:\n"
        notes_sort.sort(key=lambda x: x[0])
        notes_sort[0][1] += "major"
        notes_sort[1][1] += "minor"
        notes_sort[2][1] += "minor"
        notes_sort[3][1] += "major"
        notes_sort[4][1] += "major"
        notes_sort[5][1] += "minor"
        notes_sort[6][1] += "minorb5"
        for index, item in notes_sort:
            self.output += item+"\n"
        return self.output
