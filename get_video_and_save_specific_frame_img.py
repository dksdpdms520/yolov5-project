import cv2
import json
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

 #========================================================================================================================================

def get_video_and_save_specific_frame_img ():

    video_dir = 'C:/Users/user/Desktop/detect_license_plate/data/video' # 디렉토리 경로
    video_list = os.listdir(video_dir) # 디렉토리 안에 어떤 파일이 있는가를 리스트로
    
    json_dir = 'C:/Users/user/Desktop/detect_license_plate/data/json'
    json_list = os.listdir(json_dir)

    for v, j in zip(video_list, json_list):
        createFolder('C:/Users/user/Desktop/detect_license_plate/data/images/%s' % v.replace('.mp4', ''))
        vidcap = cv2.VideoCapture('data/video/' + v)

        with open('data/json/' + j, 'r', encoding='UTF8') as f: 
            json_data = json.load(f)

        success, image = vidcap.read()  # 읽기
        count = 1  # count 초기화
        success = True  # success 초기화

        while success:  # 파일 읽기가 실패하지 않는다면
            success, image = vidcap.read()  # 읽기

            for k in json_data[0]['metas']: # json 데이터에서 시작 끝 프레임 추출
                if k['start_frame'] <= count <= k['end_frame']:
                    cv2.imwrite("C:/Users/user/Desktop/detect_license_plate/data/images/%s/%d.jpg" % (v.replace('.mp4', ''), count), image)
                    print("saved image %d.jpg" % count)

            if cv2.waitKey(10) == 27:
                break
            
            count += 1 #프레임 수 count

#========================================================================================================================================

get_video_and_save_specific_frame_img ()