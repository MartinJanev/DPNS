import cv2

image = cv2.imread("screencapture-mensa-org-mensa-iq-challenge-2024-11-09-18_41_28.png")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Default", image)
cv2.imshow("grayscale.png", grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()