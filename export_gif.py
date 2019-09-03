import bpy, glob
from PIL import Image, ImageDraw

def append_button_header(self, context):
    layout = self.layout
    layout.separator()
    print("add button")
    if bpy.context.space_data.image is not None:
        layout.operator(
            "run.export_gif",
            text="export_GIF",
            icon='FILE_FOLDER'
            )

class GIF_OT_ExportOperator(bpy.types.Operator):
    bl_idname = "run.export_gif"
    bl_label = "auto add materials"
    bl_options = {"REGISTER", "UNDO"}

    def load_image_file(self, context):
        print("test : load_image_file")
        output_path = context.scene.render.filepath
        image_path_list = glob.glob(output_path+"/*.png", recursive=True)
        image_list = []
        first_img = None
        for i, img_path in enumerate(image_path_list):
            if i==0:
                first_img = Image.open(img_path)
                alpha = first_img.split()[3]
                first_img = first_img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
                mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
                first_img.paste(255, mask)

            else:
                print(img_path)
                im = Image.open(img_path)
                alpha = im.split()[3]
                im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
                mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
                im.paste(255, mask)
                image_list.append(im)
        return first_img, image_list


    def execute(self, context):
        print("test : execute")
        output_path = context.scene.render.filepath
        first_img, image_list = self.load_image_file(context)

        first_img.save(output_path+'/out.gif', save_all=True, transparency=255, append_images=image_list)
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