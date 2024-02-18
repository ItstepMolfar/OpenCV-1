import cv2


def example1() -> None:
    # 1
    marker_path = 'images/marker1.png'
    marker = cv2.imread(marker_path)
    cv2.imshow('MarkerDemo', marker)

    # 2
    cv2.imwrite('images/copy1.jpg', marker)
    cv2.waitKey()
    cv2.destroyAllWindows()


def example2() -> None:
    # 1
    print('Try open Your WebCam ...')
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 2
    if not cap.isOpened():
        print('Cannot open WebCam!')
    else:
        # 3
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
        # 4
        while True:
            success, frame = cap.read()
            if success:
                cv2.imshow('Capture Image', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
        # 5
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # Examples:
    # example1()
    example2()
