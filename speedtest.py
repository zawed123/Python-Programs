# https://www.facebook.com/marc.bily.330/posts/100690471811357
# Subscribed by Tushar Verma
# Check Your Internet Connection Speed Test.
import os
try:
    os.system('cmd /k "speedtest-cli --simple"') 
except:
    print('Check Your Internet Connection Or You Have To Install speedtest-cli.')
