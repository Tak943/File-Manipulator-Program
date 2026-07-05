# File Manipulator Program

CLI (コマンドラインインターフェース) 上で動作する、シンプルなファイル操作ツールです。
コマンドを指定することで、テキストファイルのコピー、行の反転、内容の複製、特定の文字列の置換などを簡単に行うことができます。

## 💻 動作環境 (Prerequisites)

* **Python 3.10 以上**
  (※コード内で `match-case` 文を使用しているため、Python 3.10以降のバージョンが必要です)

## 🚀 使い方 (Usage)

ターミナルまたはコマンドプロンプトを開き、以下の構文でスクリプトを実行します。

```bash
python3 file_manipulator.py <コマンド名> <引数...>
```

## 🛠️ コマンド一覧 (Commands)

本プログラムは以下の4つのコマンドをサポートしています。

### 1. `reverse` (行の反転)
入力ファイルの内容を1行ずつ読み込み、行の順番を逆にして新しいファイルに出力します。

* **構文:**
  `python3 file_manipulator.py reverse <入力ファイルパス> <出力ファイルパス>`
* **実行例:**
  `python3 file_manipulator.py reverse input.txt output.txt`

### 2. `copy` (ファイルのコピー)
入力ファイルの内容をそのまま読み込み、新しいファイルにコピーします。

* **構文:**
  `python3 file_manipulator.py copy <入力ファイルパス> <出力ファイルパス>`
* **実行例:**
  `python3 file_manipulator.py copy input.txt copy.txt`

### 3. `duplicate-contents` (内容の複製)
入力ファイルの内容を読み込み、指定した回数 (`n` 回) だけ複製して、**元の入力ファイルを上書き**します。

* **構文:**
  `python3 file_manipulator.py duplicate-contents <入力ファイルパス> <複製回数(整数)>`
* **実行例:** (内容を3回繰り返す場合)
  `python3 file_manipulator.py duplicate-contents input.txt 3`

### 4. `replace-string` (文字列の置換)
入力ファイルに含まれる特定の文字列 (`変換前文字列`) を、別の文字列 (`変換後文字列`) にすべて置換し、**元の入力ファイルを上書き**します。

* **構文:**
  `python3 file_manipulator.py replace-string <入力ファイルパス> <変換前文字列> <変換後文字列>`
* **実行例:** (`apple` を `orange` に置換する場合)
  `python3 file_manipulator.py replace-string input.txt apple orange`

## ⚠️ エラーハンドリング

引数の数や型が間違っている場合、自動的に正しい入力形式を案内するメッセージがターミナルに表示されます。指示に従ってコマンドを修正してください。