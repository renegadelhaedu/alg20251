from PIL import Image
import matplotlib.pyplot as plt


img = Image.open('C:\\Users\\Rene\\Desktop\\suino.png')

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,10))


axes[0].imshow(img)

axes[1].imshow(img, cmap='gray')

plt.show()