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

# 2023년 나이별 고용비율을 선택
age_groups = ['15~19세', '20~29세', '30~39세', '40~49세', '50~59세', '60세이상']
employment_rates_2023 = df.loc[age_groups, '2023']

# 파이 그래프 생성
plt.figure(figsize=(8, 8))
plt.pie(employment_rates_2023, labels=age_groups, autopct='%.1f%%', startangle=140)

# 그래프 제목 설정
plt.title('2023년 나이별 고용비율')

# 그래프 표시
plt.show()
