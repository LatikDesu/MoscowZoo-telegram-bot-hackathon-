from PIL import Image, ImageDraw, ImageFont


def generate_pic(animal_pic, schema):
    if schema == 1:
        image1 = Image.open('app/crs/totem/totem_shema.png')
    else:
        image1 = Image.open('app/crs/totem/day_shema.png')
    image1.thumbnail((350, 350))

    image2 = Image.open(fp=animal_pic)
    image3 = image2.resize((315, 315))

    result_image = Image.new("RGBA", (350, 350))
    result_image.paste(image3, (20, 20))
    result_image.paste(image1, (0, 0), image1)

    return result_image


def generate_text(animal_pic, animal_name):
    result_image = animal_pic
    draw = ImageDraw.Draw(result_image)
    font = ImageFont.truetype("app/crs/fonts/ALS_Story_2.0_B.otf", 20)
    text = animal_name
    draw.text((30, 300), text, font=font)

    return result_image


def create_totem_pic(animal_pic, animal_name):
    result_image = generate_pic(animal_pic, schema=1)
    result_image = generate_text(animal_pic=result_image, animal_name=animal_name)
    
    return result_image


def create_pic_of_day(animal_pic, animal_name):
    result_image = generate_pic(animal_pic, schema=2)
    result_image = generate_text(animal_pic=result_image, animal_name=animal_name)

    return result_image
