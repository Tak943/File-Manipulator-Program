import sys

commandname = sys.argv[1]

def error_argv():
    if commandname == "replace-string" and len(sys.argv) != 5:
        print("引数を正しく入力してください")
        print("入力の型:")
        print("python3 file_manipulator.py コマンド名 入力ファイルパス 変換前文字列 変換後文字列")
    elif commandname == "reverse" or commandname == "copy" or commandname == "duplicate-contents":
        if len(sys.argv) != 4:
            print("引数を正しく入力してください")
            print("入力の型:")
            if(commandname == "duplicate-contents"):
                print("python3 file_manipulator.py コマンド名 入力ファイルのパス 1以上の整数")
            else:
                print("python3 file_manipulator.py コマンド名 入力ファイルのパス 出力先ファイルのパス")


def reverse():
    error_argv()
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    

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


def copy():
    error_argv()
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    with open(inputpath) as f:
        contents = []
        while True:
            line = f.readline()
            if line == "":
                break
            contents.append(line.rstrip("\n"))
    
    with open(outputpath, "w") as f:
        for line in contents:
            f.write(line + "\n")


def duplicate_contents():
    error_argv()
    inputpath = sys.argv[2]
    n = int(sys.argv[3])

    with open(inputpath) as f:
        contents = []
        while True:
            line = f.readline()
            if line == "":
                break
            contents.append(line.rstrip("\n"))
    
    with open(inputpath, "w") as f:
        for _ in range(n):
            for line in contents:
                f.write(line + "\n")


def replace_string():
    error_argv()
    inputpath = sys.argv[2]
    pre_str = sys.argv[3]
    aft_str = sys.argv[4]

    with open(inputpath) as f:
        contents = []
        while True:
            line = f.readline()
            if line == "":
                break
            contents.append(line.rstrip("\n").replace(pre_str, aft_str))
    
    with open(inputpath, "w") as f:
        for line in contents:
            f.write(line + "\n")



match commandname:
    case "reverse":
        reverse()
    case "copy":
        copy()
    case "duplicate-contents":
        duplicate_contents()
    case "replace-string":
        replace_string()
    case _:
        print("有効なコマンドを入力してください")
