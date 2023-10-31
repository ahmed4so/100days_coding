# Import the Speedtest class from the speedtest library
from speedtest import Speedtest

# Create a Speedtest object
speed = Speedtest()

# Display a message indicating that we are testing download speed
print("Getting download speed ......")

# Measure the download speed and store the result in the 'download' variable
download = speed.download()

# Convert the download speed from bits per second to megabits per second
download = download / 1024 / 1024

# Display a message indicating the type of speed (download) and the measured speed
print("The download speed is ")
print(f" Download : {download:.2f} mbps")

# Display a message indicating that we are testing upload speed
print("Getting upload speed ......")

# Measure the upload speed and store the result in the 'upload' variable
upload = speed.upload()

# Convert the upload speed from bits per second to megabits per second
upload = upload / 1024 / 1024

# Display a message indicating the type of speed (upload) and the measured speed
print("The upload speed is ")
print(f" Upload : {upload:.2f} mbps")
