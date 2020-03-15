import cv2

# cv2.namedWindow("Image")
# cv2.waitKey(0)

image = cv2.imread("1.png")
cv2.imshow("cat", image)
cv2.waitKey(1000)

print(image.shape)
(h, w) = image.shape[:2]
print(h, w)

final_w = 120
r = final_w / float(image.shape[1])
dim = (final_w, int(image.shape[0] * r))
print(dim)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(1000)

cropped = image[10:150, 10:150]
cv2.imshow("cropped", cropped)
cv2.waitKey(1000)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(1000)

rotated2 = cv2.flip(image, 1) # - from -1 to 1
cv2.imshow("rotated2", rotated2)
cv2.waitKey(1000)


color_spaces = ("RGB", "GRAY", "HSV", "LAB", "XYZ", "YUV")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)
cv2.waitKey(1000)

color_image = {color: cv2.cvtColor(image, getattr(cv2, f'COLOR_BGR2{color}'))
               for color in color_spaces}
for clr in color_image:
    cv2.imshow(clr, color_image[clr])
cv2.waitKey(0)



cv2.destroyAllWindows()