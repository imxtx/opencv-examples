import cv2


def read_video_from_file(filename: str):
    """Read from a video file.

    Args:
        filename (str): filename
    """
    vid_cap = cv2.VideoCapture(filename)
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
    read_video_from_file("videos/sample-20s.mp4")
