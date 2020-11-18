# Given an image represented by an N x N matrix, 
# where each pixel is represented by a 32-bit integer, 
# write a method to rotate the image by 90 degrees.


# This solution is simpler but uses extra memory
def rotate_image(image):
    length = len(image)
    copy_image = image.copy()
    
    for r in range(length):
        for c in range(length):
            copy_image[r][c] = image[c][r]
            #copy_image[r][c] = image[c][length - r - 1]

    return copy_image

# This solution should rotate the image in place
# without using any extra memory
def in_place_rotate(image):
    l = len(image) - 1
    y = 0
    while y < l:
        x = y
        ly = l - y
        while x < ly:
            lx = l - x
            p1 = image[y][x]
            image  [y][x]  = image [lx][y]
            image [lx][y]  = image [ly][lx]
            image [ly][lx] = image  [x][ly]
            image  [x][ly] = p1
            x += 1
        y += 1
    return image
    
def print_image(image):
    print("-----Start Image-----")
    for row in image:
        print(row)
    print("------End Image------")

def main():
    image = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

    print_image(image)
    # print_image(rotate_image(image))
    print_image(in_place_rotate(image))

    return 0

if __name__ == '__main__':
    main()