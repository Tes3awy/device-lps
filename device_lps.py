#!/usr/bin/python3
import re
from datetime import date, datetime

print(
    "\nAverage LPS will be printed to the screen and can also be found at the bottom of the samples file with today's date."
)
# import pudb; pudb.set_trace()
# device_type = sys.argv[1]

# [(<logs_per_second> x 86400) x <days_of_retention>] x <average_log_size_bytes> ÷ (1024 x 1024 x 1024)

# sourcery skip: ensure-file-closed, swap-if-else-branches, use-named-expression
infile = open("device_lps.txt", "rt")
outfile = open(f"samples_{date.today()}.log", "wt+")
samples = []

for line in infile:
    if "Log incoming rate" in line:
        curr_sample = re.search("\d+", line).group()
        samples.append(float(curr_sample))
        outfile.write(f"{curr_sample}\n")
    elif "Incoming log rate" in line:
        curr_sample = line[20:]
        curr_sample = "".join(curr_sample.split())
        samples.append(float(curr_sample))
        outfile.write(f"{curr_sample}\n")

total_of_samples = sum(samples)
num_of_samples = len(samples)

if not num_of_samples:
    raise SystemExit("Wasn't able to obtain any sample values!")
else:
    avg_lps = total_of_samples / num_of_samples

print(f"Average rate LPS is {avg_lps:.5f}")
outfile.writelines([str(datetime.now()), " Average LPS is: ", str(avg_lps)])
outfile.close()
