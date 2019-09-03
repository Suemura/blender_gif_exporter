from PIL import Image

im1 = Image.open("C:\\Users\\yuiga\\AppData\\Roaming\\Blender Foundation\\Blender\\2.80\\scripts\\addons\\blender_gif_exporter\\input0001.png")
im2 = Image.open("C:\\Users\\yuiga\\AppData\\Roaming\\Blender Foundation\\Blender\\2.80\\scripts\\addons\\blender_gif_exporter\\input0018.png")
im3 = Image.open("C:\\Users\\yuiga\\AppData\\Roaming\\Blender Foundation\\Blender\\2.80\\scripts\\addons\\blender_gif_exporter\\input0029.png")
alpha1 = im1.split()[3]
alpha2 = im2.split()[3]
alpha3 = im3.split()[3]

im1 = im1.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
im2 = im2.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
im3 = im3.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

mask1 = Image.eval(alpha1, lambda a: 255 if a <=128 else 0)
mask2 = Image.eval(alpha2, lambda a: 255 if a <=128 else 0)
mask3 = Image.eval(alpha3, lambda a: 255 if a <=128 else 0)

im1.paste(255, mask=mask1)
im2.paste(255, mask=mask2)
im3.paste(255, mask=mask3)

# image_list = [im1, im1]
image_list = [im2, im1, im3, im1]

# im1.save('export.gif', save_all=True, duration=1000, loop=0, transparency=255, disposal=2, append_images=image_list)
# im1.save('export.pdf', save_all=True, duration=1000, loop=0, transparency=255, disposal=2, append_images=image_list)
for mode in [1,2]:
    im1.save(
        f"disposal_test{mode}.gif",
        save_all=True,
        loop=0,
        transparency=255,
        disposal=mode,
        append_images=image_list)
# im1.save('export.gif', save_all=True, transparency=255)