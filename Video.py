import cv2

cap = cv2.VideoCapture(0)   # -1- free camera
_, frame = cap.read()
width = 900
height = int(frame.shape[0] * (width / float(frame.shape[1])))
size = (width, height)

cv2.imwrite("img/img.jpg", frame)

fourcc = cv2.VideoWriter_fourcc(*"MPEG")
fps = 20.0
out = cv2.VideoWriter("video.avi", fourcc, fps, (640, 480))


while cap.isOpened():   # while True or 1
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("no image read")
        break

while True:
    ret, frame = cap.read()
    if not ret:
        print('no image read')
        break
    frame = cv2.resize(frame, size)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame2", gray)
    if cv2.waitKey(1) == ord("q"):
        break
# cleaning
cap.release()
out.release()
cv2.destroyAllWindows()
