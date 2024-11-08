def insertionSort(schedule):
  for i in range(1, len(schedule)):
    train, dest, time = schedule[i] 
    hour = int(time.split(":")[0])
    j = i - 1
    prevTrain, prevDest, prevTime = schedule[j][0], schedule[j][1], schedule[j][2]
    prevHour = int(prevTime.split(":")[0])
    while j>=0 and (prevTrain > train or (prevTrain == train and prevHour < hour)): #insertion condition as per question (if curr train name less than train[j] or (same name and time high then sorting )
      schedule[j+1] = schedule[j]
      j -= 1
      prevTrain, prevDest, prevTime = schedule[j][0], schedule[j][1], schedule[j][2]
      prevHour = int(prevTime.split(":")[0])
    schedule[j+1] = (train, dest, time)
  return schedule


input_file = open("E:\CSE221\input4.txt","r")
output_file = open("E:\CSE221\output4.txt","w")

n = int(input_file.readline())

schedule = []

for i in range(n):
  info = input_file.readline().split(" ")
  name = info[0]
  district = info[4]
  time = info[-1][:-1]
  schedule.append([name,district,time])
  #print(schedule)

sortedSchedule = insertionSort(schedule)
print(sortedSchedule)
for i in range(n):
  output_file.write(f"{sortedSchedule[i][0]} will departure for {sortedSchedule[i][1]} at {sortedSchedule[i][2]}\n")
output_file.close()