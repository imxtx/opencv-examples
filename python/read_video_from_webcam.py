import cv2


def read_video_from_webcam():
    """Read from webcam.
    """
    # 0 is the device id of your webcam, you can use 1, 2, ... if you
    # have multiple webcams.
    vid_cap = cv2.VideoCapture(0)
    if vid_cap.isOpened() == False:
        print("Error opening the video file")
    else:
        fps = vid_cap.get(cv2.CAP_PROP_FPS)
        print(f"Frames per second: {fps}FPS")
        frame_count = vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(f"Frame count: {frame_count}")
    
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if ret:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(20)
            # quit when stoke "Q" on keyboard
            if key == ord("q"):
                break
        else:
            break
    
    vid_cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    read_video_from_webcam()
