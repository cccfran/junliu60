from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import random

# Try to find a Helvetica font on the system
helvetica_path = None
for font in font_manager.findSystemFonts(fontpaths=None, fontext='ttf'):
    if "Helvetica" in font:
        helvetica_path = font
        break

# If Helvetica is not found, use fallback font
font_path_to_use = helvetica_path if helvetica_path else None


# Recreate data: names and categories
names = [
    "Chiara Sabatti", "Scott C. Schmidler", "Yuguo Chen", "Xiaole S. Liu", "Tanya Logvinenko",
    "Mayetri Gupta", "Shane Jensen", "Hosung Kang", "Gopi Goswami", "Peng Zhang", "WE Johnson",
    "Jiajun Gu", "Xiaodan Fan", "Tingting Zhang", "Wei Zhang", "Yuan Yuan", "Jing Zhang",
    "Paul Edlefsen", "Roee Gutman", "Bo Jiang", "Lei Guo", "Simeng Han", "Daniel Fernandez",
    "Matey Neykov", "Yang Li", "Victoria Krakovna", "Xufei Wang", "Jiexing Wu", "Dingdong Yi",
    "Xinran Li", "Shaoyang Ning", "Zhirui Hu", "Chenguang Dai", "Yucong Ma", "Wenshuo Wang",
    "Han Yan", "Shuang Song", "Buyu Lin", "Xiaodong Yang", "Yuanchuan Guo"
]

postdoc = ["Saunak Sen", "Steve Z. Qin", "Erin Conlon", "Haiyan Huang", "Xin Lu", "Yves Atchade", "Ping Ma",
    "Lei Shen", "Yu Zhang", "Cristian Catillo-Davis", "Lihua Zou", "Guocheng Yuan", "Wenxuan Zhong",
    "Jinfeng Zhang", "Rajesh Chowdhary", "Xuxin Liu", "Ke Deng", "Chunlin Ji", "Ming Hu",
    "Feng Hong", "Di Wu", "Yang Liu", "Qian Lin", "Bo Li", "Minsuk Shin", "Xin Xing",
    "Songpeng Zu", "Taehee Lee", "Yichao Li"
]

work = ["Harvard University", "Tsinghua University", "Stanford University"]
edu = ["University of Chicago", "Rutgers University", "Peking University"]
award = [
    "NSF Career Award", "ASA Fellow", "IMS Fellow", "ISCB Fellow",
    "Morningside Gold Medal", 
    "Pao-Lu Hsu Lecturer", "Jerome Sacks Award", "Pao-Lu Hsu Award",
    "ICSA Distinguished Achievement Award", "Kuwait Lecture", "Bernoulli Lecture", "IMS Medallion Lecture", 
    "Mitchell Prize", "Terman Fellowship"
    # "COPSS Presidents' Award", "National Academy of Sciences Elected Member" 
]

# Combine and assign categories
name_category_map = {}
for name in names:
    name_category_map[name] = 'phd'
for name in postdoc:
    name_category_map[name] = 'postdoc'
for name in work:
    name_category_map[name] = 'work'
for name in edu:
    name_category_map[name] = 'edu'
for name in award:
    name_category_map[name] = 'award'

# Assign frequencies with slight variation
# frequencies = {name: random.randint(10, 13) for name in name_category_map.keys()}
frequencies = {}
for name in name_category_map:
    category = name_category_map[name]
    if category in ['phd', 'postdoc']:
        frequencies[name] = random.randint(12, 14)
    elif category in ['work', 'edu']:
        frequencies[name] = random.randint(17, 20)
    elif category == 'award':
        frequencies[name] = random.randint(12, 14)

# Color scheme by category
category_colors = {
    'phd': '#011f5b', 
    'postdoc': '#06aafc',
    'work': '#990000',
    'edu': '#532a85',
    'award': 'darkorange'
}

# Custom color function
def color_func(word, **kwargs):
    category = name_category_map.get(word, 'phd')
    return category_colors.get(category, 'black')

# WordCloud size: 2238x706, centered vertical fifth
width_ultra = 2238
height_ultra = 706
fifth_width_ultra = width_ultra // 5
start_ultra = (width_ultra - fifth_width_ultra) // 2
end_ultra = start_ultra + fifth_width_ultra

mask_ultra = np.zeros((height_ultra, width_ultra), dtype=np.uint8)
mask_ultra[:, start_ultra:end_ultra] = 255

# Generate the word cloud with setup matching the new resolution and layout
wc_ultra_custom = WordCloud(
    width=width_ultra,
    height=height_ultra,
    background_color='white',
    mask=mask_ultra,
    contour_color='white',
    contour_width=0,
    font_path=font_path_to_use,
    prefer_horizontal=1.0,
    relative_scaling=0.5,
    min_font_size=20,
    max_font_size=50,
    color_func=color_func
).generate_from_frequencies(frequencies)

# Save to specified path
output_path_custom = "./junliu_students.png"
wc_ultra_custom.to_file(output_path_custom)

output_path_custom
