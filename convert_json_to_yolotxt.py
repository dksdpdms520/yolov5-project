import cv2
import json
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def get_video_and_save_specific_frame_img():
    video_dir = 'C:/Users/user/Desktop/detect_license_plate/data/video'
    video_list = os.listdir(video_dir) # 비디오 파일 디렉토리
    print(video_list)
    json_dir = 'C:/Users/user/Desktop/detect_license_plate/data/json'  # json 파일 디렉토리
    json_list = os.listdir(json_dir)
    normalize_bbox_list = []
    print(json_list)

    for v, j in zip(video_list, json_list):  # video 와 json 추출
        print(v,"와 ",j,"를 수행합니다.")
        vidcap = cv2.VideoCapture('data/video/' + v)  # 해당 비디오 VideoCapture 객체생성
        with open('data/json/' + j, 'r', encoding='UTF8') as f:  # json 파일 하나 읽고 json_data 생성
            json_data = json.load(f)
        createFolder('C:/Users/user/Desktop/detect_license_plate/convertdone/%s' % v.replace('.mp4', ''))
        success, image = vidcap.read()  # 읽기
        count = 1  # count 초기화
        bbox_index = 0

        success = True  # success 초기화

        while success:  # 파일 읽기가 실패하지 않는다면
            success, image = vidcap.read()  # 읽기
            
            for k in json_data[0]['metas']: # json 데이터에서 시작 끝 프레임 추출
                
                if k['start_frame'] <= count <= k['end_frame']:

                    cv2.imwrite("C:/Users/user/Desktop/detect_license_plate/convertdone/%s/%d.jpg" % (v.replace('.mp4', ''), count), image) # 이미지 파일 생성
                    print("saved image %d.jpg" % count)
                    print('bbox_index ', bbox_index)
                    if bbox_index > len(k['bbox_list']) - 1:
                        bbox_index = 0
                    
                    imgheight, imgwidth = (1080, 1920)
                    x, y, w, h = k['bbox_list'][bbox_index]
                    print( x, y, w, h)
                    x = x + (w/2.0)
                    y = y + (h/2.0)



                    yolo_x = x/imgwidth
                    yolo_w = w/imgwidth
                    yolo_y = y/imgheight
                    yolo_h = h/imgheight
                    print(yolo_x,yolo_y,yolo_w,yolo_h)

                    with open(f'C:/Users/user/Desktop/detect_license_plate/convertdone/%s/{count}.txt' % v.replace('.mp4', ''), 'a') as f:
                        f.write(f"0 {yolo_x} {yolo_y} {yolo_w} {yolo_h}\n")
                    bbox_index = bbox_index + 1

            if cv2.waitKey(10) == 27: # esc
                break
            count += 1 # 프레임 수 count

            
get_video_and_save_specific_frame_img()