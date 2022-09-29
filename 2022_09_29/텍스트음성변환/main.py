# python main.py로 실행(폴더 경로 문제)
# 재생이 안될 때 => pip install playsound==1.2.2
from gtts import gTTS # 텍스트를 음성으로 변환하기 위한 라이브러리
from playsound import playsound # mp3파일을 파이썬으로 재생하기 위한 라이브러리

# 텍스트를 음성으로 변환
file_path = 'Mydata.txt'
with open(file_path, 'rt', encoding='UTF8') as f: # rt : 읽는 용도로 사용
    read_file = f.read()
tts = gTTS(text=read_file, lang='ko')
mp = "schoolsong.mp3"
tts.save(mp)

# mp3파일을 파이썬으로 재생
playsound(mp)