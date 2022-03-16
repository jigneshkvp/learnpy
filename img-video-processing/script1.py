import cv2

img = cv2.imread("./sample_images/galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


res_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow("Galaxy", res_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
