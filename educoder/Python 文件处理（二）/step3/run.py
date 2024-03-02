import usr
from PIL import Image
from PIL import ImageChops

def compare_images(path_one, path_two):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    diff = ImageChops.difference(image_one, image_two)

    if diff.getbbox() is None:
       print("生成图片与预期一致")
       return
    else:
       print("生成图片与预期不一致")

if __name__ == "__main__":
    usr.Draw()
    compare_images(r'step3/ex/placeholder.png',r'step3/output/data.png')