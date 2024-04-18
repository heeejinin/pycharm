import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프에서 한글이 제대로 표시되도록 폰트를 설정
# '맑은 고딕' 폰트 경로
font_path = 'C://Windows//Fonts//malgun.ttf'  # 윈도우의 폰트 경로

# 폰트 설정
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rc('font', family=font_prop.get_name())


# CSV 파일 이름
f = open('연도별_고용률_통계표.csv', 'r', encoding='cp949')

# 인코딩을 'utf-8'로 지정하여 CSV 파일을 읽기
# 'cp949' 인코딩
df = pd.read_csv(f, encoding='cp949')

# '구분' 열을 인덱스로 설정
df.set_index(df.columns[0], inplace=True)

# 2022년과 2023년 고용비율을 선택
years = ['2022', '2023']
employment_rates = df.loc[:, years]

# 바 그래프
ax = employment_rates.plot(kind='bar', figsize=(10, 6))
ax.set_ylabel('고용률 (%)')
ax.set_title('2022년과 2023년 고용률')
ax.set_ylim(0, 100)

# 각 바 위에 수치를 표시
for p in ax.patches:
    # 바의 높이(고용률) 가져옴
    value = p.get_height()
    # 바의 중간에 수치를 표시
    ax.annotate(f'{value:.1f}%', (p.get_x() + p.get_width() / 2, value), ha='center', va='bottom')

# 그래프 표시
plt.show()
