from PIL import Image

# 将文本转换为二进制字符串
def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    
    return binary

# 将二进制字符串转换为文本
def binary_to_text(binary):
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        char = chr(int(byte, 2))
        text += char
    return text

# 将秘密信息嵌入到灰度图像中
def embed_text_in_image(text, image_path, output_path):
    binary_text = text_to_binary(text)
    image = Image.open(image_path).convert('L')
    pixels = image.load()

    width, height = image.size
    index = 0

    for y in range(height):
        for x in range(width):
            # pixel灰度值
            pixel = pixels[x, y]
            
            if index < len(binary_text):
                # 替换最低有效位
                new_pixel = (pixel & 0xFE) | int(binary_text[index])
                pixels[x, y] = new_pixel
                index += 1

    image.save(output_path)
    return len(binary_text)

# 从灰度图像中提取隐藏的秘密信息
def extract_text_from_image(image_path, leng):
    image = Image.open(image_path).convert('L')
    pixels = image.load()

    width, height = image.size
    binary_text = ''
    index = 0
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if(index<leng):
                # 提取最低有效位
                k = str(pixel & 1)
            
                binary_text += k
                index+=1


    extracted_text = binary_to_text(binary_text)
    return extracted_text

# 示例用法
# 这里填嵌入信息
secret_message = "No I will down67 kill879"
# input_image.png是图像信息
image_path = "input.jpg"
output_path = "output_image.png"

# 嵌入秘密信息到灰度图像中
len2 = embed_text_in_image(secret_message, image_path, output_path)

# 从灰度图像中提取隐藏的秘密信息
extracted_message = extract_text_from_image(output_path,len2)

print("隐藏的秘密信息:", extracted_message)
