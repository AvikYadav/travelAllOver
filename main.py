from PIL import Image
me = Image.open('me.jpg')
bg = Image.open('paris.jpg')
bg.paste(me , ( 0 , 0 ) , me )
bg.show()
bg.save("fail.jpg")
