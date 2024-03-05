import cv2
import datetime

# test video: 충청남도 천안시_교통정보 CCTV, 세집매 삼거리
cam = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u8")
fourcc = cv2.VideoWriter.fourcc(*'mp4v')

out = None
mode = 'Preview'
flip = False

while cam.isOpened():
    valid, frame = cam.read()
    height, width = frame.shape[:2]
    if valid:
        if flip:
            frame = cv2.flip(frame, 1)

        if mode == 'Record':
            if out is None:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                out = cv2.VideoWriter(f'output/output_{timestamp}.mp4', fourcc, 60, (width, height))
            out.write(frame)
            cv2.circle(frame, (600, 50), 10, (0, 0, 255), -1)

        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1)
        if key == 27:
            if out is not None:
                out.release()
            break
        elif key == ord(' '):
            if mode == 'Record':
                out.release()
                out = None
            mode = 'Preview' if mode == 'Record' else 'Record'
        elif key == ord('f') or key == ord('F'):
            flip = not flip
    else:
        break

cam.release()
cv2.destroyAllWindows()
