import imghdr

class ImageMiddleWare:
    def __init__(self):
        pass

    def validate_image_format(self, image):
        header = image.read(32)
        image.seek(0)
        return imghdr.what(None, header) == "png"

    def validate_length(self, image):
        size = len(image.read())
        image.seek(0)
        return size > 10 * 1024 * 1024

    def validate_image(self, image):
        if not self.validate_image_format(image):
            return {"status": "error", "message": "Imagem não tem o formato ideal"}
        if self.validate_length(image):
            return {"status": "error", "message": "Imagem muito grande"}
        return {"status": "ok", "message": "Imagem válida"}
