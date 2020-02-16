import requests
from bs4 import BeautifulSoup

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest.settings')

import django
django.setup()

from card.models import Card

#a = {'이름': ['은행', '혜택', '해당번호', '연회비']}
a=[]

def crawl(name):
    num = []  # 숫자 저장
    name1 = " "
    annual = " "
    html = name.text

    soup = BeautifulSoup(name.content, 'html.parser')

    # 크롤 텍스트 가져오기
    for tag in soup.select('div[class = txt]'):
        name1 = name1 + " " + tag.text
    tag1 = soup.select_one('h3[class = tit]')

    for tag2 in soup.select('.s1 li'):
        annual = annual + " " + tag2.text
    title = tag1.text

    if '면제' in annual:
        annual = 0

    if '외식' in name1 or '베이커리' in name1 or '커피' in name1 or '스타벅스' in name1 or '커피빈' in name1 or '요식' in name1 or \
            '점심값' in name1 or '배달앱' in name1 or '할리스' in name1 or '이디야' in name1 or '음식점' in name1:
        num.append(1)

    if '생활' in name1 or '교육' in name1 or '학원' in name1 or '보육료' in name1 or '학비' in name1 or '병원' in name1 or \
            '약국' in name1 or '대중교통' in name1 or '교통비' in name1 or '택시' in name1 or '통행료' in name1 or '렌탈' in name1 or \
            '편의점' in name1 or 'CU' in name1 or 'GS25' in name1 or '카카오 T' in name1:
        num.append(2)

    if '쇼핑' in name1 or '마트' in name1 or '백화점' in name1 or '아울렛' in name1 or '지마켓' in name1 or '옥션' in name1 or \
            '11번가' in name1:
        num.append(3)

    if '주유' in name1 or '칼텍스' in name1 or '리터당' in name1:
        num.append(4)

    if '통신' in name1 or '텔레콤' in name1:
        num.append(5)

    if "해외" in name1 or "항공" in name1 or "면세점" in name1:
        num.append(6)

    if '문화' in name1 or '서점' in name1 or '레저' in name1 or 'CGV' in name1 or \
            '메가박스' in name1 or '롯데시네마' in name1 or '영화' in name1 or '인터파크' in name1:
        num.append(7)

    a.append({'이름': title, '은행': '하나은행', '혜택': name1, '해당번호': num, '연회비': annual})
    return a


if __name__=='__main__':
#######################신용카드
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11491'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11524'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=7353'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=8519'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=8518'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11038'))

     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11036'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=8520'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11034'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11489'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11485'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11484'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11483'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008551P&CD_PD_SEQ=8551&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008553P&CD_PD_SEQ=8553&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009236P&CD_PD_SEQ=9236&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008500P&CD_PD_SEQ=8500&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11495'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI42000000D.web?_frame=no&CD_PD_SEQ=11528'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005536P&CD_PD_SEQ=5536&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41006882P&CD_PD_SEQ=6882&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002085P&CD_PD_SEQ=2085&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005267P&CD_PD_SEQ=5267&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004092P&CD_PD_SEQ=4092&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002652P&CD_PD_SEQ=2652&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41001215P&CD_PD_SEQ=1215&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009051P&CD_PD_SEQ=9051&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004984P&CD_PD_SEQ=4984&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005488P&CD_PD_SEQ=5488&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005269P&CD_PD_SEQ=5269&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004093P&CD_PD_SEQ=4093&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004986P&CD_PD_SEQ=4986&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007512P&CD_PD_SEQ=7512&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41001544P&CD_PD_SEQ=1544&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008900P&CD_PD_SEQ=8900&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005540P&CD_PD_SEQ=5540&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41003154P&CD_PD_SEQ=3154&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009911P&CD_PD_SEQ=9911&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009913P&CD_PD_SEQ=9913&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41011155P&CD_PD_SEQ=11155&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008317P&CD_PD_SEQ=8317&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008318P&CD_PD_SEQ=8318&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008315P&CD_PD_SEQ=8315&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008316P&CD_PD_SEQ=8316&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007144P&CD_PD_SEQ=7144&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009915P&CD_PD_SEQ=9915&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009727P&CD_PD_SEQ=9727&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009892P&CD_PD_SEQ=9892&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008874P&CD_PD_SEQ=8874&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009728P&CD_PD_SEQ=9728&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009893P&CD_PD_SEQ=9893&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008876P&CD_PD_SEQ=8876&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009729P&CD_PD_SEQ=9729&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41000759P&CD_PD_SEQ=759&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005229P&CD_PD_SEQ=5229&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41011746P&CD_PD_SEQ=11746&'))

