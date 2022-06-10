import cv2


def write_video_from_webcam():
    """Write a video file from webcam
    """
    vid_cap = cv2.VideoCapture(0)

    # set frame size and fps
    frame_width = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (frame_width, frame_height)
    fps = 20

    # FFMPEG backend with MP4 container natively uses other values as fourcc 
    # code: see [ObjectType](http://mp4ra.org/#/codecs), so you may receive 
    # a warning message from OpenCV about fourcc code conversion.
    output = cv2.VideoWriter("videos/output_video_from_webcam.mp4", 
        cv2.VideoWriter_fourcc(*"mp4v"), fps, frame_size)

    if vid_cap.isOpened() == False:
        print("Error: cannot open the webcam")
        return
    
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if ret:
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(20)
            output.write(frame)
            if key == ord("q"):
                break
        else:
            print("Stream disconnected")
            break
    
    vid_cap.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    write_video_from_webcam()
