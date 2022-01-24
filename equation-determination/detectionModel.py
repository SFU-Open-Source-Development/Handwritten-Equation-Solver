from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# load the model
model = load_model('handWritten_Detection.h5')

# function expects an image contains 0-9 or (+,-,*,/)
# returns corresponding number or operator
def inputImage (i):
    img = image.load_img(i, target_size=(28, 28))
    x = image.img_to_array(img)
    y = np.expand_dims(x, axis=0)
    classes =(model.predict(y) > 0.5).astype("int32")
    for x in range(14):
        if classes[0][x] == 1:
            if x == 0:
                return 0
            elif x == 1:
                return 1
            elif x == 2:
                return 2
            elif x == 3:
                return 3
            elif x == 4:
                return 4
            elif x == 5:
                return 5
            elif x == 6:
                return 6
            elif x == 7:
                return 7
            elif x == 8:
                return 8
            elif x == 9:
                return 9
            elif x == 10:
                return '+'
            elif x == 11:
                return '-'
            elif x == 12:
                return '*'
            elif x == 13:
                return '/'
            break

#tests
#result1 = inputImage('numbersTest3/test/zero/1.png') 
#print(result1)
#result2 = inputImage('numbersTest3/test/one/2.png') 
#print(result2)
#result3 = inputImage('numbersTest3/test/two/3.png') 
#print(result3)
#result4 = inputImage('numbersTest3/test/plus/4.png') 
#print(result4)
#result5 = inputImage('numbersTest3/test/minus/5.png')
#print(result5)