#############제휴카드
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009705P&CD_PD_SEQ=9705&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008000P&CD_PD_SEQ=8000&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007945P&CD_PD_SEQ=7945&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41000837P&CD_PD_SEQ=837&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41006045P&CD_PD_SEQ=6045&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41010911P&CD_PD_SEQ=10911&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41006784P&CD_PD_SEQ=6784&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005863P&CD_PD_SEQ=5863&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005864P&CD_PD_SEQ=5864&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009003P&CD_PD_SEQ=9003&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005867P&CD_PD_SEQ=5867&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005865P&CD_PD_SEQ=5865&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005866P&CD_PD_SEQ=5866&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005868P&CD_PD_SEQ=5868&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007666P&CD_PD_SEQ=7666&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004164P&CD_PD_SEQ=4164&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005049P&CD_PD_SEQ=5049&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008454P&CD_PD_SEQ=8454&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002567P&CD_PD_SEQ=2567&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004911P&CD_PD_SEQ=4911&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007867P&CD_PD_SEQ=7867&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41006831P&CD_PD_SEQ=6831&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005141P&CD_PD_SEQ=5141&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005219P&CD_PD_SEQ=5219&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005345P&CD_PD_SEQ=5345&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005347P&CD_PD_SEQ=5347&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008469P&CD_PD_SEQ=8469&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009368P&CD_PD_SEQ=9368&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002365P&CD_PD_SEQ=2365&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002366P&CD_PD_SEQ=2366&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005377P&CD_PD_SEQ=5377&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004905P&CD_PD_SEQ=4905&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004907P&CD_PD_SEQ=4907&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004909P&CD_PD_SEQ=4909&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008791P&CD_PD_SEQ=8791&'))
##############멤버쉽 체크카드
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41011305P&CD_PD_SEQ=11305&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009656P&CD_PD_SEQ=9656&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009636P&CD_PD_SEQ=9636&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005463P&CD_PD_SEQ=5463&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005212P&CD_PD_SEQ=5212&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004094P&CD_PD_SEQ=4094&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004882P&CD_PD_SEQ=4882&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41001704P&CD_PD_SEQ=1704&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002014P&CD_PD_SEQ=2014&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004912P&CD_PD_SEQ=4912&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004511P&CD_PD_SEQ=4511&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41008793P&CD_PD_SEQ=8793&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41010329P&CD_PD_SEQ=10329&'))
###############체크카드 캐쉬백
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41010094P&CD_PD_SEQ=10094&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002653P&CD_PD_SEQ=2653&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002745P&CD_PD_SEQ=2745&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41007821P&CD_PD_SEQ=7821&'))
##############체크카드 해외
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41009047P&CD_PD_SEQ=9047&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002338P&CD_PD_SEQ=2338&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41010222P&CD_PD_SEQ=10222&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41004017P&CD_PD_SEQ=4017&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41002437P&CD_PD_SEQ=2437&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005542P&CD_PD_SEQ=5542&'))
     crawl(requests.get('https://www.hanacard.co.kr/OPI41000000D.web?schID=pcd&mID=PI41005590P&CD_PD_SEQ=5590&'))

     for data in a:
        Card(name=data.get('이름'), bank=data.get('은행'), benefit=data.get('혜택'), bn=data.get('해당번호'), af=data.get('연회비')).save()
