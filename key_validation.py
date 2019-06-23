
# シャープキーのサイクル
Cycle_of_forth = ["F","C","G","D","A","E","B","F#","C#"]

# ♭キーのサイクル
Cycle_of_fifth = ["F","B♭","E♭","A♭","D♭","G♭","C♭","F♭"]

# キーの判定
sharp_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#"]

flat_keys = ["F","B♭","E♭","A♭","D♭","G♭","C♭"]

# 音階
notes = ["C","D","E","F","G","A","B"]

# キー入力ダイアログ
key = input("キーを入力してください:")

#音階のキーのインデックス
# シャープ,フラットキーがあった場合の条件分岐
if "#" or "♭" in key:
    notes[notes.index(key[0:1])] = key
    key_index_notes = notes.index(key)
else:
    key_index_notes = notes.index(key)

if key in sharp_keys:
    # 四度サイクルのキーのインデックス
    key_index_forth = Cycle_of_forth.index(key)

    #サイクルから音程を変更するロジック
    #シャープキーのサイクルから対象キーのインデックスを検索
    #シャープを付与する音を検索

    sharp_notes = []
    k = 0
    while k <= key_index_forth - 2:
        sharp_notes.append(Cycle_of_forth[k])
        k += 1
    k = 0
    print("シャープ音:")
    for i in sharp_notes:
        print(i,end=" ")
    #notesに合致する音をシャープする
    while k < len(notes):
        for sharp_item in sharp_notes:
            if notes[k] == sharp_item:
                notes[k] = sharp_item + "#"
            else:
                pass
        k += 1

    #指定したキーの順に並べ替えをする

    i = key_index_notes
    #2*7の2次元配列の作成
    notes_sort = [[0 for i in range(2)] for i in range(7)]
    while i < len(notes):
        notes_sort[i][0] = i-key_index_notes
        notes_sort[i][1] = notes[i]
        i += 1
    j = 0
    while j < key_index_notes:
        notes_sort[j][0]=j+7-key_index_notes
        notes_sort[j][1] = notes[j]
        j += 1
    #print("notes_sort=" + str(notes_sort))
    print("\nスケール音:")
    notes_sort.sort(key=lambda x: x[0])
    for index,item in notes_sort:
        print(item,end=" ")

if key in flat_keys:
    #五度サイクルのキーインデックス
    key_index_fifth=Cycle_of_fifth.index(key)

    #サイクルから音程を変更するロジック
    #フラットキーのサイクルから対象キーのインデックスを検索
    #フラットを付与する音を検索

    flat_notes=[]
    k = 1
    while k <= key_index_fifth + 1:
        flat_notes.append(Cycle_of_fifth[k])
        k += 1

    k = 0
    #notesに合致する音をフラットする
    while k < len(notes):
        for flat_item in flat_notes:
            if notes[k] == flat_item[0:1]:
                notes[k] = flat_item
            else:
                pass
        k += 1
    print("フラット音:")
    for i in flat_notes:
        print(i,end=" ")

    #指定したキーの順に並べ替えをする

    i = key_index_notes
    #2*7の2次元配列の作成
    notes_sort = [[0 for i in range(2)] for i in range(7)]
    while i < len(notes):
        notes_sort[i][0] = i-key_index_notes
        notes_sort[i][1] = notes[i]
        i += 1
    j = 0
    while j < key_index_notes:
        notes_sort[j][0]=j+7-key_index_notes
        notes_sort[j][1] = notes[j]
        j += 1
    print("\nスケール音:")
    notes_sort.sort(key=lambda x: x[0])
    for index,item in notes_sort:
        print(item,end=" ")
