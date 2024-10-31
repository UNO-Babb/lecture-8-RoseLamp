def main():
  pitching = open("MLB_Pitching.csv", 'r')
  team_data = []
  
  #get the import info out of pitching and store into team_data
  for line in pitching:
    info = line.split(",")
    name = info[0]
    runs_allowed = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]

    team_data.append ([name,"", runs_allowed, wins, losses, era])
    
  pitching.close()

  hitting = open("MLB_Hitting.csv", 'r')
    
  teamCount = 0  
  for line in hitting:
    info = line.split(",")
    runs_scored = info[3]
    #print(runs_scored)
    team_data[teamCount][1] = runs_scored
    print(team_data[teamCount])
    teamCount = teamCount + 1
    
  #process all the data in hitting and add to the correct portion of the team_data

  hitting.close()


  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  for line in team_data:

    output = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line [5] + "/n"
    outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()
