
# �V���[�v�L�[�̃T�C�N��
Cycle_of_forth = ["F","C","G","D","A","E","B","F#","C#"]

# ��L�[�̃T�C�N��
Cycle_of_fifth = ["F","B��","E��","A��","D��","G��","C��","F��"]

# �L�[�̔���
sharp_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#"]

flat_keys = ["F","B��","E��","A��","D��","G��","C��"]

# ���K
notes = ["C","D","E","F","G","A","B"]

# �L�[���̓_�C�A���O
key = input("�L�[����͂��Ă�������:")

#���K�̃L�[�̃C���f�b�N�X
# �V���[�v,�t���b�g�L�[���������ꍇ�̏�������
if "#" or "��" in key:
    notes[notes.index(key[0:1])] = key
    key_index_notes = notes.index(key)
else:
    key_index_notes = notes.index(key)

if key in sharp_keys:
    # �l�x�T�C�N���̃L�[�̃C���f�b�N�X
    key_index_forth = Cycle_of_forth.index(key)

    #�T�C�N�����特����ύX���郍�W�b�N
    #�V���[�v�L�[�̃T�C�N������ΏۃL�[�̃C���f�b�N�X������
    #�V���[�v��t�^���鉹������

    sharp_notes = []
    k = 0
    while k <= key_index_forth - 2:
        sharp_notes.append(Cycle_of_forth[k])
        k += 1
    k = 0
    print("�V���[�v��:")
    for i in sharp_notes:
        print(i,end=" ")
    #notes�ɍ��v���鉹���V���[�v����
    while k < len(notes):
        for sharp_item in sharp_notes:
            if notes[k] == sharp_item:
                notes[k] = sharp_item + "#"
            else:
                pass
        k += 1

    #�w�肵���L�[�̏��ɕ��בւ�������

    i = key_index_notes
    #2*7��2�����z��̍쐬
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
    print("\n�X�P�[����:")
    notes_sort.sort(key=lambda x: x[0])
    for index,item in notes_sort:
        print(item,end=" ")

if key in flat_keys:
    #�ܓx�T�C�N���̃L�[�C���f�b�N�X
    key_index_fifth=Cycle_of_fifth.index(key)

    #�T�C�N�����特����ύX���郍�W�b�N
    #�t���b�g�L�[�̃T�C�N������ΏۃL�[�̃C���f�b�N�X������
    #�t���b�g��t�^���鉹������

    flat_notes=[]
    k = 1
    while k <= key_index_fifth + 1:
        flat_notes.append(Cycle_of_fifth[k])
        k += 1

    k = 0
    #notes�ɍ��v���鉹���t���b�g����
    while k < len(notes):
        for flat_item in flat_notes:
            if notes[k] == flat_item[0:1]:
                notes[k] = flat_item
            else:
                pass
        k += 1
    print("�t���b�g��:")
    for i in flat_notes:
        print(i,end=" ")

    #�w�肵���L�[�̏��ɕ��בւ�������

    i = key_index_notes
    #2*7��2�����z��̍쐬
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
    print("\n�X�P�[����:")
    notes_sort.sort(key=lambda x: x[0])
    for index,item in notes_sort:
        print(item,end=" ")
