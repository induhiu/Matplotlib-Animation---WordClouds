from wordcloud import WordCloud, STOPWORDS
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# create a figure
fig = plt.figure()

# read in txt file
txt = ""
with open("all_poems.txt", "r", encoding="utf-8") as file:
    txt = file.read()

# set stopwords
stpwds = set(STOPWORDS)

def animate(i):
    ''' Parameter i is the frame number.
        '''
    # create wordcloud with max_words set as i
    wc = WordCloud(background_color="white", max_words=100-i)
    wc.generate(txt)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    return fig,

# # # create an animation object
anim = FuncAnimation(fig, animate, frames=100, interval=250, blit=True)
anim.save('raw_animation.mp4', writer="imagemagick")
