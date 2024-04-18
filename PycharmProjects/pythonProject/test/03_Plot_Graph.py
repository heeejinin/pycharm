import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프에서 한글이 제대로 표시되도록 폰트를 설정
# '맑은 고딕' 폰트 경로
font_path = 'C://Windows//Fonts//malgun.ttf'  # 윈도우의 폰트 경로

# 폰트 설정
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=font_prop.get_name())

# CSV 파일을 'cp949' 인코딩으로 읽기
df = pd.read_csv('연도별_고용률_통계표.csv', encoding='cp949')

# '구분' 열을 인덱스로 설정
df.set_index(df.columns[0], inplace=True)

# 15세 이상 고용률의 연도별 데이터 추출
employment_rate_15_above = df.loc['고용률(15세이상)']

# 플롯 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(employment_rate_15_above, marker='o')

# 그래프 제목 및 레이블 설정
plt.title('15세 이상 고용률의 연도별 추이')
plt.xlabel('연도')
plt.ylabel('고용률 (%)')

# 그래프 표시
plt.show()
