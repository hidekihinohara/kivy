#coding: utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

class CustomSpinner(Spinner):
    pass

#文字化け対策
from kivy.core.text import LabelBase, DEFAULT_FONT #追加
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf") #追加

class KeyValidationApp(Widget):
    key = ObjectProperty(None)

    def on_spinner_change(self, text):
        #resultの初期化
        self.result.text=""
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
        key = text

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
            self.result.text +="sharp note:"
            for i in sharp_notes:
                #print(i, end=" ")
                self.result.text += i + " "
            # notesに合致する音をシャープする
            while k < len(notes):
                for sharp_item in sharp_notes:
                    if notes[k] == sharp_item:
                        notes[k] = sharp_item + "#"
                    else:
                        pass
                k += 1

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
            # print("notes_sort=" + str(notes_sort))
            #print("\nスケール音:")
            self.result.text += "\nscale note:"
            notes_sort.sort(key=lambda x: x[0])
            for index, item in notes_sort:
                #print(item, end=" ")
                self.result.text +=item + " "
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
            self.result.text += "flat note:"
            for i in flat_notes:
                print(i, end=" ")
                self.result.text += i + " "

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
            self.result.text +="\nflat scale note:"
            notes_sort.sort(key=lambda x: x[0])
            for index, item in notes_sort:
                #print(item, end=" ")
                self.result.text += item+" "

class KeyValidation(App):
    def build(self):
        return KeyValidationApp()

if __name__ == '__main__':
    KeyValidation().run()