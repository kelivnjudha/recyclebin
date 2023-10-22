from PIL import Image

def resize_image(img, target_height):
    
    aspect_ratio = img.width / img.height
    new_width = int(target_height * aspect_ratio)

    img_resized = img.resize((new_width, target_height), Image.LANCZOS)
    return img_resized