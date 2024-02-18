import cv2
import numpy
import imutils


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


def example3() -> None:
    # 1
    image = cv2.imread('images/marker1.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # 2
    cv2.imshow('OriginalDemo', image)
    cv2.imshow('GrayDemo', gray)

    # 3
    edges = cv2.Canny(gray, 10, 250)
    cv2.imshow('EdgesDemo', edges)

    # 4
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('ClosedDemo', closed)

    # 5
    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # 6
    total = 0
    cv2.imwrite('images/copy2.jpg', image)
    final = cv2.imread('images/copy2.jpg')

    # 7
    for c in cnts:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)
        if len(approx) == 4:
            cv2.drawContours(final, [approx], -1, (0, 255,), 4)
            total += 1

    # 8
    print(total)
    cv2.imshow('FinalDemo', final)
    cv2.imwrite('images/final.jpg', final)

    # Fin
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Examples:
    # example1()
    # example2()
    example3()
