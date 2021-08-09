'''
Parses data from '.out' file for objects detected and stores them in 'data.json' file.
Output Format is a list of dicts.
frame_no: dict
{
"1":{'persons': 2,'bags':3},
...
}

index in the array represent the frame number
'''
import json
counts = {}
lines_ = []
with open('slurm-9099279.out') as f:
    lines = f.readlines()
    lines_.append(lines)

'''
#For video
# Remove last, start few lines
lines_ = lines_[0][5:]
lines_ = lines_[:-4] 

for i in range(len(lines_)):
    extracts = lines_[i].split('384x640')
    #['video 1/1 (10/56626) /scratch/vc2118/yolov5/wtc.mp4: ', ' 1 person, Done. (0.010s)\n']
    #Extract frame_no
    temp = extracts[0].split(' (') # ['video 1/1', '10/56626) /scratch/vc2118/yolov5/wtc.mp4: ']
    frame_no = int(temp[1].split('/')[0])
    extracts = extracts[1] # its a string
    # Remove last 'Done. (0.010s)\n' part
    extracts = extracts[:-15]
    #Now extract items 
    extract = extracts.split(',')
    # Remove spaces
    extract = [x.strip(' ') for x in extract] # ['13 persons', '2 cars', '1 traffic light', '1 tv', '']
    frame_dict = {}
    for item in extract[:-1]:
        items = item.split()# ['13', 'persons']
        frame_dict[items[1]] = int(items[0])
    counts[frame_no] = frame_dict
'''


# Remove last, start few lines
lines_ = lines_[0][5:]

for i in range(2,len(lines_)-3):
    extracts = lines_[i].split('384x640')
    frame_no = extracts[0].split('/')[-1][:-6]
    if frame_no == '':
        continue
    #print(frame_no)
    #print(extracts[-1])
    extracts = extracts[-1].split('Done')
    extracts = extracts[0].split(',')
    #print(extracts)
    
    item = {}
    for element in extracts:
        element = element.strip()
        no_ele = element.split()
        if len(no_ele) == 2:
            item[no_ele[-1]] = int(no_ele[0])
    counts[int(float(frame_no))] = item
counts = dict(sorted(counts.items()))
with open('data.json', 'w') as f:
    json.dump(counts, f)

