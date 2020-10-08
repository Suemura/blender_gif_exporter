bl_info = {
    "name": "gif_exporter",
    "author": "Masato Suemura",
    "blender": (2, 80, 0),
    "version": (1, 0, 0), # test
    "location": "UV/Image Editor and View Layers",
    "category": "Render",
    "description": "export gif image file",
    "warning": "",
    "support": 'COMMUNITY',
    # "wiki_url": "https:///",
    # "tracker_url": "https://"
}

import bpy
import os, os.path, sys, subprocess
from . import export_gif
from bpy.props import *
from bpy_extras.io_utils import ImportHelper

class GIF_OT_InstallPillow(bpy.types.Operator):
    bl_idname = "gif.install_pillow"
    bl_label = "install pillow"
    bl_options = {"REGISTER", "UNDO"}
    mode = StringProperty()

    def check_installed_package(self, context, python_dir):
        # get installed package
        packages_message = subprocess.check_output(".\python.exe -m pip freeze", shell=True)
        package_message_list = packages_message.decode().split("\n")
        package_list = []
        for p in package_message_list:
            package_name = p.replace("\r", "")
            package_name = package_name.split("==")[0]
            package_list.append(package_name)
        print(package_list)

        if "Pillow" in package_list:
            context.scene["pillow_status"] = "Installed!"
            return True
        else:
            context.scene["pillow_status"] = "Not Installed."
            return False

    def execute(self, context):
        # python.exeのパスを取得
        blender_version = str(bpy.app.version_string)[:4]
        blender_pass = str(sys.executable)
        python_dir = os.path.dirname(blender_pass) +"\\"+blender_version+ "\\python\\bin\\"
        python_pass = python_dir + "python.exe"
        os.chdir(python_dir)
        pip_install_command = ".\python.exe -m pip install pillow"
        pip_uninstall_command = ".\python.exe -m pip uninstall pillow"

        installed = False
        if self.mode == "CHECK":
            installed = self.check_installed_package(context, python_dir)
        elif self.mode == "INSTALL":
            subprocess.call(pip_install_command, shell=True)
        elif self.mode == "UNINSTALL":
            subprocess.call(pip_uninstall_command, shell=True)
        return {"FINISHED"}

class GIF_PT_preferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    bpy.types.Scene.pillow_status = bpy.props.StringProperty(name = "", default="Please Check.")
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.label(text="initial settings : ")
        row = layout.row(align=True)
        row.operator("gif.install_pillow", text="check").mode = "CHECK"
        row.prop(scene, "pillow_status", text="")
        layout.operator("gif.install_pillow", text="install pillow package").mode = "INSTALL"
        layout.label(text="If you want to uninstall the library, please show the console", icon="ERROR")
        layout.operator("gif.install_pillow", text="uninstall pillow package").mode = "UNINSTALL"

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
        col.prop(context.scene, "gif_output_directory", text="path")
        col.prop(context.scene, "gif_output_name", text="name")

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
    GIF_PT_preferences,
    GIF_PT_tools,
    GIF_OT_InstallPillow,
    GIF_OT_open_filebrowser,
    export_gif.GIF_OT_ExportOperator
]

if __name__ == '__main__':
    register()


