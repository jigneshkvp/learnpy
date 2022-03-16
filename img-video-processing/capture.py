import cv2

video = cv2.VideoCapture(0)
f_cascade = cv2.CascadeClassifier("./Files/haarcascade_frontalface_default.xml")
a = 1
while True:
    a = a + 1
    check, frame = video.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = f_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    for x, y, w, h in faces:
        gray_img = cv2.rectangle(gray_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Capturing", gray_img)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows
