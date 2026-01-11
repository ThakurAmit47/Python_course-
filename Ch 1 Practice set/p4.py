# lebel p3 file
# Os ko import kr rhe isse os ka access mile
import os
# path enter kr rhe jisse proper location pe poch sake jisko folder ko dekhna hai
path = "C:/Users/acer/Desktop/Data Science/Python/Practice set ch1"
# isse content bataega kya kya hai folder mai
content = os.listdir(path)
# je excute karega kitni files hai batae ke liye
for item in content:
    print(item)
