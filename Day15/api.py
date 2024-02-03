#API(어느 회사에서 제공하는 서비스 프로그램)
from googleapiclient.discovery import build

key = "AIzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g"
#유튜브 api 클라이언트 생성
youtube = build('youtube','v3',developerKey=key)


result = youtube.commentThreads().list(
    part = 'snippet',#댓글들이라고 스니핏이라고 한다.
    videoId = '03TbrIhuAdM',
    maxResults = 100,
).execute()

for i in result['items']:
    comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
    print(comment)

