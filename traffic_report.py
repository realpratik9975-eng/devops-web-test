from collections import Counter

log_file = "access.log"

total_requests = 0
successful_requests = 0
not_found_requests = 0

url_counter = Counter()

with open(log_file, "r") as file:
    for line in file:
        if '"GET ' in line:
            total_requests += 1

            request = line.split('"')[1]
            parts = request.split()

            method = parts[0]
            url = parts[1]

            url_counter[url] += 1

            if '" 200 ' in line:
                successful_requests += 1

            elif '" 404 ' in line:
                not_found_requests += 1

print("Traffic Report")
print("--------------")
print(f"Total requests : {total_requests}")
print(f"Successful     : {successful_requests}")
print(f"404 errors     : {not_found_requests}")

if total_requests > 0:
    error_rate = (not_found_requests / total_requests) * 100
    print(f"404 error rate : {error_rate:.2f}%")

print()
print("Top URLs")
print("--------")

for url, count in url_counter.most_common():
    print(f"{url:15} : {count}")
