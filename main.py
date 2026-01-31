import cv2

def simple_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Не получилось открыть камеру :/")
        return
    print("Камера успешно запущена, нажмите q, чтобы выйти")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Не удалось получить кадр :/")
            break

        cv2.imshow('Сова', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    simple_webcam()