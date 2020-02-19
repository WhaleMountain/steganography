# steganography 

## 目的 
steganographyを作ってみたい。遊びです。

## できること
- 画像に文字を隠す。 
- 画像に画像を隠す。 

## エンコード
### 画像に文字を隠す
1. 画像のパスの記述
~~~python
if __name__ == "__main__":
    imgpath = "入力画像"
    outpath = "出力画像"
~~~
2. msg変数に隠したい文字を入れる。
~~~python
def stegano_encode(imgpath, outpath):
    img = read_img(imgpath)
    msg = "Hello, World!!"
    msg = [msg[i:i+1] for i in range(0, len(msg), 1)]
~~~

### 画像に画像を隠す
1. 画像のパスの記述
~~~python
if __name__ == "__main__":
    imgpath = "入力画像"
    outpath = "出力画像"

    print("Image encode")
    key = stegano_encode(imgpath, outpath)
    # keyファイルの出力
    with open("出力パス", "wb") as f:
        pickle.dump(key, f)
~~~
2. 隠したい画像の読み込み
~~~python
def stegano_encode(imgpath, outpath):
    img = read_img(imgpath)
    with open("隠したい画像", "rb") as f:
        msg = base64.b64encode(f.read())
    msg = [msg[i:i+1] for i in range(0, len(msg), 1)]
~~~

## デコード
1. keyファイルの読み込み
~~~python
if __name__ == "__main__":
    imgpath = "エンコードした画像のパス"

    key = []
    with open("keyファイルのパス", "rb") as f:
        key = pickle.load(f)

    print("Image decode")
    stegano_decode(outpath, key)
~~~
2. 関数の書き換え。状況に応じて
~~~python
def stegano_decode(imgpath, key):
    # 画像を取り出す時
    with open("出力パス", "wb") as f:
        f.write(base64.b64decode(msg))
    # 文字を取り出す時
    # print(msg)
~~~