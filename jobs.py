# Soln: we need to maximize John's earnings while also keeping track of the number of jobs and earnings left for other employees. 
# The key is to sort the jobs by their end times, which allows us to select jobs in a way that maximizes the earnings without overlapping time slots. 

def calculate_earnings(jobs):
  # sort jobs by end time
  jobs.sort(key=lambda x : x[1])

  current_time = 0
  earnings = 0
  job_count = 0

  # compare start time to current time
  for job in jobs:
    start_time, end_time, profit = job
    if start_time >= current_time:
      earnings += profit
      current_time = end_time
      job_count += 1

  jobs_left = len(jobs) - job_count
  earnings_left = sum(job[2] for job in jobs) - earnings

  return earnings_left, jobs_left

# This function takes user input for job start time, end time, and earnings, and calculates the total earnings and number of jobs that can be completed within a given time frame.
# It then prints the number of tasks and earnings available for others.
def main():
  try:
    n = int(input("Enter the number of jobs: "))

    #check if n is in range
    if not 0 <= n <= 10:
      print("Job number is out of range")
      return
    
    jobs = []

    # get input for the number of jobs
    for i in range(n):
      start_time = int(input("Enter job start time (HHMM 24HRS format): "))
      end_time = int(input("Enter job end time (HHMM 24HRS format): "))
      profit = int(input("Enter job earnings: "))

      # check if time fits into time range
      if not 0 <= start_time <= 2359 or not 0 <= end_time <= 2359 or start_time >= end_time:
          print("Invalid job timings")
          return
      jobs.append((start_time, end_time, profit))

    earnings_left, jobs_left = calculate_earnings(jobs)

    print("The number of tasks and earnings available for others\nTask: {}\nEarnings: {}".format(jobs_left, earnings_left))
  except Exception as e:
    print("Invalid input \n\nDetailed error: \n\n{}".format(e))


if __name__ == "__main__":
    main()
