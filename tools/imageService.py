#coding:utf-8
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

from io import BytesIO

def ocrImage(request):
	file = request.FILES['image']
	print file.size
	if file.size > (1024*1024*3):
		return "请不要搞这么大的图片有点受不了"
	return pytesseract.image_to_string(Image.open(file), lang='chi_sim')