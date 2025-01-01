def find_minimum_platforms(arrival, departure):

    """Approach:
Sort the Timings:

Sort both arrival and departure arrays.
Use Two Pointers:

Use one pointer for arrivals (i) and one for departures (j).
Traverse the sorted arrays and count the number of platforms needed at any time.
Logic:

If the arrival of the next train is earlier than or equal to the departure of the currently parked train, increase the count of platforms.
Otherwise, decrease the count of platforms as the train has departed.
Keep Track of the Maximum:

At each step, update the maximum number of platforms required."""
    arrival.sort()
    departure.sort()

    max_platform=0
    needed_platform=0
    i=0
    j=0
    n = len(arrival)

    while i < n and j  < n:
        if arrival[i] <= departure[j]:
            needed_platform +=1

            i +=1

            max_platform = max(max_platform , needed_platform)
        else:
            needed_platform -=1
            j +=1
    return max_platform

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print(find_minimum_platforms(arrival, departure))

class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        platform_needed =0
        max_platforms =0
        i=0
        j=0
        while i < len(arr) and j <len(dep):
            if arr[i] <= dep[j]:
                platform_needed +=1
                i+=1
                max_platforms=max(max_platforms, platform_needed)
            else:
                platform_needed -=1
                j+=1
        return max_platforms