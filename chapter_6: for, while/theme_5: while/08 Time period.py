# Time period

# Ужасное решение: присваивание строчных и численых значений одним и тем же переменным, повторение одной конструкции дважды
h_1 = int(input())
m_1 = int(input())
h_2 = int(input())
m_2 = int(input())

mm_1 = h_1 * 60 + m_1
mm_2 = h_2 * 60 + m_2

diff = mm_2 - mm_1

if h_1 < 10:
    h_1 = '0' + str(h_1)
if m_1 < 10:
    m_1 = '0' + str(m_1)   
print(h_1, m_1, sep=':')

for i in range(1, diff + 1):
    mm_n = mm_1 + i 
    h_n = mm_n // 60
    m_n = mm_n % 60  
    if m_n > 59:       
        m_n = 0
        h_n = h_1 + 1   
    if h_n < 10 or h_n == 0:
        h_n = '0' + str(h_n)
    if m_n < 10:
        m_n = '0' + str(m_n)    
    print(h_n, m_n, sep=':')
