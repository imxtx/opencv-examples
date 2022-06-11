import cv2
import numpy
import os


def split_video(filename: str) -> list[numpy.ndarray]:
    """Split a video into images

    Args:
        filename (str): filename of video

    Returns:
        list[numpy.ndarray]: list of frames
    """
    vid_cap = cv2.VideoCapture(filename)
    
    if vid_cap.isOpened() == False:
        print(f"Error: cannot open {filename}")
        return None
    
    frames = []
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if ret:
            frames.append(frame)
        else:
            break
    
    return frames


def save_frames(frames: list[numpy.ndarray], path: str, ext: str="jpg") -> None:
    """Save frames as images

    Args:
        frames (list[numpy.ndarray]): list of frames
        path (str): path to save frames
        ext (str): file extension, defaults to jpg
    """
    if frames is None or len(frames) == 0:
        print("Error: No frame to save")
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        print(f"saving {len(frames)} frames to {path} ...")
        for index, frame in enumerate(frames):
            cv2.imwrite(path + f"/{index}.{ext}", frame)
        print("done.")


if __name__ == "__main__":
    frames = split_video("videos/sample-20s.mp4")
    save_frames(frames, "videos/frames")
