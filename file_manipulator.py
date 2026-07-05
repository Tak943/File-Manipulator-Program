import sys
if(len(sys.argv) != 4):
    print("引数を正しく入力してください")
    print("入力の型:")
    print("python3 ファイル名 コマンド名 入力ファイルのパス 出力先ファイルのパス")
commandname = sys.argv[1]
inputpath = sys.argv[2]
outputpath = sys.argv[3]

def reverse():
    with open(inputpath) as f:
        contents = []
        while True:
            line = f.readline()
            if line == "":
                break
            contents.append(line.rstrip("\n"))
    
    with open(outputpath, "w") as f:
        for line in contents[::-1]:
            f.write(line + "\n")

if commandname == "reverse":
    reverse()
