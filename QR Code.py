import qrcode

#https://cs50.harvard.edu/x/2024/
#https://github.com/AbdulMoazzim/

img1 = qrcode.make("https://github.com/AbdulMoazzim/")
img1.save("MyGithub.png")

img2 = qrcode.make("https://cs50.harvard.edu/x/2024/")
img2.save("CS50.png")