from PIL import Image
import getpass

username = getpass.getuser()
print(username)

image_1 = Image.open(
    r'C:\Users\%s\Documents\Important\Screenshot_balance.png' % username)
image_2 = Image.open(
    r'C:\Users\%s\Documents\Important\Screenshot_summary.png' % username)

im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')

image_list = [im_2]
im_1.save(r'C:\Users\%s\Documents\Important\\Screenshot_summary.pdf' % username,
          save_all=True, append_images=image_list)
