# Given an image represented by an N x N matrix, 
# where each pixel is represented by a 32-bit integer, 
# write a method to rotate the image by 90 degrees.

def rotate_image(image):
    length = len(image)
    copy_image = image.copy()
    
    for r in range(length):
        for c in range(length):
            copy_image[r][c] = image[c][length-1 - r]


def in_place_rotate(image):
    length = len(image)
    

def main():
    pass

if __name__ == '__main__':
    main()