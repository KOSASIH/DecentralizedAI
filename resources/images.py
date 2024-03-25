import os

class ImageResources:
    IMAGES_DIR = 'resources/images'

    @staticmethod
    def get_image_path(image_name):
        return os.path.join(ImageResources.IMAGES_DIR, image_name)

    @staticmethod
    def save_image(image_data, image_format, image_name):
        image_path = ImageResources.get_image_path(image_name)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        with open(image_path, 'wb') as file:
            file.write(image_data)

    @staticmethod
    def load_image(image_name, image_format=None):
        image_path = ImageResources.get_image_path(image_name)
        with open(image_path, 'rb') as file:
            image_data = file.read()

        if image_format is not None:
            image_data = ImageResources.convert_image_format(image_data, image_format)

        return image_data

    @staticmethod
    def convert_image_format(image_data, target_format):
        from PIL import Image
        image = Image.open(io.BytesIO(image_data))
        image = image.convert('RGB')
        return BytesIO(image.save(format=target_format))

    @staticmethod
    def is_image_file(filename):
        from PIL import Image
        try:
            Image.open(filename)
            return True
        except Exception as e:
            return False
