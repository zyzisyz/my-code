import json
import os


# 打开文件
def OpenFile(path):
    f = open(path, encoding='utf-8')
    json_file = json.load(f)
    return json_file


# 找id
def FindID(path):
    json_file = OpenFile(path)
    AuthorID = []
    ID_Same = False
    for i in json_file:
        for j in AuthorID:
            if i["authorId"] == j:
                ID_Same = True
        if not ID_Same:
            AuthorID.append(i["authorId"])
        ID_Same = False
    return AuthorID


# 找时间
def FindTimeStamp(path):
    AuthorID = FindID(path)
    json_file = OpenFile(path)
    ID_Number = len(AuthorID)
    TimeList = [([] * 1) for i in range(ID_Number)]
    for i in json_file:
        p = 0
        for j in AuthorID:
            if i["authorId"] == j:
                p = int(AuthorID.index(j))
        TimeList[p].append(i["timestamp"])
    return TimeList


# 创建dict
def MakeDict(path):
    AuthorID = FindID(path)
    TimeList = FindTimeStamp(path)
    Dict_Data = dict(list(zip(AuthorID, TimeList)))
    return Dict_Data


# 转json
def Make_json_file(path):
    Dict_Data = MakeDict(path)
    Decode_json = json.dumps(Dict_Data)
    return Decode_json


# json输出
def OutputJson(InPath, OutPath):
    Decode_json = Make_json_file(InPath)
    with open(OutPath, "a") as jf:
        jf.write(Decode_json)
        jf.close()
        print("done！")


# 主函数
def main():
    json_File_Path = os.path.abspath(os.curdir) + "\\test.json"
    Oputput_path = os.path.abspath(os.curdir) + "\\OutPut.json"
    OutputJson(json_Path[i], OutPut_json_file_path[i])


main()

# 转txt
'''
(暂时没用)
with open(txt_path, "a") as tf:
    for i in AuthorID:
        tf.write(str(i))
        tf.write("\n")
        p = AuthorID.index(i)
        for j in TimeList[p]:
            tf.write(" ")
            tf.write(str(j))
            tf.write("\n")
        tf.write("\n")
print("txt done!")
'''

# 测试
'''
for i in AuthorID:
    print(i)
    p = AuthorID.index(i)
    for j in TimeList[p]:
        print(" ", j)

print(Decode_json)
'''
