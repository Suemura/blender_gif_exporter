bl_info = {
    "name": "gix_exporter",
    "author": "Suemura",
    "blender": (2, 80, 0),
    "version": (0, 0, 0), # test
    "location": "UV/Image Editor and View Layers",
    "category": "Render",
    "description": "export gif image file",
    "warning": "",
    "support": 'TESTING',
    # "wiki_url": "https:///",
    # "tracker_url": "https://"
}

import bpy
import os, os.path
from . import export_gif


class test_Panell(bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "export"
    bl_category = "Gif Exporter"
    bl_options = {'DEFAULT_CLOSED'}
    def draw(self, _):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="出力フォルダの指定")
        col.operator("run.export_gif", text="export_gif")



# クラスの登録
def register():
    for cls in classes:
        print("Register : " + str(cls))
        bpy.utils.register_class(cls)

# クラスの登録解除
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

# 登録するクラス
classes = [
    export_gif.GIF_OT_ExportOperator,
    test_Panell
]

if __name__ == '__main__':
    register()


