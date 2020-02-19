from PIL  import Image
import random
import base64
import pickle

def read_img(imgpath):
    img = Image.open(imgpath)
    return img.convert('RGB')

def write_img(img, outpath):
    img.save(outpath)

def char_enc(r, g, b, m):
    bm = (r+g)//4 + ord(m)
    return r, g, bm

def char_dec(r, g, b):
    bm = b - (r+g)//4
    return chr(bm)

def stegano_encode(imgpath, outpath):
    img = read_img(imgpath)
    with open("images/sarah.jpg", "rb") as f:
        msg = base64.b64encode(f.read())
    msg = [msg[i:i+1] for i in range(0, len(msg), 1)]
    #msg = "hello, world!!"
    key = []

    while msg != []:
        # 座標の決定
        x = random.randint(0, img.size[0]-1)
        y = random.randint(0, img.size[1]-1)
        if [x, y] in key: continue
        key.append([x, y])

        # 情報の挿入
        r, g, b = img.getpixel((x, y))
        if r == 255 and g == 255 and b == 255: continue # 白色は対象にしない。わかりやすいから。
        r, g, b = char_enc(r, g, b, msg.pop(0))
        img.putpixel((x, y), (r, g, b))

    write_img(img, outpath)
    return key

def stegano_decode(imgpath, key):
    img = read_img(imgpath)
    msg = ""
    for k in key:
        r,g,b = img.getpixel((k[0], k[1]))
        msg += char_dec(r, g, b)

    with open("images/majika.jpg", "wb") as f:
        f.write(base64.b64decode(msg))
    #print(msg)
    

if __name__ == "__main__":
    imgpath = "images/sarah2.jpg"
    outpath = "images/stegano.png"

    # エンコード時
    #print("Image encode")
    #key = stegano_encode(imgpath, outpath)
    #with open("images/stegano_key.txt", "wb") as f:
    #    pickle.dump(key, f)

    # デコード時
    key = []
    with open("images/stegano_key.txt", "rb") as f:
        key = pickle.load(f)

    print("Image decode")
    stegano_decode(outpath, key)