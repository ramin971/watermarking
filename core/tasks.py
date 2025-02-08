from celery import shared_task
from PIL import Image, ImageDraw, ImageFont
import os 
from django.conf import settings
from .models import Product


@shared_task
def add_watermark(image_path, product_id, watermark_text='Diba.ir'):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Load a font
        font_path = os.path.join(settings.BASE_DIR, 'fonts/Reglarik.ttf')
        font = ImageFont.truetype(font_path, 36)

        # Calculate the size of the text using textbbox
        text_bbox = draw.textbbox((0,0),watermark_text,font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Position the text at the bottom tight corner
        x = image.width - text_width - 10
        y = image.height - text_height - 10

        # Add text watermark
        draw.text((x,y), watermark_text, font=font, fill=(100,100,255,128))

        # Save the watermarked image
        # print('###################')
        # print('text-w = ', text_width)
        # print('text-h = ', text_height)
        # print('x = ',x,'*****' , 'y = ',y)
        # print('media-root = ',settings.MEDIA_ROOT)
        # print('image_path = ', image_path)
        watermarked_image_path = os.path.join(settings.MEDIA_ROOT, 'images/watermarked', os.path.basename(image_path))
        # print('watermarked-image-path = ',watermarked_image_path)
        image.save(watermarked_image_path)

        # Update the product instance with the watermarked image path
        product = Product.objects.get(id=product_id)
        # product.watermarked_image = watermarked_image_path
        product.watermarked_image = os.path.join('images/watermarked',os.path.basename(image_path))
        # Delete original image
        product.image.delete()
        product.save()
    except Exception as e:
        print(f'Error adding watermark: {e}')