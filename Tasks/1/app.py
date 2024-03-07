import cv2


img = cv2.imread("olivia.png", cv2.IMREAD_COLOR)

cv2.imshow("image", img)

# define the alpha and beta
alpha = 1.2  # Contrast control
beta = 20  # Brightness control

brightnessParam = cv2.convertScaleAbs(img, beta=beta)
contrastParam = cv2.convertScaleAbs(img, alpha=alpha)

# display the output image
cv2.imshow('brightnessParam', brightnessParam)
cv2.imshow('contrastParam', contrastParam)
cv2.waitKey()
cv2.destroyAllWindows()
