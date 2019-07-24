from org.hinohara.AbstractClass.AbstractGenerator import AbstractGenerator

class Generator(AbstractGenerator):

    #コンストラクタ：インスタンス変数の初期化
    def __init__(self):
        self.input = ""
        self.output = ""
    #キーに合致するメジャースケールの生成

    def set(self,instr):
        self.input = instr

    def get(self):
        #resultの初期化
        self.output = ""
        # シャープキーのサイクル
        Cycle_of_forth = ["F", "C", "G", "D", "A", "E", "B", "F#", "C#"]

        # bキーのサイクル
        Cycle_of_fifth = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]

        # キーの判定
        sharp_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#"]

        flat_keys = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]

        # 音階
        notes = ["C", "D", "E", "F", "G", "A", "B"]

        # キー入力ダイアログ
        key = self.input

        # 音階のキーのインデックス
        # シャープ,フラットキーがあった場合の条件分岐
        if "#" or "b" in key:
            notes[notes.index(key[0:1])] = key
            key_index_notes = notes.index(key)
        else:
            key_index_notes = notes.index(key)
        #シャープキー対応
        if key in sharp_keys:
            # 四度サイクルのキーのインデックス
            key_index_forth = Cycle_of_forth.index(key)

            # サイクルから音程を変更するロジック
            # シャープキーのサイクルから対象キーのインデックスを検索
            # シャープを付与する音を検索

            sharp_notes = []
            k = 0
            while k <= key_index_forth - 2:
                sharp_notes.append(Cycle_of_forth[k])
                k += 1
            k = 0
            #print("シャープ音:")
            self.output +="sharp note:\n"
            for i in sharp_notes:
                #print(i, end=" ")
                self.output += i + "\n"
            # notesに合致する音をシャープする
            while k < len(notes):
                for sharp_item in sharp_notes:
                    if notes[k] == sharp_item:
                        notes[k] = sharp_item + "#"
                    else:
                        pass
                k += 1

        #bキー対応
        if key in flat_keys:
            # 五度サイクルのキーインデックス
            key_index_fifth = Cycle_of_fifth.index(key)

            # サイクルから音程を変更するロジック
            # フラットキーのサイクルから対象キーのインデックスを検索
            # フラットを付与する音を検索

            flat_notes = []
            k = 1
            while k <= key_index_fifth + 1:
                flat_notes.append(Cycle_of_fifth[k])
                k += 1

            k = 0
            # notesに合致する音をフラットする
            while k < len(notes):
                for flat_item in flat_notes:
                    if notes[k] == flat_item[0:1]:
                        notes[k] = flat_item
                    else:
                        pass
                k += 1
            #print("フラット音:")
            self.output += "flat note:\n"
            for i in flat_notes:
                print(i, end=" ")
                self.output += i + "\n"

        return self.output,notes,key_index_notes

