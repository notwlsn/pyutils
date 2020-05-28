import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)
url = input('URL: ')
file_name = input('file name: ')

dl_jpg(url, 'C:/Users/wcamp/Desktop/xlsx_macro_py/images/', file_name)
