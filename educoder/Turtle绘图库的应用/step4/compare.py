from PIL import Image
def getDiff(width, high, image):  # 将要裁剪成w*h的image照片
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')  # 转换为灰度图片 便于处理
    pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255
    for row in range(high): # 逐一与它左边的像素点进行比较
        rowStart = row * width  # 起始位置行号
        for index in range(width - 1):
            leftIndex = rowStart + index
            rightIndex = leftIndex + 1  # 左右位置号
            diff.append(pixels[leftIndex] > pixels[rightIndex])
    return diff  #  *得到差异值序列 这里可以转换为hash码*
def getHamming(diff, diff2):  # 暴力计算两点间汉明距离
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1
    return hamming_distance

if __name__ == '__main__':
    hash1 = Image.open("step4/img/example.jpg")
    hash2 = Image.open("step4/sj.jpg")
    diff1 = getDiff(32, 32, hash1)
    diff2 = getDiff(32, 32, hash2)
    ans = getHamming(diff1, diff2)
    if ans <= 7:
        print("生成图片与预期一致")
    else:
        print("你的答案与正确答案不一致")
