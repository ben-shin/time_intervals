import os
from datetime import datetime

def get_time_intervals(start_dir=5, end_dir=405):
    time_data = {}
    fmt = "%Y-%m-%d %H:%M:%S.%f"
    
    for i in range(start_dir, end_dir + 1):
        acqu_path = f"./{i}/acqu"
        if not os.path.exists(acqu_path):
            continue
            
        with open(acqu_path, 'r') as f:
            for line in f:
                # Look for the timestamp line starting with $$
                if line.startswith("$$ 202"):  # Adjust '202' based on the year
                    # Extract the date/time string: '2025-12-19 16:13:11.307'
                    time_str = line.split('+')[0].replace('$$', '').strip()
                    time_data[i] = datetime.strptime(time_str, fmt)
                    break
    
    if start_dir not in time_data:
        print(f"Error: Could not find timestamp for directory {start_dir}")
        return

    t0 = time_data[start_dir]
    intervals = {}
    
    print(f"{'Directory':<10} | {'Elapsed (min)':<15} | {'Timestamp'}")
    print("-" * 45)
    
    for i in sorted(time_data.keys()):
        diff = time_data[i] - t0
        minutes = diff.total_seconds() / 60.0
        intervals[i] = minutes
        print(f"{i:<10} | {minutes:<15.2f} | {time_data[i]}")
        
    return intervals

if __name__ == "__main__":
    intervals = get_time_intervals()
