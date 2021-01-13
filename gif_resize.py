from PIL import Image, ImageSequence
import glob, os, os.path

# 指定パス内のGifファイルを取得
def load_gif_images(input_path):
    image_list = glob.glob(input_path+"/*.gif", recursive=True)
    image_list.sort()
    # print(image_list)
    return image_list

# gifをフレームに分解
def get_frames(path):
    im = Image.open(path)
    return (frame.copy() for frame in ImageSequence.Iterator(im))


input_path = r"G:\共有ドライブ\10 PJフォルダ\LAVA\design_work\walking_animation\10_image_data"
output_path = r"G:\共有ドライブ\10 PJフォルダ\LAVA\design_work\walking_animation\10_image_data\resize"
image_list = load_gif_images(input_path)


for img in image_list:
    frames = get_frames(img)
    file_name = os.path.basename(img)# ファイル名を取得

    # フレームごとに分解してリサイズ
    image_list = []
    for f in frames:
        # print(f)
        f_resize = f.resize((300, 375), Image.LANCZOS)
        # すでにPモードだったため透過処理はOFF
        # alpha = f.split()[3]
        # im = f.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        # mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
        # f.paste(255, mask)
        image_list.append(f_resize)

    # 保存の仕方は、最初の一枚で「.save()」をし、残りのフレームはappend_imagesで渡す
    # 最適化をすると透過がバグるため、optimizeはTrueにはしない
    image_list[0].save(
        output_path + "/" + file_name,
        save_all = True,
        loop = 0,
        duration = 55,
        transparency = 255,
        disposal = 2,# 前フレームを消す処理
        append_images=image_list[1:])