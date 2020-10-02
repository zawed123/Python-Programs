frames = []
page_fault = 0

try : 
    frame_num = int(input("Enter Number of frames that you want : "))
    page_no = input("Enter the page number seperate with dot(.) : ")
    page_list = page_no.split('.')
except Exception as e :
    print(e)

for page in page_list :
    if (len(frames) == frame_num) :
        if page not in frames :
            frames.pop(0)
            frames.append(page)
            print(frames)
            page_fault += 1
        else :
            element = frames.pop(0)
            frames.append(element)
    else :
        if page not in frames :
            frames.append(page)
            print(frames)
            page_fault += 1

print(page_fault)
