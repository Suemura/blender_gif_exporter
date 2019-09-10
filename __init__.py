bl_info = {
    "name": "gif_exporter",
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
from bpy.props import *
from bpy_extras.io_utils import ImportHelper

class GIF_PT_tools(bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "export"
    bl_category = "Gif Exporter"

    # properties
    bpy.types.Scene.gif_loop_counts = bpy.props.IntProperty(name = "", default = 0, min = 0)
    bpy.types.Scene.gif_use_alpha = bpy.props.BoolProperty(name = "", default = False)
    bpy.types.Scene.gif_invert = bpy.props.BoolProperty(name = "", default = False)
    bpy.types.Scene.gif_duration = bpy.props.IntProperty(name = "", default = 100)
    bpy.types.Scene.gif_output_directory = bpy.props.StringProperty(name = "",)
    bpy.types.Scene.gif_output_name = bpy.props.StringProperty(name = "",)


    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        # col.label(text="loop counts  (0 = infinite)")
        col.prop(context.scene, "gif_use_alpha", text="use_alpha")
        col.prop(context.scene, "gif_invert", text="invert")
        col.prop(context.scene, "gif_loop_counts", text="loop counts")
        col.prop(context.scene, "gif_duration", text="duration(milliseconds)")
        col.operator("gif.open_filebrowser", text="set_output_directory")
        col.operator("gif.export_gif", text="export_gif")
        col.label(text="output_directory")
        col.prop(context.scene, "gif_output_directory", text="output_directory")
        col.prop(context.scene, "gif_output_name", text="output_directory")


class GIF_OT_open_filebrowser(bpy.types.Operator, ImportHelper):
    bl_idname = "gif.open_filebrowser"
    bl_label = "Set output path"
    filter_glob = StringProperty( default="*", options={'HIDDEN'} )

    def execute(self, context):
        filename, extension = os.path.splitext(self.filepath)
        path_pair = os.path.split(self.filepath)
        context.scene["gif_output_directory"] = path_pair[0]
        context.scene["gif_output_name"] = path_pair[1]
        if context.scene["gif_output_name"] == "":
            context.scene["gif_output_name"] = "out.gif"
        return {'FINISHED'}

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
    GIF_PT_tools,
    GIF_OT_open_filebrowser
]

if __name__ == '__main__':
    register()


