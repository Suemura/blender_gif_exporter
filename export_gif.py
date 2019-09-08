import bpy, glob
from PIL import Image, ImageDraw

class GIF_OT_ExportOperator(bpy.types.Operator):
    bl_idname = "gif.export_gif"
    bl_label = "auto add materials"
    bl_options = {"REGISTER", "UNDO"}

    def load_image_file(self, context):
        print("test : load_image_file")
        output_path = context.scene.render.filepath
        image_path_list = glob.glob(output_path+"/*.png", recursive=True)
        image_path_list.sort()
        image_list = []

        # "use_alpha"
        if context.scene["gif_use_alpha"] == True:
            for img_path in image_path_list:
                print(img_path)
                im = Image.open(img_path)
                alpha = im.split()[3]
                im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
                mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
                im.paste(255, mask)
                image_list.append(im)
        else:
            for img_path in image_path_list:
                print(img_path)
                im = Image.open(img_path)
                image_list.append(im)

        # "invert"
        if context.scene["gif_invert"] == True: image_list.reverse()

        return image_list[0], image_list[1:]


    def execute(self, context):
        print("test : execute")
        output_path = context.scene.render.filepath
        first_img, image_list = self.load_image_file(context)

        # save
        if context.scene["gif_use_alpha"] == True:
            first_img.save(
                context.scene["gif_output_directory"] + "/out.gif",
                save_all = True,
                loop = abs(context.scene["gif_loop_counts"]),
                duration = abs(context.scene["gif_duration"]),
                transparency = 255,
                disposal = 2,
                append_images=image_list)
        else:
            first_img.save(
                context.scene["gif_output_directory"] + "/out.gif",
                save_all = True,
                loop = abs(context.scene["gif_loop_counts"]),
                duration = abs(context.scene["gif_duration"]),
                disposal = 1,
                append_images=image_list)
        return {"FINISHED"}


# クラスの登録
def register():
    for cls in classes:
        bpy.types.IMAGE_HT_header.append(append_button_header)

# クラスの登録解除
def unregister():
    for cls in classes:
        bpy.types.IMAGE_HT_header.remove(append_button_header)

if __name__ == '__main__':
    register()
