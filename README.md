# Detecting Missing Video Frames

This is a solution to a hackathon problem where a surveillance platform receives
video frames with incremental numbers. Some frames may be missing due to network
issues or hardware lag.  

The task is to:
- Detect the missing frame ranges (gaps).
- Find the longest missing range.
- Count the total number of missing frames.

##  How It Works
We:
1. Find the maximum frame number in the list.
2. Store all received frames in a set for O(1) lookups.
3. Scan from `1` to `max_frame`, detecting gaps along the way.
4. Track the longest gap and count missing frames.

This avoids built-in sort functions and works in **O(n)** time.

---

##  Example

```python
from missing_frames import find_missing_ranges

frames = [1, 2, 3, 5, 6, 10, 11, 16]
result = find_missing_ranges(frames)
print(result)
