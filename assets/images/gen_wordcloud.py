from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

# Try to find a Helvetica font on the system
helvetica_path = None
for font in font_manager.findSystemFonts(fontpaths=None, fontext='ttf'):
    if "Helvetica" in font:
        helvetica_path = font
        break

# If Helvetica is not found, use fallback font
font_path_to_use = helvetica_path if helvetica_path else None


names = [
    "Chiara Sabatti", "Scott C. Schmidler", "Yuguo Chen", "Xiaole S. Liu", "Tanya Logvinenko",
    "Mayetri Gupta", "Shane Jensen", "Hosung Kang", "Gopi Goswami", "Peng Zhang", "WE Johnson",
    "Jiajun Gu", "Xiaodan Fan", "Tingting Zhang", "Wei Zhang", "Yuan Yuan", "Jing Zhang",
    "Paul Edlefsen", "Roee Gutman", "Bo Jiang", "Lei Guo", "Simeng Han", "Daniel Fernandez",
    "Matey Neykov", "Yang Li", "Victoria Krakovna", "Xufei Wang", "Jiexing Wu", "Dingdong Yi",
    "Xinran Li", "Shaoyang Ning", "Zhirui Hu", "Chenguang Dai", "Yucong Ma", "Wenshuo Wang",
    "Han Yan", "Shuang Song", "Buyu Lin", "Xiaodong Yang", "Yuanchuan Guo", "Saunak Sen",
    "Steve Z. Qin", "Erin Conlon", "Haiyan Huang", "Xin Lu", "Yves Atchade", "Ping Ma",
    "Lei Shen", "Yu Zhang", "Cristian Catillo-Davis", "Lihua Zou", "Guocheng Yuan", "Wenxuan Zhong",
    "Jinfeng Zhang", "Rajesh Chowdhary", "Xuxin Liu", "Ke Deng", "Chunlin Ji", "Ming Hu",
    "Feng Hong", "Di Wu", "Yang Liu", "Qian Lin", "Bo Li", "Minsuk Shin", "Xin Xing",
    "Songpeng Zu", "Taehee Lee", "Yichao Li"
]

# Frequency dictionary
word_frequencies_uniform = {name: 10 for name in names if name not in ["Wing Hung Wong", "Augustine Kong"]}

# Define ultra-wide 5K resolution and mask
width_ultra = 2238
height_ultra = 706
fifth_width_ultra = width_ultra // 5
start_ultra = (width_ultra - fifth_width_ultra) // 2
end_ultra = start_ultra + fifth_width_ultra

# Create the mask
mask_ultra = np.zeros((height_ultra, width_ultra), dtype=np.uint8)
mask_ultra[:, start_ultra:end_ultra] = 255

# Generate the word cloud
wc_ultra = WordCloud(
    width=width_ultra,
    height=height_ultra,
    background_color='white',
    mask=mask_ultra,
    contour_color='white',
    contour_width=0,
#    font_path=font_path_to_use,
    prefer_horizontal=1.0,
    relative_scaling=0,
    min_font_size=20,
    max_font_size=40
).generate_from_frequencies(word_frequencies_uniform)

# Plot the result
plt.figure(figsize=(22.3, 7.1))  # inches corresponding to pixel resolution
plt.imshow(wc_ultra, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.show()

output_path = "./junliu_students.png"
wc_ultra.to_file(output_path)

output_path
