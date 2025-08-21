def find_missing_ranges(frames: list[int]) -> dict:
    if not frames:
        return {"gaps": [], "longest_gap": [], "missing_count": 0}

    max_frame = 0
    for f in frames:
        if f > max_frame:
            max_frame = f

    frame_set = set(frames)

    gaps = []
    longest_gap = []
    missing_count = 0

    i = 1
    while i <= max_frame:
        if i not in frame_set:
            start = i
            while i <= max_frame and i not in frame_set:
                i += 1
            end = i - 1
            gaps.append([start, end])
            missing_count += (end - start + 1)

            if not longest_gap or (end - start) > (longest_gap[1] - longest_gap[0]):
                longest_gap = [start, end]
        i += 1

    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }
